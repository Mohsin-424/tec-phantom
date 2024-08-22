# try:
#     # Code that may raise an exception
#     x = 1 / 0
# except ZeroDivisionError:
#     # Code to handle the exception
#     print("Error: Division by zero is not allowed.")
# else:
#     print("No error occured Finally")
# finally:
#     # Code that will always be executed, regardless of whether an exception occurred or not
#     print("This code will always be executed.")



# File Handling

# f  = open("example.txt", "w")
# f.write("Hello, world!")
# f.write("Hello, world2 ")


# f  = open("example.txt", "a")
# f.write("Hello, world!")To reove files we need to import os

# import os
# old_name = "example.txt"
# new_name = "new_file.txt"
# os.rename(old_name, new_name)



# f  = open("example.txt", "a")
# f.write("Hello, world!")
# f.close()


# f  = open("example.txt", "a")
# f.read()


f = open("example.txt", "r")
data = f.read()
print(data)
f.close()




# r = read
# a = append
# w = write