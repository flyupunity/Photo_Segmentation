import cv2
from ultralytics import YOLO

model = YOLO('best.pt')                                     # Load the YOLOv8 model

print("0)Train new model")
print("1)Test with web-camera")
print("2)Test with image/folder")
print("3)Test with video")
mode = input()

if mode == "0":
    model = YOLO('yolov8n.yaml')                            # load new model
    results = model.train(data='config.yaml', epochs=5)     # train model
    model.export(format='onnx')                             # save model in 'onnx' format
    
elif mode == "1":
    media_path = 0                                          # Open the video file
    cap = cv2.VideoCapture(media_path)
elif mode == "2":
    print("Please enter global or local image/folder path")
    media_path = input()#"train/images"#"test.jpg"#"test.jpg"
    results = model.track(source=media_path, show=True)
elif mode == "3":
    media_path = "test.mp4"                                 # Open the video file
    cap = cv2.VideoCapture(media_path)

if mode != "1": 
    success = False
if mode == "1" or mode == "3": 
    success = cap.isOpened()
    if success == False:
        print("Camera/video is not responding...")

while success:                                              # Loop through the video frames
    
    success, frame = cap.read()                             # Read a frame from the video
    if mode == "3": 
        results = model.track(source=frame, show=True)
    if mode == "1": 
        results = model.track(frame, persist=True)          # Run YOLOv8 tracking on the frame, persisting tracks between frames
    
    annotated_frame = results[0].plot()                     # Visualize the results on the frame
    #cv2.imshow("YOLOv8 Tracking", annotated_frame)          # Display the annotated frame

    if cv2.waitKey(1) & 0xFF == ord("q"):                   # Break the loop if 'q' is pressed
        break

if cv2.waitKey(1) & 0xFF == ord("q"):
    if mode != "1":
        cap.release()                                       # Release the video capture object and close the display window
    cv2.destroyAllWindows()

