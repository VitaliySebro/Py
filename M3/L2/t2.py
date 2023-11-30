'''
Напишіть функцію
Програма просить ввести число n і друкує всі числа від n до 1 включно
'''
def print_numbers_reverse(n):
    while n >= 1:
        print(n)
        n -= 1

# Запитати користувача про число n
user_input = input("Введіть число n: ")

# Перевірити, чи введено число
if user_input.isdigit():
    n = int(user_input)
    print_numbers_reverse(n)
else:
    print("Будь ласка, введіть коректне ціле число.")
