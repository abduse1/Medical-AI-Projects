# Check if a number is odd or even
a = int(input("Enter a number: "))

if a % 2 == 0:
    print("The number you entered is even")
else:
    print("The number you entered is odd")

# Print numbers from 1 to 10
print("Numbers from 1 to 10:")
for num1 in range(1, 11):
    print(num1)

# Print numbers from 10 to 1
print("Numbers from 10 to 1:")
num = 10
while num > 0:
    print(num)
    num -= 1