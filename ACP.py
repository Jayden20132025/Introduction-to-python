# Program to check whether a number is even or odd

# Ask the user for a number
number = int(input("Enter a number: "))

# Check if even or odd using modulus operator
if number % 2 == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")

print("Best of luck!")
