import cv2

captura = cv2.VideoCapture("videoSalida.avi") # cero "0" activa camara video de la pc prende , si le ponemos el nombre de archivo video de abre este
#salida = cv2.VideoWriter("videoSalida.avi", cv2.VideoWriter_fourcc(*"XVID"),20.0,(640,480))

while(captura.isOpened()):
    ret,imagen = captura.read()
    if ret == True:
        cv2.imshow("video",imagen)
       #salida.write(imagen)
        if cv2.waitKey(30) & 0xFF == ord("s"): #el 30 es tiempo de velocidad del video
            break
    else: break
captura.release()
#salida.release()
cv2.destroyAllWindows()