import cv2

# Загрузка видео
cap = cv2.VideoCapture("F:\\PythonProjects\\ArmedControll\\videos\\no_weapon\\V2.mp4")

# Инициализация алгоритма для вычитания фона
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Применение алгоритма для вычитания фона
    fgmask = fgbg.apply(frame)
    
    # Пороговая обработка для получения движущихся объектов
    _, thresh = cv2.threshold(fgmask, 127, 255, cv2.THRESH_BINARY)
    
    # Отображение результатов
    cv2.imshow('Motion', thresh)
    
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()