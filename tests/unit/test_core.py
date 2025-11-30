import textutils.core as c 

def test_word_count_basic():
    text = "Hello world I am testing the word count function"
    assert c.word_count(text) == 9