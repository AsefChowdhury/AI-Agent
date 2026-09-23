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
    strip_formatting_cases
)

@pytest.mark.parametrize("input_text, expected_text", strip_formatting_cases)
def test_strip_formatting_symbols(input_text, expected_text):
    assert strip_formatting_symbols(input_text) == expected_text