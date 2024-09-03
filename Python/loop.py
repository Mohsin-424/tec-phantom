# for i in range(0,100,16):
#     print(i)

# # For Loop
# x = 10

# for i in range(x):
#     print(i)
#     if i == 5:
#         print(f'{i} is multiple of 5')
#     else:
#         print(f'{i} is not a multiple of 5')


# for i in range(10):
#     if i == 5:
#         break
#     print(i)





# i = 1
# while i < 6:
#   print(i)
#   if (i == 3):
#     break
#   i += 1


# Write a program that prints the numbers from 1 to n. But for multiples of 3, print 'Fizz' 
#  instead of the number, and for multiples of 5, print 'Buzz'. For numbers that are multiples of both 3 and 5, print 'FizzBuzz'

mohsin = [1 , 2,3,43,4,5,6,23,7,8]
for i in mohsin:
    if i%3 == 0:
        print("Fizz")
    elif i % 5 ==0:
        print("Buzz")
    elif  i%3 == 0 and i%5 ==0:
        print("Fizz Buzz")
    else:
        print("Nothing")


        
mohsin = [1 , 2,3,43,4,5,6,23,7,8]
for i in mohsin:
    if i%3 == 0:
        print("Fizz")
    elif i % 5 ==0:
        print("Buzz")
    elif  i%3 ==0 and i%5 ==0:
        print("Fizz Buzz")
    else:
        print("Nothing")



        


# name1 = ["Hello"]
# name2 = ["Mohsin" , "Salman " , "Noor", "Hamza" , "John Doe", "John"]
# for i, l in enumerate(name1):
#     for j, b in enumerate(name2):
#         print(i, j,l , b)
    

ls1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
ls2 = []

for i in ls1:
    if i % 2 == 0:
        ls2.append(i)

    elif i % 5 == 0:
        ls2.append(i)
    else:
        print(i)


print(ls2)




