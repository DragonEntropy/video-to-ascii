import cv2
import numpy as np
import math

#Aim: 16:9 ratio
#IDE limit: 156:44 = 39:11
#Approx X to Y ratio: 2:1




#Note: All colours are in BGR format

#Returns a mask made of black and white pixels only
def apply_mask(img, lower_bound, upper_bound):
    mask = cv2.inRange(img, lower_bound, upper_bound)
    return mask

#The range of target pixels
lower_bound = np.array([230, 230, 230])
upper_bound = np.array([255, 255, 255])

src = "apple reduced.mp4"
vid = cv2.VideoCapture(src)

final_width = 101
final_height = 44
width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))

blank = cv2.imread("blank.png")
cv2.imshow('frame', blank)
cv2.waitKey(10000)

while 1 == 1:
    ret, frame = vid.read()
    mask = apply_mask(frame, lower_bound, upper_bound)
    cv2.imshow('frame', mask)
    if not ret:
        break

    #Collects pixels to be treated as one character
    grid = np.zeros((final_height, final_width, 2))
    for y in range(0, height):
        y_grid = math.floor(final_height * y / height)
        for x in range(0, width):
            x_grid = math.floor(final_width * x / width)
            if mask[y][x] == 0:
                grid[y_grid][x_grid][0] += 1
            grid[y_grid][x_grid][1] += 1

    #Finds final output of each character
    img_string = ""
    for y in range(0, final_height):
        img_string = img_string + "\n"  
        for x in range(0, final_width):
            #print("Value 1 is: {0}; Value 2 is: {1}".format(*grid[y][x]))
            if grid[y][x][0]/grid[y][x][1] >= 0.45:
                img_string = img_string + "0"
            else:
                img_string = img_string + " " 
    print(img_string)

    cv2.waitKey(10)

