from pathlib import Path
from face_crop_plus import Cropper


INPUT_DIR = Path("input")
OUTPUT_DIR = Path("output")


def crop_faces():
    OUTPUT_DIR.mkdir(exist_ok=True)

    image_files = [
        file for file in INPUT_DIR.iterdir()
        if file.suffix.lower() in [".jpg", ".jpeg", ".png"]
    ]

    if not image_files:
        print("No images found in input folder.")
        return

    print(f"Found {len(image_files)} images.")

    cropper = Cropper(
        output_size=256,
        face_factor=0.85,
        strategy="largest",
        enh_threshold=None
    )

    cropper.process_dir(
        input_dir=str(INPUT_DIR),
        output_dir=str(OUTPUT_DIR)
    )

    print()
    print("Face cropping completed.")
    print(f"Images found: {len(image_files)}")
    print(f"Output folder: {OUTPUT_DIR.absolute()}")


if __name__ == "__main__":
    crop_faces()