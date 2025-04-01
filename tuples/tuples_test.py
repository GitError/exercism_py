import pytest
from tuples import get_coordinate, convert_coordinate, compare_records, create_record, clean_up

def test_get_coordinate():
    record = ("Scrimshawed Whale Tooth", "2A")
    assert get_coordinate(record) == "2A"

def test_convert_coordinate():
    coordinate = "2A"
    assert convert_coordinate(coordinate) == ("2", "A")

def test_compare_records_matching():
    azara_record = ("Scrimshawed Whale Tooth", "2A")
    rui_record = ("Deserted Docks", ("2", "A"), "Blue")
    assert compare_records(azara_record, rui_record) is True

def test_compare_records_not_matching():
    azara_record = ("Scrimshawed Whale Tooth", "2A")
    rui_record = ("Deserted Docks", ("3", "B"), "Blue")
    assert compare_records(azara_record, rui_record) is False

def test_create_record_matching():
    azara_record = ("Scrimshawed Whale Tooth", "2A")
    rui_record = ("Deserted Docks", ("2", "A"), "Blue")
    expected = ("Scrimshawed Whale Tooth", "2A", "Deserted Docks", ("2", "A"), "Blue")
    assert create_record(azara_record, rui_record) == expected

def test_create_record_not_matching():
    azara_record = ("Scrimshawed Whale Tooth", "2A")
    rui_record = ("Deserted Docks", ("3", "B"), "Blue")
    assert create_record(azara_record, rui_record) == "not a match"

def test_clean_up():
    combined_record_group = (
        ("Scrimshawed Whale Tooth", "2A", "Deserted Docks", ("2", "A"), "Blue"),
        ("Brass Spyglass", "4B", "Abandoned Lighthouse", ("4", "B"), "Blue"),
    )
    expected = (
        "('Scrimshawed Whale Tooth', 'Deserted Docks', ('2', 'A'), 'Blue')\n"
        "('Brass Spyglass', 'Abandoned Lighthouse', ('4', 'B'), 'Blue')\n"
    )
    assert clean_up(combined_record_group) == expected