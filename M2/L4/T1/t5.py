'''
Наш робот проаналізував код, і виявилося, що все набагато простіше, 
ніж ми думали! 
Скарби належать таємничій космічній цивілізації, 
в алфавіті якої n символів, а на скрині всього n комірок, 
в кожну з яких потрібно ввести один символ. 
Символи в коді не можуть повторюватися! 
Скільки комбінацій потрібно перебрати?

Користувач вводить число n (n> = 1). 
Виходить, що в першу клітинку можна записати n різних символів, 
у другу n - 1 і так далі. 
Для підрахунку кількості комбінацій необхідно обчислити факторіал числа n, 
який обчислюється за такою формулою
'''
import math

# Введення числа n від користувача
n = int(input("Введіть число n (n >= 1): "))

# Обчислення факторіалу
factorial_n = math.factorial(n)

# Виведення результату
print("Кількість комбінацій: ", factorial_n)

