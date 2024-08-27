
# class Person:
#     x = 10**2
# p =  Person()
# print(p.x)


# class Person():
#     def __init__(self, name , age):
#         self.name = name
#         self.age = age
#     def show(self):
#         print(f"Name: {self.name}, Age: {self.age}")


# p = Person("John Doe", 26)
# print(p.name , p.age)

# p.show()


# p1 = Person("Mohid",34)

# print(p1.name , p1.age)

# p1.show()


# p2 = Person("Muhammad Mohsin" , 232)
# print(p2.name , p2.age)
# p2.show()




# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person( "Muhammad Mohsin", 24 )

# print(p1.name)
# print(p1.age)



# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def show(self):
#     return f" the  namae is :: {self.name},  with age: {self.age}"
#   def __del__(self):             #De structors
#        return f" the Person with Name: {self.name},with Age: {self.age} is deleted from the class Python"
  


# p1 = Person( "Muhammad Mohsin", 24 )
# p1.show()

# print(p1.name)
# print(p1.age)








# Inheritance 
# class Animal:
#    def __init__(self , name):
#       self.name = name
# #       print("Animal created")
#    def show(self):
#       print(f"Name:  {self.name}")


# class Cat(Animal):
#    def meo(self):
#       print(f'{self.name} is meowing')

# c = Cat("Cat") 
# c.meo()


# Multilevel Inheritance


# class Parent:
#    def __init__(self, name):
#       self.name = name
#       print("Multilevel created as Parent")
# class Child(Parent):
#    def show(self):
#       print( self.name)

# class GrandChild(Child):
#    def show(self):
#       print(self.name)
#       super().show()

# gc = GrandChild("grandchild")
# gc.show()

# ab = Parent("ab")
# ab.show()






# ...................Multilpe Inheritance.......................

# class Parent1:
#     def __init__(self, name):
#         self.name = name
#         print("Multiple  created as Parent11")
# class Parent2:
#     def __init__(self,age):
#         self.age = age
#         print("Multiple  created as Parent2")

# class Child(Parent2, Parent1):

#     def show(self):
#         print(f'Age: {self.age}')

# p  = Child(3)
# p.show()




# class Parent1:
#     def __init__(self, name):
#         self.name = name
#         print("Multiple  created as Parent11")
# class Parent2:
#     def __init__(self,age):
#         self.age = age
#         print("Multiple  created as Parent2")

# class Child(Parent1, Parent2):  # Order changed this time

#     def show(self):
#         print(f'Nmae : {self.name}')

# p  = Child("gOPI kISHAN")          #Mre do do baap
# p.show()



# # .................................. Method Resolution Order MRO ................................

# class Parent1:
#     def __init__(self, name , age):
#         self.name = name
#         self.age = age
#         print("Multiple  created as Parent11")
# class Parent2:
#     def __init__(self,age):
#         self.age = age
#         print("Multiple  created as Parent2")

# class Child(Parent1, Parent2):  # Order changed this time

#     def show(self):
#         print(f'Nmae : {self.name} have age: {self.age}')

# p  = Child("gOPI kISHAN" , 23)          #Mre do do baap
# p.show()




# Polymorphism in Python
# class P1:
#     def show(self):
#         print("P1 show")
# class P2:
#     def show(self):
#         print("P2 show")
# # s = P1()
# s = P2()
# s.show()


# # Polymorphism in Python
# class P1:
#     def display(self):
#         print("P1 show")
# class P2:
#     def display(self):
#         print("P2 show")
# # s = P1()
# # s = P2()
# # s.display()

# x = P1()
# x.display()




# .......................................... Abstraction ............................................


class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def display(self):
        # for abstraction we nened to add abstractions
        total = self._salary + 230000
        print(f"Name: {self._name}, Salary: {self._salary}, Total: {total}")
        # print(f"Name: {self._name}, Salary: {self._salary}")

x = Employee("ashutosh" , 230000 )
x.display()

# Private Public Protected Methods









