from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.pt")  # load a pretrained model (recommended for training)

# Display model information (optional)
model.info()

# Train the model
results = model.train(data="/workspace/dataset/dataset.yaml", epochs=10, imgsz=640)
print(results)

# Evaluate the model's performance on the validation set
metrics = model.val()

# Export the model to ONNX format
success = model.export(format="onnx")