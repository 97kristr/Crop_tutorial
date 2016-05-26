# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 08:35:11 2016

@author: 97kristr
"""

from animal_class import *

class Pig(Animal):
    """en gris"""
    
    #konstruktor
    def __init__(self, name):
        #call the parent class construktor with default values for potato
        #growthrate= 1; light need = 3; water need = 6
        super().__init__(1,3,6)
        self._type = "Pig"
        self.name = name
        
        
    #override grow method for subclass
    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "Child" and water > self._water_need:
                self._weight += self._growth_rate * 1.8
            elif self._status == "Young" and water > self._water_need:
                self._weight += self._growth_rate * 1.5
            else:
                self._weight += self._growth_rate
        #increament days growing
        self._days_growing += 1
        #update the status
        self._update_status()
        
def main():
    #Gör en ny potatis planta
    pig_animal = Pig()
    print(pig_animal.report())
    manual_grow(pig_animal)
    print(pig_animal.report())
    manual_grow(pig_animal)
    print(pig_animal.report())
    
if __name__ == "__main__":
    main()