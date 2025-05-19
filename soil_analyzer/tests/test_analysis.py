"""Tests for soil_analyzer.analysis using pytest."""

from soil_analyzer.analysis import classify_ph


def test_classify_ph():
    assert classify_ph(5.0) == "acidic"
    assert classify_ph(6.5) == "optimal"
    assert classify_ph(7.5) == "alkaline"

