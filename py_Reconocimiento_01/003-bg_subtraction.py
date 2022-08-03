import cv2

cap = cv2.VideoCapture("vtest.avi")
#fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()   #este codigo detecta fondo negro y personas en blanco
#fgbg = cv2.createBackgroundSubtractorMOG2()         #este codigo detecta fondo negro y personas en blanco más sombra en gris
fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()   #este codigo detecta fondo negro y personas mancha blanco incluye todo demora unos segundo cargar
while True:

    ret, frame = cap.read()
    if ret == False: break

    fgmask = fgbg.apply(frame)

    cv2.imshow("fgmask", fgmask)
    cv2.imshow("frame", frame)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()