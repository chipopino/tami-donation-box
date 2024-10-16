from flask import Flask, abort, jsonify, request, redirect, url_for, send_from_directory
from flask_cors import CORS
import os
import subprocess
import time

P_MNT = '/mnt/gifs'
P_GIFS = '/mnt/gifs/gifs'

def remountRO():
    for i in range(10):
        try:
            subprocess.run(['mount', '-o', 'remount,ro', P_MNT], check=True)
            break
        except:
            print("ERROR mounting /mnt/gifs as ro")
            time.sleep(1)

def remountRW():
    try:
        subprocess.run(['mount', '-o', 'remount,rw', P_MNT], check=True)
    except:
        abort(500, description=f'could not remount /mnt/gifs as rw')


def is_valid_gif(file, width=32, height=7):
    # try:
    #     with Image.open(file) as img:
    #         if img.format == 'GIF' and img.width == width and img.height == height:
    #             return True
    #         return False
    # except (IOError, SyntaxError):
    #     return False
    return True

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})


@app.route('/test', methods=['POST'])
def post_data():
    data = request.json
    return jsonify(data)  

@app.route('/toggleLeds')
def turnOn():
    return jsonify('success')

@app.route('/getGifNames')
def getGiffs():
    return jsonify(os.listdir(P_GIFS))

@app.route('/gifs/<path:filename>')
def gifs(filename):
    return send_from_directory(P_GIFS, filename)

@app.route('/deleteGif/<path:filename>')
def deleteGif(filename):
    file = os.path.join(P_GIFS, filename)
    
    remountRW()
    
    try:
        os.remove(file)
    except FileNotFoundError:
        print(f'File "{file}" not found')
        remountRO()
        abort(500, description=f'File "{file}" not found')
    except PermissionError:
        print(f'Permission to delete "{file}" denied')
        remountRO()
        abort(500, description=f'Permission to delete "{file}" denied')
    except Exception as e:
        print(f'An error occurred while deleting "{file}": {e}')    
        remountRO()
        abort(500, description=f'An error occurred while deleting "{file}": {e}')
    
    remountRO()
    return {}
    
@app.route('/upload', methods=['POST'])
def upload_file():
    
    remountRW()
    
    if not os.path.exists(P_GIFS):
        os.makedirs(P_GIFS)

    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)
    if not is_valid_gif(file):
        return 'Invalid GIF file', 400

    fin = file.filename.replace(' ', '')
    file.save(os.path.join(P_GIFS, fin))
    
    remountRO()
    
    return 'File uploaded successfully!'

@app.route('/<path:filename>')
def front(filename):
    return send_from_directory('../front/dist/', filename)


if __name__ == '__main__':
    app.run(port=5000)
