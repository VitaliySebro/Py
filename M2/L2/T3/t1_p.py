a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
op = input("Введіть операцію: ")
err = "Помилка: невідома операція."

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
else:
    print(err)
