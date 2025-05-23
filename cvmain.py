import cv2
import pandas as pd
import numpy as np
import pickle
#img= cv2.imread("C:\\Users\\Mamidituhi\\Downloads\\P2.png")
#img = cv2.resize(img, (700, 500))
poslist=[]
with open('carpos','rb') as f:
    poslist=pickle.load(f)
width,height=26,15
def carparking(imgPro,img_copy):
    c=0
    for pos in poslist:
        x,y=pos
        crop=imgPro[y:y+height,x:x+width]
        #cv2.imshow(str(x*y),crop)
        count = cv2.countNonZero(crop)
        if count<=100:
            color=(0,255,0)
            c=c+1
        else:
            color=(0,0,255)    
        cv2.putText(img_copy, str(count), (x+1, y +9), cv2.FONT_HERSHEY_SIMPLEX, 0.4,(0,255,255),1 )
        cv2.rectangle(img_copy, pos, (pos[0]+width, pos[1]+ height), color, 1)
    cv2.putText(img_copy,"avaliable slots" +str(c), (10,10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255, 255, 255), 2)
    cv2.putText(img_copy,"Occupied Slots" +str(len(poslist)-c), (200,10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255, 255, 255), 2) 
    cv2.putText(img_copy,"Total Number of Slots" +str(len(poslist)), (400,10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255, 255, 255), 2) 
    d={'Total Number of Slots':[len(poslist)],'Occupied Slots':[len(poslist)-c],'avaliable slots':[c]}   
    data=pd.DataFrame(d)
    data.to_csv("output.csv",index=False) 
    
while True:
    img = cv2.imread("C:\\Users\\Mamidituhi\\Downloads\\P2.png")
    img_copy = cv2.resize(img, (700, 500))
    imggray=cv2.cvtColor(img_copy,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(imggray,(1,1),0)
    th=cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,21,16)
    medianblur=cv2.medianBlur(th,5)
    kernal=np.ones((3,3),np.uint8)
    dilate=cv2.dilate(medianblur,kernal,iterations=1)
    
    carparking(dilate,img_copy)
    #for pos in poslist:
     #   cv2.rectangle(img_copy, pos, (pos[0]+width, pos[1]+ height), (255, 0, 255), 1)
   
    cv2.imshow('Image with ROI', img_copy)

    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
    