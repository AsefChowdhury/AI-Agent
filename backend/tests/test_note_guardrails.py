import pytest, json
from unittest.mock import ANY
from app import (
    handle_post, 
    screen_raw_note_against_classifier,
    build_flexible_pattern,
    filter_suspicious_phrases, 
    extract_plain_text_from_sections, 
    strip_formatting_symbols, 
    check_header_against_content,
    check_word_count_against_threshold, 
    post_request_and_extract_data, 
    clean_note_content
)
from test_data import (
    strip_formatting_cases,
    extract_plain_text_cases,
    check_word_count_cases,
    build_flexible_pattern_cases,
    filter_suspicious_phrases_english_cases,
    filter_suspicious_phrases_technical_cases,
    check_header_against_content_cases,
    screen_raw_note_cases,
    post_request_and_extract_cases,
    post_request_malformed_json_cases,
    post_request_missing_message_key_cases

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

@pytest.mark.parametrize("input_text, input_dict, expected_text", check_word_count_cases)
def test_check_word_count_against_threshold(input_text, input_dict, expected_text):
    assert check_word_count_against_threshold(input_text, input_dict) == expected_text

@pytest.mark.parametrize("input_phrase, expected_phrase", build_flexible_pattern_cases)
def test_build_flexible_pattern(input_phrase, expected_phrase):
    assert build_flexible_pattern(input_phrase) == expected_phrase

@pytest.mark.parametrize("unfiltered_note, filtered_note", filter_suspicious_phrases_english_cases)
def test_filter_suspicious_phrases_english(unfiltered_note, filtered_note):
    assert filter_suspicious_phrases(unfiltered_note) == filtered_note

@pytest.mark.parametrize("unfiltered_note, filtered_note", filter_suspicious_phrases_technical_cases)
def test_filter_suspicious_phrases_technical(unfiltered_note, filtered_note):
    assert filter_suspicious_phrases(unfiltered_note) == filtered_note

@pytest.mark.parametrize("input_dict, expected_result", check_header_against_content_cases)
def test_check_header_against_content(input_dict, expected_result ):
    assert check_header_against_content(input_dict) == expected_result

@pytest.mark.parametrize("input_text, mocked_response, expected_output", screen_raw_note_cases)
def test_screen_raw_note_against_classifier(mocker, input_text, mocked_response, expected_output):
    mock_post = mocker.patch("app.requests.post")

    mock_post.return_value.json.return_value = {"message": {"content": mocked_response}}
    result = screen_raw_note_against_classifier(input_text)

    assert result == expected_output
    mock_post.assert_called_once_with("http://localhost:11434/api/chat", json=ANY)

@pytest.mark.parametrize("mocked_response, expected_extracted_data", post_request_and_extract_cases)
def test_post_request_and_extract_data(mocker, mocked_response, expected_extracted_data):
    payload = {}
    mock_post = mocker.patch("app.requests.post")
    mock_post.return_value.json.return_value = mocked_response

    result = post_request_and_extract_data(payload)
    assert result == expected_extracted_data

@pytest.mark.parametrize("mocked_response", post_request_malformed_json_cases)
def test_post_request_and_extract_data_malformed_json(mocker, mocked_response):
    payload = {}
    mock_post = mocker.patch("app.requests.post")
    mock_post.return_value.json.return_value = mocked_response

    with pytest.raises(json.decoder.JSONDecodeError):
        post_request_and_extract_data(payload)

@pytest.mark.parametrize("mocked_response", post_request_missing_message_key_cases)
def test_post_request_and_extract_data_missing_message_key(mocker, mocked_response):
    payload = {}
    mock_post = mocker.patch("app.requests.post")
    mock_post.return_value.json.return_value = mocked_response

    with pytest.raises(KeyError):
        post_request_and_extract_data(payload)