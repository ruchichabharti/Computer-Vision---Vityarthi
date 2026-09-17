import csv
from pathlib import Path


def save_detection_summary(counts, output_file):
    Path(output_file).parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["class", "count"])
        for name, count in sorted(counts.items()):
            writer.writerow([name, count])


def load_summary(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))
