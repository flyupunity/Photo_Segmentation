from ultralytics import YOLO

# train new model
model = YOLO('yolov8m.yaml')
results = model.train(data='config.yaml', epochs=5)

ret = True
# read frames
while ret:
    #ret, frame = cap.read()

    # detect objects
    # track objects
    results = model.track('./test.jpg', persist=False)

    # plot results
    frame_ = resuls[0].plot()
        
    # visualize
    cv2.imshow(frame, 'frame')
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    
