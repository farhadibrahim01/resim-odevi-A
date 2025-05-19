from PIL import Image
import os

BASE_DIR = r"C:\Resim-A\data\mental_dataset"
TARGET_SIZE = (224, 224)

def resize_all_images(base_path):
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                file_path = os.path.join(root, file)
                try:
                    img = Image.open(file_path).convert('RGB')
                    img = img.resize(TARGET_SIZE)
                    img.save(file_path)
                    print(f"Resized: {file_path}")
                except Exception as e:
                    print(f"Failed: {file_path} — {e}")

if __name__ == "__main__":
    resize_all_images(BASE_DIR)
