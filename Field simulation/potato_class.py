# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 08:35:11 2016

@author: 97kristr
"""

from crop_class import *

class Potato(Crop):
    """en potatis planta"""
    
    #konstruktor
    def __init__(self) :
        #call the parent class construktor with default values for potato
        #growthrate= 1; light need = 3; water need = 6
        super().__init__(1,3,6)
        self._type = "Potato"
        
    #override grow method for subclass
    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            if self._status == "Seedling" and water > self._water_need:
                self._growth += self._growth_rate * 1.5
            elif self._status == "Young" and water > self._water_need:
                self._growth += self._growth_rate * 1.25
            else:
                self._growth += self._growth_rate
        #increament days growing
        self._days_growing += 1
        #update the status
        self._update_status()
        
def main():
    #Gör en ny potatis planta
    potato_crop = Potato()
    print(potato_crop.report())
    manual_grow(potato_crop)
    print(potato_crop.report())
    manual_grow(potato_crop)
    print(potato_crop.report())
    
if __name__ == "__main__":
    main()