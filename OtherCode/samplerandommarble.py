# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 09:56:28 2022

@author: Rochelle Kaper
"""

import random

class Jar:      
    """
    marbles = [{0: 'red'}, 
               {1: 'purple'}, 
               {2: 'green'}]
    """
    def __init__(self, name):
        self.name = name
        self.marble = {}
        self.marbles = []
   
    def add_marble(self, marble, weight): 
        self.marble[weight] = marble
        self.marbles.append(self.marble)
        self.marble = {}
        
    def cleanse(self):
        self.marble.clear()
        return self.marble
             
    def print_stuff(self,stuff):
        print('print:', stuff)

        
        
r = Jar('my_jar')
#print('--------- START ---')
r.add_marble('red', 0)
r.add_marble('purple', 1)
r.add_marble('green', 2)

print('random:', random.choice(r.marbles))


