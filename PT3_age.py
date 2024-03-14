a = input("Enter your name:")

b = int(input("Enter your age:"))

if b <= 10:
    print(f"Long way to go dear {a}")
elif b <= 30:
    print(f"Your are a family man Mr.{a}")
elif b <= 50:
    print(f"Enjoy your peak time in your life Mr.{a}")
else:
    print(f"Prepare for your retirement life")