import cv2

videoCap = cv2.VideoCapture('cars.mp4')
carCascade = cv2.CascadeClassifier('cars.xml')

# Read until video is loaded
while True:
    if carCascade.empty():
        print("Error: Could not load cascade file.")
        exit()

    ret, frame = videoCap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect cars in the video
    cars = carCascade.detectMultiScale(gray, 1.1, 3)

    # Draw a rectangle around each car
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Car Detection', frame)

    # Press 'z' on keyboard to exit
    if cv2.waitKey(90) & 0xFF == ord('z'):
        break

videoCap.release()
cv2.destroyAllWindows()
