import cv2
img = cv2.imread("poster.jpg")
cordenada = img [120:360,400:500]
img[0:240,500:600]=cordenada
text = "Me gusta mucho programar"
cv2.putText(img,text,
            (20,220),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(0,0,255))
cv2.imshow("Muestra la imagen",img)

cv2.waitKey(0)