import pytest
from app import (
    handle_post, 
    screen_raw_note_against_classifier, 
    filter_suspicious_phrases, 
    extract_plain_text_from_sections, 
    strip_formatting_symbols, 
    check_word_count_against_threshold, 
    post_request_and_extract_data, 
    clean_note_content
)
from test_data import (
    strip_formatting_cases,
    extract_plain_text_cases
)

@pytest.mark.parametrize("input_text, expected_text", strip_formatting_cases)
def test_strip_formatting_symbols(input_text, expected_text):
    assert strip_formatting_symbols(input_text) == expected_text

@pytest.mark.parametrize("input_dict, expected_text", extract_plain_text_cases)
def test_extract_plain_text_from_sections(input_dict, expected_text):
    assert extract_plain_text_from_sections(input_dict) == expected_text 

def test_extract_plain_text_missing_key():
    with pytest.raises(KeyError):
        assert extract_plain_text_from_sections({"sections": [{"header": "Heading Only"}, {"content": ""}]})