import json
from pathlib import Path


REPORT_PATH = Path("/app/report.json")
EXPECTED_KEYS = {"total_requests", "unique_ips", "top_path"}
EXPECTED_REPORT = {
    "total_requests": 6,
    "unique_ips": 3,
    "top_path": "/index.html",
}


def _load_report():
    with REPORT_PATH.open(encoding="utf-8") as report_file:
        return json.load(report_file)


def test_criterion_1_report_exists_and_is_json_object():
    """Success criterion 1: /app/report.json exists and contains a single JSON object."""
    assert REPORT_PATH.exists(), "report.json was not created"
    report = _load_report()
    assert isinstance(report, dict), "report.json must contain a JSON object"


def test_criterion_2_report_has_exact_keys():
    """Success criterion 2: the JSON object has exactly the required keys."""
    report = _load_report()
    assert set(report) == EXPECTED_KEYS


def test_criterion_3_report_values_match_access_log():
    """Success criterion 3: the JSON values summarize /app/access.log exactly."""
    report = _load_report()
    for key, expected_value in EXPECTED_REPORT.items():
        assert report.get(key) == expected_value
