# Write a Python script that calculates the sum of all integers from 1 to n (inclusive), where n is a user-input integer.
#  Use a for loop to achieve this.

# num = int(input("Enter Any Number"))
# sum = 0
# for i in range(0, num):
#     sum = sum + i
#     print(sum)



# num1 = int(input("Number 1:                  "))
# # print(num1)
# sum = 0
# for i in range( 0 , num1):
#     sum = sum + i
#     print(sum)


# Given a list of integers, write a Python script that uses a 
# for loop to print all the even numbers in the list.

# numbers = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in numbers:
#     if num%2 == 0:
#         print(num)
#     else:
#         print("Not Even Number")



# Write a Python script to calculate the factorial of a number n (where n is a
#  positive integer provided by the user) using a while loop.


# fact = int(input("Enter Any number for factorial:  ............"))
# result = 1
# for i in range(1, fact + 1 ):
#     result = result * i
#     print(result)


# Write a Python script that reverses a list of integers using a for loop and prints the reversed list.

# number = [13 , 12,11, 10,9,8,7,6,5,4,3,2,1]

# reversed_list = []

# for num in range(1, len(number) + 1):

#     reversed_list.append(number[-num])

# print(reversed_list)





# Write a Python script that counts and prints the number of 
# vowels (a, e, i, o, u) in a user-input string using a for loop. Ignore case.

string = str(input('Please enter any string'))

count = 0
vowels = "aeiou"
for char in string:
    if char.lower() in vowels:
        count += 1
print(f"The vowels in given number are:{count}")


        










   

    
    



