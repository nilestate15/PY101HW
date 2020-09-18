#Problem 2
import cv2
import numpy as np
#File location of picture
filenm = "/opt/miniconda3/envs/PY101/Week2/HW3/ANT.png"
#Reads in image
img = cv2.imread(filenm)
#Prints shape of image/array
print(np.shape(img))#Look an alpha channel
#Transpose image
A = np.transpose(img, (1,0,2)).copy()
#Rotates image
B = np.rot90(img).copy() ## We need to copy() here if we want a new object
#Put images into variable for loop
imgs = (img, A, B)
for i in imgs:
    #Shows image
    cv2.imshow("",i)
    #Press any key to go to next image
    cv2.waitKey(0)
