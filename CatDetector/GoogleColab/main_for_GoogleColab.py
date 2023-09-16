#!git clone https://github.com/flyupunity/photosegmentation_Package_Colab_.git

#!pip install ultralytics
#!pip install opencv-python

from ultralytics import YOLO
import cv2

# train new model
model = YOLO('yolov8n.yaml')
results = model.train(data='/content/photosegmentation_Package_Colab_/config_for_GoogleClab.yaml', epochs=50)
model.export(format='onnx')

ret = True
# read frames
while ret:
    #ret, frame = cap.read()

    # detect objects
    # track objects
    results = model.track('https://youtu.be/LNwODJXcvt4', persist=True)

    # plot results
    frame_ = results[0].plot()

    # visualize
    cv2.imwrite("summary", frame_)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
