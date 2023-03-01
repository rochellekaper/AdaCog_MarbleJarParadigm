#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 17:02:16 2023

@author: rochellekaper
"""
import numpy
from PIL import Image, ImageDraw, ImageFont
import random
import glob
import os

f_out = open("dictionary.txt", "w")


def generate_marblejar(amount_of_jars):  #specify number of images you want generated
    file_colors = dict()
    #Dictionary stores the jar image file path as the value & the key is the associated marble jar color list
    #list of all marble color lists 
    col_list_of_lists = []
    
    
    for i in range(amount_of_jars):
        ''' specify marble color probability:
            Highest value marble = 17% chance of being in jar, 
            Medium value marble = 33% chance of being in jar,
            Lowest value marble = 50% chance of being in jar '''
            
        random_num_list = list(numpy.random.choice(range(2,5),size=9, p=[0.5, 0.33, 0.17]))
        col_list = [1] * 9 
        
        for index, val in enumerate(random_num_list):
             if val == 2:        
                 col_list[index] = 'red'
             if val == 3:        
                 col_list[index] = 'green'   
             if val == 4:        
                 col_list[index] = 'purple'
                 
        col_list_of_lists.append(col_list)
         

        w, h = 250, 250
        shape = [(1,1), (w-1, h-1)]
        # creating new Image object
        img = Image.new("RGB", (w, h),)
        # create rectangle (jar)
        img1 = ImageDraw.Draw(img) 
        img1.rectangle(shape, fill ="white", outline ="black")
        img1.ellipse((25, 25, 85, 85), fill = col_list[0], outline = col_list[0]) #marble 1 
        img1.ellipse((95, 25, 155, 85), fill = col_list[1], outline = col_list[1]) #marble 2
        img1.ellipse((165, 25, 225, 85), fill = col_list[2], outline = col_list[2]) #marble 3
        img1.ellipse((25, 95, 85, 155), fill = col_list[3], outline = col_list[3]) #marble 4
        img1.ellipse((95, 95, 155, 155), fill = col_list[4], outline = col_list[4]) #marble 5
        img1.ellipse((165, 95, 225, 155), fill = col_list[5], outline = col_list[5]) #marble 6
        img1.ellipse((25, 165, 85, 225), fill = col_list[6], outline = col_list[6]) #marble 7
        img1.ellipse((95, 165, 155, 225), fill = col_list[7], outline = col_list[7]) #marble 8
        img1.ellipse((165, 165, 225, 225), fill = col_list[8], outline = col_list[8]) #marble 9
        #img.show()
        img.save(r'/Users/rochellekaper/Desktop/AdaCog/Jar Selection Task/Stimuli/marblejar'+str(i)+".jpg")
        
        
    
    for filename, i in zip(glob.glob('/Users/rochellekaper/Desktop/AdaCog/Jar Selection Task/Stimuli/*.jpg'), range(len(col_list_of_lists))): 
        file_colors[filename] = col_list_of_lists[i]
        
    
    return file_colors #return dictionary


path_colors_dict = generate_marblejar(12)
 

#write out dictionary to text file 
with open("dictionary.txt", 'w') as f: 
    for key, value in path_colors_dict.items(): 
        f.write('%s:%s\n' % (key, value))     



f_out.close() 




