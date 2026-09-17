from pathlib import Path
from collections import Counter
import cv2
from ultralytics import YOLO
from detection.preprocessing import read_image


class ObjectDetector:
    """YOLO-based object detector used by all processing modes."""

    def __init__(self, model_path="yolo11n.pt", confidence=0.35):
        if not 0.0 < confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1")
        self.model = YOLO(model_path)
        self.confidence = confidence

    def predict(self, frame):
        return self.model.predict(frame, conf=self.confidence, verbose=False)[0]

    def annotate(self, frame):
        result = self.predict(frame)
        annotated = result.plot()
        counts = Counter()
        if result.boxes is not None:
            for cls_id in result.boxes.cls.tolist():
                name = result.names[int(cls_id)]
                counts[name] += 1
        return annotated, dict(counts)

    def detect_image(self, source, output):
        image = read_image(source)
        annotated, counts = self.annotate(image)
        Path(output).parent.mkdir(parents=True, exist_ok=True)
        if not cv2.imwrite(str(output), annotated):
            raise IOError(f"Could not write output image: {output}")
        return {"counts": counts}
