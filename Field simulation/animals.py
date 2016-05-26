# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 08:58:41 2016

@author: 97kristr
"""

from cow_class import *
from pig_class import *

def display_menu():
    print()
    print("Which animal would you like to create?")
    print()
    print("1. Cow")
    print("2. Pig")
    print()
    print("Please select an option from the above menu")
    
def select_option():
    valid_option = False
    while not valid_option:
        try:
            choice = int(input("Option selected: "))
            if choice in (1,2):
                valid_option = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice

def create_animal():
    display_menu()
    choice = select_option()
    if choice == 1:
        new_animal = Cow()
    elif choice == 2:
        new_animal = Pig()
    return new_animal
    
def main():
    new_animal = create_animal()
    manage_animal(new_animal)
    
if __name__ == "__main__":
    main()