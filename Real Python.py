# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 14:22:07 2021

@author: Anand
"""

#taking the details of each employee and storing it in a list
kirk = ["James Kirk", 34, "Captain", 2265]
spock = ["Spock", 35, "Science Officer", 2254]
mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]


#using init() to initialize every new instance of this class
class Dog:
    def _init_(self, name, age):
        self.name = name
        self.age = age

#giving a class attribute
class Dog:
    # Class attribute
    species = "Canis familiaris"

    def _init_(self, name, age):
        self.name = name
        self.age = age

#using two instance methods in the class Dog
class Dog:
    species = "Canis familiaris"

    def _init_(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
#adding another instance attribute 'breed'
class Dog:
    species = "Canis familiaris"

    def _init_(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

#creating child classes of the parent class Dog
class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

#providing a default value of bark for every child class
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"

#accessing parent class from child class using super()
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)
    