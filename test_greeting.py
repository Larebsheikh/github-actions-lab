from greeting import generate_greeting

def test_greeting_name():
    assert generate_greeting("Lareb") == "Hello, Lareb!"

def test_greeting_empty():
    assert generate_greeting("") == "Hello, Guest!"
