def greet(name: str) -> str:
    return f"Привет, {name}!"

def farewell(name: str) -> str:
    return f"До свидания, {name}!"

def main():
    user_name = input("Введите ваше имя: ")
    action = input("Выберите действие (1 - Приветствие, 2 - Прощание): ")
    if action == "1":
        print(greet(user_name))
    elif action == "2":
        print(farewell(user_name))
    else:
        print("Неверный выбор!")

if __name__ == '__main__':
    import os
    # Если переменная CI установлена, не запускать интерактивное приложение (опционально)
    if os.environ.get("CI") != "true":
        main()
