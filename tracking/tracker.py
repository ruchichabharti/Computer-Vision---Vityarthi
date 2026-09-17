from collections import Counter
from pathlib import Path
import cv2


class VideoTracker:
    """Video tracking using Ultralytics' built-in tracking pipeline."""

    def __init__(self, detector):
        self.detector = detector

    def process(self, source, output):
        cap = cv2.VideoCapture(str(source))
        if not cap.isOpened():
            raise ValueError(f"Unable to open video: {source}")

        fps = cap.get(cv2.CAP_PROP_FPS) or 25.0
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        Path(output).parent.mkdir(parents=True, exist_ok=True)
        writer = cv2.VideoWriter(
            str(output), cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height)
        )

        totals = Counter()
        while True:
            ok, frame = cap.read()
            if not ok:
                break
            result = self.detector.model.track(
                frame, conf=self.detector.confidence, persist=True, verbose=False
            )[0]
            writer.write(result.plot())
            if result.boxes is not None:
                for cls_id in result.boxes.cls.tolist():
                    totals[result.names[int(cls_id)]] += 1

        cap.release()
        writer.release()
        return dict(totals)
