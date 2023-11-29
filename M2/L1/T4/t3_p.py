s1 = input("Do you speak English?")
if s1 == "yes":
    print("Hello!")
    s2 = input("Do you play football?")
    if s2 == "yes":
        print("Great! I love football! ")
    else:
        s3 = input("What do you like? ")
        print(s3 + "? That's good!")
else:
    s2 = input("Привіт! Ви розмовляєте українською")
    if s2 == "Так":
        s3 = input("Як сьогодні погода?")
        print(s3 + "? Я теж так думаю...")
    else:
        print( "sorry! " )