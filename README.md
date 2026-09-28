# Face Crop Assignment

This script detects frontal faces in `input/test.jpg`, crops each face with a small border, and saves the results in `output/`.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Replace `input/test.jpg` with the image you want to process. Then run:

```powershell
python app.py
```

Cropped faces are written as `output/face_1.jpg`, `output/face_2.jpg`, and so on. Existing output files are overwritten when they have the same names.
