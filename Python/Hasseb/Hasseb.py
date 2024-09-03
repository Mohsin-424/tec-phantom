mohsin = [1 , 2,3,43,4,5,6,23,7,8 , 33, 50, 90 , 34]
for i in mohsin:
    if i%3 == 0:
        print("Fizz")
    elif i % 5 ==0:
        print("Buzz")
    elif  i%3 ==0 and i%5 ==0:
        print("Fizz Buzz")
    else:
        print("Nothing")
