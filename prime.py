def is_prime(num):
    # Handle cases for numbers less than 2
    if num <= 1:
        return False
    # Check divisibility from 2 up to the square root of num
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Take user input
number = int(input("Enter a number: "))

# Check if the number is prime
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
