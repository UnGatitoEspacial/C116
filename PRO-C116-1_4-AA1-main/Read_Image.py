import cv2 

 #Leer la imagen
img = cv2.imread("butterfly.jpg")

#Muestra la imagen a color
cv2.imshow("Muestra la imagen", img) 
#print(img)

#convierte la imagen a color a una escala de grises
gray_img= cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("Escala de grises", gray_img)
cv2.waitKey(0)