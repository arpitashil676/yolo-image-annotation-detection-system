import os
import cv2

INPUT_FOLDER = "train/images"
OUTPUT_FOLDER = "augmented_images"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

count = 0

for filename in os.listdir(INPUT_FOLDER):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        image_path = os.path.join(INPUT_FOLDER, filename)
        image = cv2.imread(image_path)

        if image is None:
            continue

        flipped = cv2.flip(image, 1)

        output_path = os.path.join(OUTPUT_FOLDER, "flip_" + filename)
        cv2.imwrite(output_path, flipped)

        count += 1

print(f"Augmentation completed. {count} flipped images created.")