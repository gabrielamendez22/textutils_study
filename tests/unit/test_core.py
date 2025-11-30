import textutils.core as c 

def test_word_count_basic():
    text = "Hello world hello WORLD WORLD HELLO"
    assert c.word_count(text) == {'hello': 3, 'world': 3}