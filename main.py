from ultralytics import YOLO
import cv2

# load yolov8 model
model = YOLO('yolov8.pt')

# load video
video_path = './test.jpg'
cap = cv2.VideoCapture(video_path)

ret = True
# read frames
while ret:
    ret, frame = cap.read()

    # detect objects
    # track objects
    results = model.track('./test.jpg', persist=False)

    # plot results
    frame_ = resuls[0].plot()
        
    # visualize
    cv2.imshow(frame, 'frame')
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    
