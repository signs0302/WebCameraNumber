import cv2

camera = cv2.VideoCapture(-1)

while True:
    ret, frame = camera.read()
    cv2.imshow('WebCamera', frame)
    # キー操作があればwhileループを抜ける
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 撮影用オブジェクトとウィンドウの解放
camera.release()
cv2.destroyAllWindows()