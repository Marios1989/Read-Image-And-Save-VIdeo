import cv2
#import numpy as np
#import glob

cap=cv2.VideoCapture('CAP_V4L2')

img_array = []
List = open("/home/user/PycharmProjects/Images/filenames.txt").readlines()
# getting length of list
length = len(List)
dir_name = '/home/user/PycharmProjects/Images/'

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(dir_name+ 'result.avi', fourcc, 1.0,(1280, 720))

for i in range(length):
    img_name=dir_name+List[i]
    img_name=img_name.replace('\n', '')
    img= cv2.imread(img_name)


    #write the flipped frame
    img = cv2.flip(img, -1)

    out.write(img)
    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    else:
        break


#Release everything if job is finished
out.release()
cap.release()
cv2.destroyAllWindows()
