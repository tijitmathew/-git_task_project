name = input("Enter your name:")

age = int(input("Enter your age:"))

if age <= 10:
    print(f"Long way to go dear {name}")
elif age <= 30:
    print(f"Your are a family man Mr.{name}")
elif age <= 50:
    print(f"Enjoy your peak time in your life Mr.{name}")
else:
    print("Prepare for your retirement life")