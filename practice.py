# print("Hello, World!")
# print("This is a test.")

# name = input("Please enter your name: ")
# print("Hello, " + name + "!")  # Concatenating strings

# a = 10
# b = 5

# Arithmetic operations
# sum = a + b
# diff = a - b
# product = a * b
# quotient = a / b
# modulus = a % b
# exponent = a ** b
# floor_division = a // b

# print("Sum: ", sum)
# print("Difference: ", diff)
# print("Product: ", product)
# print("Quotient: ", quotient)
# print("Modulus: ", modulus)
# print("Exponent: ", exponent)
# print("Floor Division: ", floor_division)

# Comparison operations
# is_equal = a == b
# is_not_equal = a != b
# is_greater = a > b
# is_less = a < b
# is_greater_equal = a >= b
# is_less_equal = a <= b
# print("Is Equal: ", is_equal)
# print("Is Not Equal: ", is_not_equal)
# print("Is Greater: ", is_greater)
# print("Is Less: ", is_less)
# print("Is Greater or Equal: ", is_greater_equal)
# print("Is Less or Equal: ", is_less_equal)

# Logical operations
# is_true = True
# print("Is True: ", is_true)
# print("Is False: ", not is_true)
# print("Is True and False: ", is_true and False)
# print("Is True or False: ", is_true or False)
# print("Is True XOR False: ", is_true ^ False)
# print("Is True and False: ", is_true and False)
# print("Is True or False: ", is_true or False)
# print("Is True XOR False: ", is_true ^ False)
# print("Is True and False: ", is_true and False)
# print("Is True or False: ", is_true or False)


# Conditional statements
#even and odd numbers

# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")

# Fibbonacci series
# n = int(input("Enter a number: "))
# fib = [0, 1]
# for i in range(2, n):
#     fib.append(fib[i-1] + fib[i-2])
# print(f"The Fibonacci series up to {n} is: {fib}")

# Factorial of a number
# num = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print(f"The factorial of {num} is: {factorial}")

# Prime number check
# num = int(input("Enter a number: "))
# is_prime = True
# for i in range(2, num):
#     if num % i == 0:
#         is_prime = False
#         break
# if is_prime:
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")

# Table of a number
# num = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")

#Palindrome check
# num = int(input("Enter a number: "))
# original_num = num
# reversed_num = 0
# while num != 0:
#     digit = num % 10
#     reversed_num = reversed_num * 10 + digit
#     num //= 10
# if original_num == reversed_num:
#     print(f"{original_num} is a palindrome")
# else:
#     print(f"{original_num} is not a palindrome")

#Function to convert celsius to fahrenheit
# def celsius_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit
# celsius = float(input("Enter temperature in Celsius: "))
# fahrenheit = celsius_to_fahrenheit(celsius)
# print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit")

# def c_to_f(celcius):
#     return (celcius * 9/5) + 32

# temp_c = input("Enter temperature in Celsius: ")
# print("Temperature in Fahrenheit: ", c_to_f(float(temp_c)))

#Function to convert fahrenheit to celsius
# def fahrenheit_to_celsius(fahrenheit):
#     celsius = (fahrenheit - 32) * 5/9
#     return celsius
# fahrenheit = float(input("Enter temperature in Fahrenheit: "))
# celsius = fahrenheit_to_celsius(fahrenheit)
# print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius")

