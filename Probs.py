from ultralytics import YOLO
import cv2
from PIL import Image

MODEL = 'yolo11s-cls.pt'
VAL_IMG = 'images/original.jpeg'

# Load a COCO-pretrained YOLO11n model
model = YOLO(MODEL)

# Train the model on the COCO8 example dataset for 100 epochs
# results = model. train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLO11n model on the 'bus.jpg' image
results = model(VAL_IMG)

# from ndarray
im2 = cv2.imread(VAL_IMG)
results = model.predict(source=im2, save=True, save_txt=True)  # save predictions as labels

# from list of PIL/ndarray
results = model.predict(source=[ im2])

# View results
for r in results:
    print(r.probs) 