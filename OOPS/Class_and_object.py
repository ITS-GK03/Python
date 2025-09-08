# oops - object oriented programming system:

# CLASS - OBJECT:


# 1.create class Goa . Function as party , beach:

# class Goa:
#     fun_activities=""
#     party_place=""
#     age=0

#     def party(self):
#         print("Such a happrning place a full fun and party mode on and a boys trip bucket list place is goa........")
    
#     def beach(self):
#         print("Beach is full of water activities and fun filled combo")
    

# goa1=Goa()
# goa1.fun_activities="Water sliding"
# goa1.age=20
# print(goa1.fun_activities)
# print(goa1.age)

# goa1.beach()

# print("\n")
# goa2=Goa()
# goa2.party_place="Beach house"
# goa2.age=22
# print(goa2.party_place)
# print(goa2.age)

# goa2.party()



# 2. Create a  class called laptop. Create  the following variables and functions . 
#   		Var = price, processor, ram
# Create object as Lenovo, HP, Dell

# class Laptop:
#     price_lap=0
#     processor_lap=""
#     ram_lap=0

#     def lenovo(self):
#         print("Lenovo has a best processoor aand ram in lapton but it has issue of price..... ")
    
#     def hp(self):
#         print("HP has best in all it has no issues abouyt laptop.....")

#     def dell(self):
#         print("Dell has best ram and price but it has heating isses ")


# laptop1=Laptop()
# laptop1.price_lap=55000
# laptop1.processor_lap="Intel i12"
# laptop1.ram_lap=16
# print(laptop1.price_lap)
# print(laptop1.processor_lap)
# print(laptop1.ram_lap)

# laptop1.lenovo()

# print("\n")
# laptop2=Laptop()
# laptop2.price_lap=60000
# laptop2.processor_lap="Intel i14"
# laptop2.ram_lap=16
# print(laptop2.price_lap)
# print(laptop2.processor_lap)
# print(laptop2.ram_lap)

# laptop2.hp()

# print("\n")
# laptop3=Laptop()
# laptop3.price_lap=40000
# laptop3.processor_lap="Intel i12"
# laptop3.ram_lap=8
# print(laptop3.price_lap)
# print(laptop3.processor_lap)
# print(laptop3.ram_lap)

# laptop3.lenovo()



# 3.create class called Kodaikanal.and create all the possible variables and functions:

# class Kodaikanal:
#     def __init__(self, place1, place2):
#         self.place1=place1
#         self.place2=place2
    
#     def getter_fun(self):
#         print("Place 1:", self.place1)
#         print("Place 2:", self.place2)

# kodai1=Kodaikanal("Guna Cave", "Pine forest")

# kodai1.getter_fun()


#OOPS - Object Orientation Programing System.
#OOPS is used for code resuablity,update and also security...

#Types of OOPS:                                              
# 1.class and objects
# 2.Encapsulation
# 3.Inheritance
# 4.Polymorphism
# 5.Abstraction 



# class mygame:
#     userid = "evil"
#     level=71

#     def account(self):
#         print("Id worth 35k browww")


# myid=mygame()
# print(myid.userid)

# myid=mygame()
# print(myid.level)

# myid.account()




# class cricket:
#     player="gowtham"

#     def __init__(self, name, jer_num):
#         self.name= name
#         self.jer_num= jer_num

#     def display(self):
#         print(f"Name of the player:  {self.name}, jersey number is:  {self.jer_num}")



# cricket2=cricket("Gowtham sanjay", 7)
# cricket2.display()



# OOPS:

#2.Inheritance:

# * Inheritance - Inheritance is a mechanism that allows one class properties(Attributes,Method) to another class...
# * Inheritance is used for Code reusability etc.....


# Types of Inheritance:

# 1. Single Inheritance – One child class inherits from one parent class.
# 2. Multiple Inheritance – One child class inherits from multiple parent classes.
# 3. Multilevel Inheritance – A class inherits from a class which itself inherits from another class.
# 4. Hierarchical Inheritance – Multiple child classes inherit from a single parent class.
# 5. Hybrid Inheritance – A combination of two or more types of inheritance.


#Type1: (SINGLE INHERITANCE)

# class father:
#     name = "Saleem"
#     def father_job(self):
#         print("Father is a doctor")
# class son (father):
#     son_name = "Nayeem........ son of saleem "
#     def son_job(self):
#         print("CSE student")
# s=son()
# print(s.name)
# print(s.son_name)
# s.father_job()
# s.son_job()



#Type2:-(MULTIPLE INHERITANCE)

