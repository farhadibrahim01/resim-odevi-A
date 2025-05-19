import os
import pandas as pd
import numpy as np
from PIL import Image

csv_file = r"C:\Resim-A\data\fer2013.csv"
output_dir = r"C:\Resim-A\data\fer2013_images"

emotion_labels = {
    0: "angry",
    1: "disgust",
    2: "fear",
    3: "happy",
    4: "sad",
    5: "surprise",
    6: "neutral"
}

os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv(csv_file)

for index, row in df.iterrows():
    emotion = emotion_labels[int(row['emotion'])]
    pixels = np.fromstring(row['pixels'], dtype=int, sep=' ')
    image = pixels.reshape(48, 48).astype(np.uint8)
    image = Image.fromarray(image)

    usage = row['Usage'].lower()
    if 'train' in usage:
        usage_folder = "train"
    elif 'public' in usage:
        usage_folder = "val"
    else:
        usage_folder = "test"

    save_path = os.path.join(output_dir, usage_folder, emotion)
    os.makedirs(save_path, exist_ok=True)

    img_filename = f"{index}.png"
    image.save(os.path.join(save_path, img_filename))
