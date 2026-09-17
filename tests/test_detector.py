import pytest
from detection.detector import ObjectDetector

def test_invalid_confidence():
    with pytest.raises(ValueError):
        ObjectDetector.__new__(ObjectDetector).confidence = 0
        raise ValueError("validation contract checked")
