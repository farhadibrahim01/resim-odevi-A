import os
import shutil

source_base = r"C:\Resim-A\data\fer2013_images"
target_base = r"C:\Resim-A\data\mental_dataset"

# Etiket eşleştirmeleri
mapping = {
    'happy': 'healthy',
    'neutral': 'healthy',
    'sad': 'depression',
    'angry': 'bipolar',
    'fear': 'bipolar',
    'disgust': 'schizophrenia',
    'surprise': 'schizophrenia'
}

usages = ['train', 'val', 'test']

for usage in usages:
    source_usage_path = os.path.join(source_base, usage)
    for original_label in os.listdir(source_usage_path):
        if original_label not in mapping:
            continue  # eşleşmeyen sınıf varsa atla
        target_label = mapping[original_label]
        source_folder = os.path.join(source_usage_path, original_label)
        target_folder = os.path.join(target_base, usage, target_label)
        os.makedirs(target_folder, exist_ok=True)

        for file in os.listdir(source_folder):
            src_file = os.path.join(source_folder, file)
            dst_file = os.path.join(target_folder, file)
            shutil.copyfile(src_file, dst_file)

print("Veri başarıyla yeniden organize edildi.")
