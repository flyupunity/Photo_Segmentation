from ultralytics import YOLO
import cv2

# train new model
model = YOLO('yolov8n.yaml')
results = model.train(data='config.yaml', epochs=5)
model.export(format='onnx')

ret = True
# read frames
while ret:
    #ret, frame = cap.read()

    # detect objects
    # track objects
    results = model.track('./test.jpg', persist=False)

    # plot results
    frame_ = results[0].plot()
        
    # visualize
    cv2.imshow(frame_, 'frame')
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    
