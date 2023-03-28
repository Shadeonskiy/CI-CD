import pytest
from main import clean_text


@pytest.mark.parametrize("text, expected_result", [(["Hi\n"], ["Hi"]),
                                                   (["Hello"], ["Hello"]),
                                                   (["Hi\n", "How are you?\n"],
                                                    ["Hi", "How are you?"])])
def test_text_cleaner(text, expected_result):
    assert clean_text(text) == expected_result
