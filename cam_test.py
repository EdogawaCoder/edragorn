import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise RuntimeError("Não consegui abrir a câmera (VideoCapture(0)).")

while True:
    ok, frame = cap.read()
    if not ok:
        break

    cv2.imshow("WSL Camera Test", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

