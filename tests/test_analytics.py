from analytics.analytics import save_detection_summary, load_summary

def test_summary_round_trip(tmp_path):
    path = tmp_path / "summary.csv"
    save_detection_summary({"person": 3, "car": 2}, path)
    rows = load_summary(path)
    assert rows == [{"class": "car", "count": "2"}, {"class": "person", "count": "3"}]
