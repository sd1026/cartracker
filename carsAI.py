import cv2
video = cv2.VideoCapture(' # Your mp4 files goes here')
car_tracker_file = 'cars.xml' # files from library of OpenCV
car_tracker = cv2.CascadeClassifier(car_tracker_file)
pedestrian_tracker_file = 'pedestrian.xml' # files from library of OpenCV
pedestrian_tracker = cv2.CascadeClassifier('pedestrian.xml')
while True:
    (success, frame) = video.read()
    if success:
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break
    cars = car_tracker.detectMultiScale(grayscaled_frame)
    pedestrians = pedestrian_tracker.detectMultiScale(grayscaled_frame)
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
    for (x, y, w, h) in pedestrians:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('AI Driven Car Tracker', frame)
    key = cv2.waitKey(2)
    if key==81 or key==113:
        break
video.release()