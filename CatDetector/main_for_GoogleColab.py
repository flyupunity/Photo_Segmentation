#!git clone https://github.com/flyupunity/Photo_Segmentation

#!pip install ultralytics
#!pip install opencv-python

from ultralytics import YOLO
import cv2

# train new model
model = YOLO('yolov8n.yaml')
results = model.train(data='/content/Photo_Segmentation/CatDetector/config_for_GoogleClab.yaml', epochs=5)
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
    cv2.imwrite("summary", frame_)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
