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




def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

print(is_prime(7))



def prime(n):
    if n>=1 and  n %2 == 0:
        return True
    else:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

print(f'Prime Number: {prime(-2)}')


    

    
