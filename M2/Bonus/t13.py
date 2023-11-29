'''
Найбільшим спільним дільником двох натуральних чисел, n і m, 
є найбільше число, d, яке ділиться рівномірно як на n, так і на m. 
Існує кілька алгоритмів, які можуть бути використані для вирішення 
цього завдання.
    Напишіть програму, яка зчитує два додатніх цілих числа від користувача 
і використовує алгоритм для визначення і повідомлення їх найбільшого 
спільного дільника



'''
# Функція для знаходження найбільшого спільного дільника (НСД)
def find_gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

# Зчитування двох додатних цілих чисел від користувача
num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))

# Знаходження та виведення найбільшого спільного дільника
gcd = find_gcd(num1, num2)
print(f"Найбільший спільний дільник {num1} і {num2} є {gcd}.")