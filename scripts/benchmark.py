import time
from ultralytics import YOLO

MODEL_PATH = "runs/detect/train-3/weights/best.pt"
SOURCE_FOLDER = "test/images"

model = YOLO(MODEL_PATH)

start_time = time.time()

results = model.predict(
    source=SOURCE_FOLDER,
    conf=0.25,
    save=False,
    verbose=False
)

end_time = time.time()

total_images = len(results)
total_time = end_time - start_time
avg_time = total_time / total_images
fps = 1 / avg_time

print("Benchmark completed.")
print(f"Total images tested: {total_images}")
print(f"Total inference time: {total_time:.2f} seconds")
print(f"Average time per image: {avg_time:.4f} seconds")
print(f"Estimated FPS: {fps:.2f}")