import cv2
import numpy as np
import pickle

img = cv2.imread("C:\\Users\\Mamidituhi\\Downloads\\P2.png")
img = cv2.resize(img, (700, 500))
poslist=[]
try:
    with open("carpos",'rb') as f:
        poslist=pickle.load(f)
except:
    poslist=[]


width=26
height=15
def mouseclick(events,x,y,flag,params):
    if events==cv2.EVENT_LBUTTONDOWN:
        poslist.append((x,y))
    if events==cv2.EVENT_RBUTTONDOWN:
        for i,pos in enumerate(poslist):
            x1,y1=pos
            if x1<x<x1+width and y1<y<y1+height:
                poslist.pop(i)   
    with open("carpos",'wb') as f:
        pickle.dump(poslist,f)            
cv2.namedWindow('Image with ROI')
cv2.setMouseCallback('Image with ROI',mouseclick)
while True:
   
    img_copy = img.copy()
    for pos in poslist:
        cv2.rectangle(img_copy, pos, (pos[0]+width, pos[1]+ height), (255, 0, 255), 1)
    
    # Display the image
    cv2.imshow('Image with ROI', img_copy)
    
    # Exit condition
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()






#roi = cv2.selectROI("Select Region", img, fromCenter=False, showCrosshair=True)
#cv2.destroyWindow("Select Region")

# Extract ROI coordinates
#x, y, w, h = int(roi[0]), int(roi[1]), int(roi[2]), int(roi[3])