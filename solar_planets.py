import cv2

img = cv2.imread('solar-system.jpg')


cv2.putText(img,"Sol",(100,80),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))
cv2.putText(img,"Mercurio",(115,180),cv2.FONT_HERSHEY_COMPLEX,0.4,(0,0,255))
cv2.putText(img,"Venus",(192,170),cv2.FONT_HERSHEY_COMPLEX,0.4,(0,0,255))
cv2.putText(img,"Terra",(282,170),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,0,255))
cv2.putText(img,"Marte",(385,180),cv2.FONT_HERSHEY_COMPLEX,0.4,(0,0,255))
cv2.putText(img,"Jupiter",(453,50),cv2.FONT_HERSHEY_COMPLEX,1.4,(0,0,255))
cv2.putText(img,"Saturno",(740,120),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,255))
cv2.putText(img,"Urano",(965,135),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(img,"Netuno",(1110,145),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.imwrite("solar_systemwithname.jpg", img)

img = cv2.imshow('Resultado', img)
cv2.waitKey(0)
