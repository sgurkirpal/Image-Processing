import cv2
import time
import matplotlib.pyplot as plt
cap=cv2.VideoCapture('project_video.mp4')
centers=[]
contours=[]
tim=[]
dist=[]
finaldist=[]
ret, frame1=cap.read()

ret, frame2=cap.read()

while(cap.isOpened()):
    asdf=[]
    r=0
    
    diff=cv2.absdiff(frame1,frame2)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur=cv2  .GaussianBlur(gray,(5,5),0)
    _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh,None,iterations=3)
    contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        (x,y,w,h)=cv2.boundingRect(contour)
        if(cv2.contourArea(contour)>5000 or cv2.contourArea(contour)<1100):
            continue
        asdf.append(contour)
        r=1
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
    if(r==1):
        tim.append(time.clock())
        cntx1 = asdf[0][0]
        cntx = asdf[0][1]
        pt1 = (cntx1[0][0],cntx1[0][1])
        pt2 = (cntx[0][0],cntx[0][1])

        distance=abs(pt1[0]-1750)
        dist.append(distance)
        # Find the distance D between the two contours:
       
    window = cv2.namedWindow('MAZE_NAME', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('MAZE_NAME', 600,600)
    frame1=cv2.rotate(frame1,cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow('MAZE_NAME',frame1)
    frame1=frame2
    
    ret,frame2=cap.read()
    if cv2.waitKey(50)==27:
        cv2.destroyAllWindows()
    if len(tim)>1 and tim[len(tim)-1]-tim[0]>4.5:
        break
    
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
cap = cv2.VideoWriter('output.MOV',fourcc, 20.0, (640,480))
cv2.destroyAllWindows()
cap.release()
for i in range(len(dist)):
    finaldist.append(1800-dist[i])

plt.plot(tim[:47],dist[:47])
plt.xlabel('time')
plt.ylabel('height')
plt.show()
