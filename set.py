# my_set = { 1,2 , 3,4,5,6,7,8,9,10}
# x = type(my_set)
# print(x)

# # Set Constructor
# my_set = set([1,2,3,4])
# print(my_set)
# # # print(len(my_set))
# # # print(len( my_set)- 1 )

# my_set.discard(2)

# # # my_set.add(20)
# print(my_set)


set1 = {1 ,2,3,4,5,6,7,8,9,10}
set2 = {"I ", "Love", "You", "", "5", "Hello", "World"}
set3 = {"I ", "am" , "a Boy", True , 0}

# set1.update(set2)
# print(set1)

# set1.remove("5")
# print(set1)

# set3 = set1.union(set2)
set4 = set1 | set2 | set3
# | standing bar is used for union in Python
print(set4)
# set3 = set1.intersection(set2)
# print(set3)

set5 = set1 & set2 & set3
print(set5)

set6 = set1 & set2 | set2 & set3 - set4
print(set6)

