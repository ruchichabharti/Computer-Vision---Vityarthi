import argparse
from pathlib import Path

from config.config import DEFAULT_MODEL, DEFAULT_CONFIDENCE, DEFAULT_OUTPUT_DIR
from detection.detector import ObjectDetector
from tracking.tracker import VideoTracker
from counting.counter import ObjectCounter
from analytics.analytics import save_detection_summary
from utils.file_utils import validate_input, ensure_dir


def parse_args():
    parser = argparse.ArgumentParser(
        description="SmartVision: object detection, tracking and counting."
    )
    parser.add_argument("--mode", choices=["image", "video", "count"], required=True)
    parser.add_argument("--input", required=True, help="Path to image or video.")
    parser.add_argument("--output", default=None, help="Output file path.")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--confidence", type=float, default=DEFAULT_CONFIDENCE)
    return parser.parse_args()


def main():
    args = parse_args()
    source = validate_input(args.input)
    output_dir = ensure_dir(DEFAULT_OUTPUT_DIR)

    detector = ObjectDetector(args.model, args.confidence)

    if args.mode == "image":
        output = Path(args.output) if args.output else output_dir / "detected_image.jpg"
        result = detector.detect_image(source, output)
        save_detection_summary(result["counts"], output_dir / "image_summary.csv")
        print(f"Saved annotated image: {output}")
        print(f"Detected objects: {result['counts']}")

    elif args.mode == "video":
        output = Path(args.output) if args.output else output_dir / "tracked_video.mp4"
        tracker = VideoTracker(detector)
        summary = tracker.process(source, output)
        save_detection_summary(summary, output_dir / "video_summary.csv")
        print(f"Saved processed video: {output}")
        print(f"Observed object counts: {summary}")

    else:
        output = Path(args.output) if args.output else output_dir / "counted_video.mp4"
        counter = ObjectCounter(detector)
        summary = counter.process(source, output)
        save_detection_summary(summary, output_dir / "count_summary.csv")
        print(f"Saved counted video: {output}")
        print(f"Frame-level detection totals: {summary}")


if __name__ == "__main__":
    main()
