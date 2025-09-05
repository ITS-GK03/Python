#  MATCH CASE TASK:

# 1.Check a day as weekday or weekend:

# day=input("Enter the day:")

# match day.lower():
#     case day if day=="monday" or day=="tuesday" or day=="wednesday" or day=="thursday" or day=="friday":
#         print("It is a weekday")

#     case day if day=="saturday" or day=="sunday":
#         print("It is a weekend")
    
#     case _:
#         print("Invalid day")


# 2.Print a no of days in a month:

# month=input("Enter a month:")

# match month.lower():
#     case month if month=="january" or month=="march" or month=="may" or month=="july" or month=="august" or month=="october" or month=="december":
#         print("The month has 31 days")

#     case month if month=="february":
#         print("The month has 28 days, In leap year 29 days")

#     case month if month=="april" or month=="june" or month=="september" or month=="november":
#         print("The month has 30 days")

#     case _:
#         print("Invalid month")


# 3.Print a entered input is vowels or consonants:

# character=input("Enter a character:")

# match character.lower():
#     case character if character in (" a,e,i,o,u"):
#         print("Charater is vowel")
    
#     case character if character in (" b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z"):
#         print("Charater is consonant")
    
#     case _:
#         print("Both vowel and consonant")


#  4.Grade by percentage:

# percentage=int(input("Enter the percentage:"))

# match percentage:
#     case percentage if percentage>=90 and percentage<=100:
#         print("A grade")
    
#     case percentage if percentage>=70 and percentage<=89:
#         print("B grade")

#     case percentage if percentage>=50 and percentage<=69:
#         print("C grade")

#     case percentage if percentage>=35 and percentage<=49:
#         print("D grade")

#     case percentage if percentage>=0 and percentage<=34:
#         print("Fail")

#     case _:
#         print("Invalid percentage")



#  5.Season based on month name:


# month=input("Enter the month:")

# match month.lower():
#     case month if month in ("december,january,february"):
#         print("It is winter season")
    
#     case month if month in ("march,april,may"):
#         print("It is a spring")
    
#     case month if month in ("june,july,august"):
#         print("It is a summer season")

#     case month if month in ("september,october,november"):
#         print("It is a autumn")

#     case _:
#         print("Plase enter a valid input")


# 6.Positive or negative:

# number=int(input("Enter a number:"))

# match number:
#     case number if number>=1:
#         print("Positive Number")

#     case number if number<0:
#         print("Negative Number")

#     case number if number==0:
#         print("Neither positive nor negative")


# 7.Get input from user print if it is between 1-50:

# number=int(input("Enter a number:"))

# match number:
#     case number if number>=1 and number<=50:
#         print("Number is in the range")
  
#     case _:
#         print("Number is not in the range")




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
    


class Animal:  

    def dog(self):
        print("Bark")
    
    def cat(self):
        print("Meowwww")


sound = Animal()

sound.dog()
sound.cat()