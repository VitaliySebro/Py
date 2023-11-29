'''
Змініть минулу програму так, щоб вона тривала до тих пір, 
поки не буде дана правильна відповідь. 
Для цього умова має бути не в умовному операторі, а в циклі while.
'''
def riddle_game():
    # Загадка
    riddle = "Що може бути світліше за день і темніше за ніч?"

    # Відповідь на загадку
    answer = "фургон"

    # Початок циклу while
    while True:
        # Запитання користувачеві
        user_response = input(riddle + "\nТвоя відповідь: ")

        # Перевірка відповіді та виведення результату
        if user_response.lower() == answer:
            print("Вірно! Вітаємо!")
            break  # Завершення циклу при правильній відповіді
        else:
            print("Спробуйте ще раз. Це було неправильно.")

# Виклик функції для гри в загадки
riddle_game()