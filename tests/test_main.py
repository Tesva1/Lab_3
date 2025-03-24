import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import main

# Вывод отладочной информации
print("Текущая рабочая директория:", os.getcwd())
print("sys.path:", sys.path)

def test_greet():
    result = main.greet("Мир")
    expected = "Привет, Мир!"
    assert result == expected, f"Ожидалось: {expected}, получено: {result}"

def test_farewell():
    result = main.farewell("Мир")
    expected = "До свидания, Мир!"
    assert result == expected, f"Ожидалось: {expected}, получено: {result}"
