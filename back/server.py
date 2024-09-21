from flask import Flask, jsonify, request, redirect, url_for, send_from_directory
from flask_cors import CORS
import os

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


@app.route('/toggleLeds')
def turnOn():
    return jsonify('success')

@app.route('/getGifNames')
def getGiffs():
    return jsonify(os.listdir('./gifs'))

@app.route('/gifs/<path:filename>')
def gifs(filename):
    return send_from_directory('./gifs', filename)


@app.route('/test', methods=['POST'])
def post_data():
    data = request.json  # Get JSON data from the request
    return jsonify(data)  # Echo the received data back


@app.route('/upload', methods=['POST'])
def upload_file():
    if not os.path.exists('./gifs'):
        os.makedirs('./gifs')

    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)
    if not is_valid_gif(file):
        return 'Invalid GIF file', 400

    fin = file.filename.replace(' ', '')
    file.save(f'./gifs/{fin}')
    return 'File uploaded successfully!'



if __name__ == '__main__':
    app.run(port=5000)
