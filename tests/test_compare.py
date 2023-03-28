import pytest
from main import compare_files, read_from_files


def test_compare_files(prepare_text_files):
    expected = ({"Lorem ipsum dolor sit amet, consectetur adipiscing elit."},
                {"Fusce eu commodo arcu. Phasellus imperdiet convallis turpis.",
                 "Phasellus imperdiet convallis turpis.",
                 "Fusce eu commodo arcu."})
    f1_info, f2_info = read_from_files(*prepare_text_files)
    assert compare_files(f1_info, f2_info) == expected
