from PIL import Image

def readGif(fileName):
    gif = Image.open(fileName)

    frame_number = 0
    frames = []

    # while True:
    #     try:
    #         gif.seek(frame_number)  # Go to the frame
    #         frame_array = np.array(gif)  # Convert the frame to a NumPy array
    #         frames.append(frame_array)  # Store the frame array
    #         frame_number += 1  # Increment the frame number
    #         # print(f'Frame {frame_number} pixels:')
    #         # print(frame_array)
    #     except EOFError:
    #         break  # Exit the loop when all frames are processed
    #     except OSError:
    #         print(f"Error loading frame {frame_number}, skipping...")
    #         frame_number += 1  # Skip the problematic frame and continue

    # frames = frames[1:len(frames)]

    return []



# readGif('gifs/deleteme4.gif')