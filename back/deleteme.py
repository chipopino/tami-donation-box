from PIL import Image
import numpy as np

gif = Image.open('deleteme.gif')

frame_number = 0
frames = []

while True:
    try:
        gif.seek(frame_number)  # Go to the frame
        frame_array = np.array(gif)  # Convert the frame to a NumPy array
        # print(f'Frame {frame_number} pixels:')
        # print(frame_array)
        frame_number += 1
        frames.append(frame_array)
    except EOFError:
        break  # Exit the loop when all frames are processed

frames = frames[1:len(frames)]

for f in range(len(frames)):
    for y in range(len(frames[f])):
        for x in range(len(frames[f][y])):
            print('frame: ', f, ',' , x, y, frames[f][y][x])
