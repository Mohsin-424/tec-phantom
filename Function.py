# def greet():
#     print("Hello World")
# greet()
# print(" Outside Function ")


# def namer(name):
#     return "Hello" +  name
# print(namer("          Mohsin"))
# print(namer("Hello World"))


# def sum(a, b):
#     c = a + b
#     print(c)
# sum(23,32)

# def sum_sub(a, b):
#     return a + b, a - b
# print(sum_sub(23,32))


# def diff(a , b):
#     c = a - b
#     return c
# print(diff(43,54))




# def square(alpha):
#     c  = alpha * alpha
#     return c
# bravo = square(8)
# print(bravo)


# Built in Functions
# import math

# # sqrt computes the square root
# square_root = math.sqrt(4)

# print("Square Root of 4 is",square_root)

# # pow() computes the power
# power = pow(2, 3)

# print("2 to the power 3 is",power)




# *kwargs 

# def add_all(*numbers):
#     return sum(numbers)
# print(add_all(1,2,3,4,5,6,7,8,9,10))

# def add_all(*numbers):
#     return sum(numbers)
# print(add_all(1,2,3,4,5,6,7,8,9,10))




# def greet(**words):

#     for key, value in words.items():
#         # print(key, value)
#         return key , value
# print(greet( name = "Hello" , value = "Mohsin"))




# def is_prime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
    
#     for i in range(3, int(n ** 0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True

# print(is_prime(7))



# def prime(n):
#     if n>=1 and  n %2 == 0:
#         return True
#     else:
#         return False
    
#     for i in range(3, int(n**0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True

# print(f'Prime Number: {prime(-2)}')


    

    

# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# # Taking input from the user
# num = int(input("Enter a number: "))

# # Checking if the number is prime or not
# if is_prime(num):
#     print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")




# # map and filter
# def get_even_squares(numbers):
#     """
#     This function returns a list of squares of even numbers from the given list using map() and filter().
#     """
#     even_numbers = filter(lambda x: x % 2 == 0, numbers)
#     return list(map(lambda x: x**2, even_numbers))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_squares = get_even_squares(numbers)
# print(even_squares)  # Output: [4, 16, 36, 64, 100]




try:
    # Code that may raise an exception
    x = 1 / 0
except ZeroDivisionError:
    # Code to handle the exception
    print("Error: Division by zero is not allowed.")
finally:
    # Code that will always be executed, regardless of whether an exception occurred or not
    print("This code will always be executed.")

