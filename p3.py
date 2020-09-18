from PIL import ImageGrab
import numpy as np
import cv2
import time
from directkeys import PressKey, W,A,S,D,ReleaseKey
def main():
	while(True):
		img=np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        img=cv2.Canny(img,threshold1=200,threshold2=300)
        vertices=np.array([[10,500],[10,300],[300,200],[500,200],[800,300],[800,500]])
        roi=np.zeros_like(img)
        cv2.fillPoly(roi,vertices,255)
        roi=cv2.bitwise_and(img,roi)
		cv2.imshow('window', roi)
		if cv2.waitKey(25) & 0xFF==ord('q'):
			cv2.destroyAllWindows()
			break
