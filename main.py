def greet(name: str) -> str:
    """
    Функция возвращает приветственное сообщение для заданного имени.
    """
    return f"Привет, {name}!"

if __name__ == "__main__":
    user_name = input("Введите ваше имя: ")
    print(greet(user_name))
