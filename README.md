# SmartVision — Object Detection, Tracking & Counting

SmartVision is a command-line Computer Vision project that uses YOLO and OpenCV to detect objects in images, track objects in videos, count detections, and export summary data.

## Features
- Image object detection
- Video object tracking
- Video object counting
- CSV result summaries
- Input validation
- Automated tests
- Command-line execution

## Technology
- Python 3.10+
- Ultralytics YOLO
- OpenCV
- NumPy
- Pytest

## Project Structure
See the folders `detection`, `tracking`, `counting`, `analytics`, `utils`, `config`, and `tests`.

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/SmartVision.git
cd SmartVision
```

### 2. Create a virtual environment
Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

On first execution, Ultralytics may download the configured YOLO model weights. Internet access is required for that first model download unless the weights are already available locally.

## Running

Image detection:
```bash
python main.py --mode image --input input/sample.png
```

Video tracking:
```bash
python main.py --mode video --input input/sample.mp4
```

Object counting:
```bash
python main.py --mode count --input input/sample.mp4
```

Custom confidence:
```bash
python main.py --mode image --input input/sample.jpg --confidence 0.50
```

Custom output:
```bash
python main.py --mode image --input input/sample.jpg --output output/my_result.jpg
```

## Testing
Run:
```bash
pytest -q
```

## Outputs
Generated files are placed in `output/` by default:
- annotated image
- processed video
- CSV detection summary

## View the result image
After running image detection, use:
```bash
start output\final_result.png
```

## Notes for Evaluation
The project is designed for terminal execution. No GUI setup is required. The sample input is generated separately because binary media files are not embedded in the source code.

## Academic Integrity
This repository is intended as a student project template. Review, understand, test, and modify the implementation before submission so the final work accurately represents your own work.
