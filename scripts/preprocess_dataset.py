import os
from PIL import Image

DATASET_FOLDERS = [
    "train/images",
    "test/images"
]

def check_images():
    total_images = 0
    corrupt_images = []

    for folder in DATASET_FOLDERS:
        if not os.path.exists(folder):
            print(f"Folder not found: {folder}")
            continue

        for filename in os.listdir(folder):
            if filename.lower().endswith((".jpg", ".jpeg", ".png")):
                total_images += 1
                path = os.path.join(folder, filename)

                try:
                    with Image.open(path) as img:
                        img.verify()
                except Exception:
                    corrupt_images.append(path)

    print("Dataset check completed.")
    print(f"Total images found: {total_images}")
    print(f"Corrupt images found: {len(corrupt_images)}")

    if corrupt_images:
        print("\nCorrupt image files:")
        for img in corrupt_images:
            print(img)

if __name__ == "__main__":
    check_images()