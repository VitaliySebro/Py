'''
Потрібно порахувати добуток чисел від a до b. 
Програма запитує числа і виводить результат.
Програма запитує у людини спочатку перше число, потім друге. 
Після цього програма повинна перемножити всі числа від a до b 
(припускаючи, що a < b) і надрукувати результат. 
Приклад: Введено числа 5 і 7. 
Програма надрукує "210" (5 * 6 * 7 = 210).
'''
def calculate_product(a, b):
    product = 1
    for i in range(a, b + 1):
        product *= i
    return product

# Запитати користувача про перше число (a)
a = int(input("Введіть перше число (a): "))

# Запитати користувача про друге число (b), яке повинно бути більшим за a
b = int(input("Введіть друге число (b), більше за перше: "))

# Перевірити, чи b більше за a
if b > a:
    result = calculate_product(a, b)
    print(f"Добуток чисел від {a} до {b}: {result}")
else:
    print("Будь ласка, введіть друге число, більше за перше.")

