import pytest
from main import read_from_files


@pytest.mark.parametrize("expected_file1, expected_file2",
                         [(["Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                           "Fusce eu commodo arcu. Phasellus imperdiet convallis turpis."],
                          ["Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                           "Phasellus imperdiet convallis turpis.",
                           "Fusce eu commodo arcu."])])
def test_file_reading(prepare_text_files, expected_file1, expected_file2):
    f1_info, f2_info = read_from_files(*prepare_text_files)
    assert f1_info == expected_file1
    assert f2_info == expected_file2
