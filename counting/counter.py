from collections import Counter
from pathlib import Path
import cv2


class ObjectCounter:
    """Counts detected objects across video frames."""

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
            annotated, counts = self.detector.annotate(frame)
            totals.update(counts)
            cv2.putText(
                annotated, f"Objects: {sum(counts.values())}",
                (20, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2
            )
            writer.write(annotated)

        cap.release()
        writer.release()
        return dict(totals)
