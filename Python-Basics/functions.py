# Function to check if a number is even
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Test the function
result = is_even(14)
if result:
    print("14 is even")
else:
    print("14 is odd")

# Function to calculate factorial
def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

# Test the function
print(factorial(4))  # Output: 24

# Function to print patient details
def print_patient_detail(name, age, height, weight, is_tb_positive):
    print(f"The patient name is {name}, he is {age} years old, his height is {height}m, his weight is {weight}kg, and Is he a TB carrier: {is_tb_positive}")

# Test the function
print_patient_detail("Abebe", 24, 1.73, 45, True)