a = int(input("Множник 1: "))
b = int(input("Множник 2: "))
answer = 0

# Множення a на b за допомогою циклу while
while a > 0:
    answer += b
    a -= 1

print(answer)
