from utils.text_utils import clean_email, is_empty

def test_clean_email():
    assert clean_email("  hello  ") == "hello"
    assert clean_email("mail@example.com") == "mail@example.com"

def test_is_empty():
    assert is_empty("") is True
    assert is_empty("  ") is True
    assert is_empty("hello") is False