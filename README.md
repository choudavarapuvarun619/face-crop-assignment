# Face Cropping Assignment

## Overview

This project detects faces in input images and automatically crops the detected face into a standard 256 × 256 image.

The project uses **Face Crop Plus** for face detection, facial landmark detection, alignment, and cropping.

Image enhancement and sharpening are intentionally disabled because they are not required for this assignment.

## Features

- Processes multiple images from an input folder
- Automatically detects faces
- Selects the largest face in each image
- Aligns the detected face using facial landmarks
- Crops the face from the original image
- Produces a standard 256 × 256 output
- Does not perform sharpening or image enhancement
- Saves processed images in a separate output folder

## Project Structure

```text
face-crop-assignment/
│
├── app.py
├── requirements.txt
├── README.md
│
├── input/
│   ├── image001.jpg
│   ├── image002.jpg
│   └── ...
│
└── output/
    ├── face_1.jpg
    ├── face_2.jpg
    └── ...
```

## Requirements

- Python 3.10 or later
- Internet connection for initial installation and model download

## Installation

### 1. Create a virtual environment

```bash
python -m venv venv
```

### 2. Activate the virtual environment

For Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

Place the images that need to be processed inside the `input` folder.

Example:

```text
input/
├── person1.jpg
├── person2.jpg
├── person3.jpg
└── person4.jpg
```

Run the application:

```bash
python app.py
```

The cropped faces will be saved automatically in the `output` folder.

## Processing Pipeline

```text
Input Images
     │
     ▼
Face Detection
     │
     ▼
Facial Landmark Detection
     │
     ▼
Face Alignment
     │
     ▼
Largest Face Selection
     │
     ▼
Face Cropping
     │
     ▼
256 × 256 Output
```

## Configuration

### Face Selection

```python
strategy="largest"
```

When an image contains multiple faces, the largest detected face is selected.

### Output Size

```python
output_size=256
```

The cropped face is generated at 256 × 256 pixels.

### Face Factor

```python
face_factor=0.85
```

Controls how much of the output image is occupied by the detected face.

### Enhancement

```python
enh_threshold=None
```

Image enhancement is disabled.

The project therefore performs face detection, alignment, and cropping without applying sharpening or super-resolution.

## Input

The application accepts:

- JPG
- JPEG
- PNG

Multiple images can be placed in the `input` directory and processed in a single run.

## Output

The processed images are saved in the `output` folder.

Each detected face is saved as a cropped image.

## Example

The input can contain normal photographs, full-body photographs, or images containing multiple people.

The application detects the face within the image and produces a focused face crop.

### Input

A normal photograph containing a person, background, and face.

### Output

A cropped image containing the detected face at 256 × 256 pixels.

## Limitations

- The current configuration selects only the largest face from each image.
- Faces that are extremely small, heavily occluded, or poorly visible may not be detected.
- The project performs face detection and cropping only; it does not perform face recognition.
- Image enhancement and sharpening are intentionally disabled.

## Technologies Used

- Python
- Face Crop Plus
- RetinaFace-based face detection and landmark detection
- Pillow
- NumPy

## How It Works

The application reads all supported images from the `input` folder and passes them to the face cropping pipeline.

For each image, the system detects the available faces, selects the largest face, aligns it using facial landmarks, and generates a standardized 256 × 256 crop.

The resulting images are saved in the `output` folder.

## Author

Face Cropping Assignment
