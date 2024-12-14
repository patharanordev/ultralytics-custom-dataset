from ultralytics import YOLO

# Load a model
onnx_model = YOLO("/workspace/runs/detect/train/weights/best.pt")

# Run batched inference on a list of images
results = onnx_model([
    "/workspace/dataset/test/images/1036125_0.jpg",
    "/workspace/dataset/valid/images/Frame_400.jpg"
])  # return a list of Results objects
# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    obb = result.obb  # Oriented boxes object for OBB outputs
    result.show()  # display to screen
    result.save(filename="/workspace/output/result.jpg")  # save to disk