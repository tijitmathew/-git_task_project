name = input("Enter your name:") # Requesting user to input name 

age = int(input("Enter your age:")) # Requesting user to input age

if age <= 10: # Printing reponse using if elif for each age category.
    print(f"Long way to go dear {name}") # Respose for age below or equal 10

elif age <= 30:
    print(f"Your are a family man Mr.{name}") # Respose for age below or equal 30

elif age <= 50:
    print(f"Enjoy your peak time in your life Mr.{name}") # Respose for age below or equal 50

else:
    print("Prepare for your retirement life") # Respose for age above 50