# class sample1:
#     def bike(self):
#         print("Dhilip can drive bikes")
# class sample2:
#     def car(self):
#         print("Dhilip can also drive cars")
# class dhilip(sample1,sample2):
#     pass

# m=dhilip()
# m.bike()
# m.car()


#Type3:-(MUPLTILEVEL INHERITANCE)

# class Grandfather:
#     def grandfather_name(self):
#         print("Mohamadh Ali ")
# class Father(Grandfather):
#     def father_name(self):
#         print("Saleem")
# class Son(Father):
#     def son_name(self):
#         print("Nayeem")
# s = Son()
# s.grandfather_name()
# s.father_name()
# s.son_name()


#Type4.(HIERARCHICAL INHERITANCE)
# class name:
#     def parent(self):
#         print("Senthil Kumar is the Parent")
# class child1(name):
#     def name(self):
#         print("Kamalini is the daughter of Senthil Kumar")
# class child2(name):
#     def name2(self):
#         print("Dhilip Kumar is the son of Senthil Kumar")

# obj1=child1()
# obj2=child2()

# obj1.parent()
# obj1.name()
# obj2.name2()



#3.Polymorphism:

#Polymorphism = Polymorphism refers to the different objects to respond on the same method with differnt ways...


#Types of Polymorphism:

#1. Run Time Polymorphism:(Dynamic polymorphism)
#Run-Time Polymorphism means the function that will run is decided while the program is running, not before.

#2. compile Time Polynorphism:(static polymorphism)
# Compile-Time Polymorphism means the function or operator is decided before the program runs (at compile time).



# Example of Polymorphism:

# class name:
#     def speak(self):
#         print("Dhilip Kumar")
# class name1:
#     def speak(self):
#         print("Vetrichelvan")
# class name2:
#     def speak(self):
#         print("Gowtham")

# object1=name()
# object2=name1()
# object3=name2()
# object1.speak()
# object2.speak()
# object3.speak()



#Type1:(Complier Time Polymorphism)

# class num:
#     def values(self,a=2,b=0,c=9):
#         return a+b+c
    
# object=num()
# print(object.values(10,20,30))
# print(object.values(10))
# print(object.values(1,3))



#Type2:(Run Time Polymorphism)

# class name:
#     def speak(self):
#         print("Dhilip Kumar")
# class name1:
#     def speak(self):
#         print("Vetrichelvan")
# class name2:
#     def speak(self):
#         print("Gowtham")

# objects=[name(),name1(),name2()]
# for i in objects:
#     i.speak()




# 4.Encapsulation:

#bundle of variable and methods 
#three types of Encapsulation:
#1. Public 
#2.Protected (_)
#3. Private  ()



#1.public can be usable in anywhere:

# class MyClass:
#     def _init_(self):
#         self.name = "gowtham" 

# obj = MyClass()
# print(obj.name)



#2. Protected can be usable when another by another class:

# class MyClass:
#     def _init_(self):
#         self._age = 25  

# class Child(MyClass):
#     def show_age(self):
#         print(self._age)

# obj = Child()
# obj.show_age()     
# print(obj._age) 



#3.private can be accessable by another function method:

# class MyClass:
#     def _init_(self):
#         self.__salary = 700000  

#     def show_salary(self):
#         print(self.__salary)

# obj = MyClass()
# obj.show_salary()    


# class myclass:
#     def _init_(self,name,age):
#         self.name=name
#         self._age=age
#         self.__salary= 7000000

#     def get_salary(self):
#         return self.__salary
    
#     def set_salary(self,new_salary):
#         if new_salary>0:
#             return self.__salary== new_salary
#         else:
#             return ("Invalid salary")
        
#     def display_info(self):
#         print(f"Name: {self.name}, Age: {self.age}, Salary: {self._salary}")

# obj=myclass("gowtham",28)
# print(obj.name)



# 5. Abstraction:


# from abc import ABC, abstractmethod

# class Payment(ABC):

#     @abstractmethod
#     def make_payment(self, amount):
#         pass


# class CreditCardPayment(Payment):
#     def make_payment(self, amount):
#         print(f"Paid ₹{amount} using Credit Card.")


# def process_payment(payment_method: Payment, amount: float):
#     payment_method.make_payment(amount)


# p1 = CreditCardPayment()

# process_payment(p1, 1000)
    


# class Animal:  

#     def dog(self):
#         print("Bark")
    
#     def cat(self):
#         print("Meowwww")


# sound = Animal()

# sound.dog()
# sound.cat()