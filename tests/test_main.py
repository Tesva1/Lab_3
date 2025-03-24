import main

def test_greet():
    result = main.greet("Мир")
    expected = "Привет, Мир!"
    assert result == expected, f"Ожидалось: {expected}, получено: {result}"
