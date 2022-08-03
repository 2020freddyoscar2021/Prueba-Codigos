import cv2

image= cv2.imread("001-ProcesoImportacion.jpg", 0)  #el cero 0 es para cambiar de color a gris la imagen
cv2.imshow("Image" , image)
cv2.imwrite("001-ColorGrisImagen.jpg", image)       #guardar imagen de color gris
cv2.waitKey(0)
cv2.destroyAllWindows()