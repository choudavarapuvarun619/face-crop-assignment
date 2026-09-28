from sklearn.datasets import fetch_lfw_people
from PIL import Image
from pathlib import Path
import numpy as np

OUTPUT_DIR = Path("input")
OUTPUT_DIR.mkdir(exist_ok=True)

print("Downloading LFW dataset...")

lfw = fetch_lfw_people(
    color=True,
    resize=None,
    min_faces_per_person=20
)

print(f"Dataset contains {len(lfw.images)} images.")

num_images = 100

for i, image in enumerate(lfw.images[:num_images]):
    image = np.clip(image, 0, 255).astype(np.uint8)

    Image.fromarray(image).save(
        OUTPUT_DIR / f"lfw_{i + 1:03d}.jpg"
    )

print(f"{num_images} images saved to input/")