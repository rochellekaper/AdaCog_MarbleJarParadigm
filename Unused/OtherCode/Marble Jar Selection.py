#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 22:06:13 2023

@author: rochellekaper
"""

import numpy
from PIL import Image, ImageDraw, ImageFont
import random


def generate_jar(jar_num):
    ''' Function to generate a marble jar image.
    Input is either 1 (jar 1) or 2 (jar 2) '''     
    
    ''' specify marble color probability:
            purple = highest value marble, 20% chance of being in jar;
           green & red both 40% chance of being in jar '''
    random_num_list = list(numpy.random.choice(range(2,5),size=9, p=[0.4, 0.4, 0.2]))
    col_list = [1] * 9 
        
    for index, val in enumerate(random_num_list):
         if val == 2:        
             col_list[index] = 'red'
         if val == 3:        
             col_list[index] = 'green'   
         if val == 4:        
             col_list[index] = 'purple'
             
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
    img.save(r'marblejar'+"_"+str(jar_num)+".jpg")
    return img, col_list


jar1, colors_1 = generate_jar(1)
jar2, colors_2 = generate_jar(2)

#Show both marble jars next to each other
jar1 = Image.open('/Users/rochellekaper/Desktop/AdaCog/marblejar_1.jpg')
#jar1.show()
jar2 = Image.open('/Users/rochellekaper/Desktop/AdaCog/marblejar_2.jpg')
#jar2.show()
jar1 = jar1.resize((250, 250))
jar1_size = jar1.size
jar2_size = jar2.size
new_image = Image.new('RGB',(2*jar1_size[0], jar1_size[1]), (250,250,250))
new_image.paste(jar1,(0,0))
new_image.paste(jar2,(jar1_size[0],0))
#new_image.save("merged_image.jpg","JPEG")
new_image.show()


#Ask user to pick a jar to sample from
print("red = 2; green = 3; purple = 4\n")
which_jar = input(str("Which jar do you want to sample a marble from?\nPress 'r' for right; Press 'l' for left:\n")).lower()

if which_jar == "l": #jar1
    color = random.choice(colors_1)
    if color == 'red':
        points = 2
    elif color == 'green':
        points = 3
    else:
        points = 4
    print('\nThe marble selected was ', color, '.', ' You got ', points, ' points.', sep = '')
if which_jar == "r": #jar2
    color = random.choice(colors_2)
    if color == 'red':
        points = 2
    elif color == 'green':
        points = 3
    else:
        points = 4
    print('\nThe marble selected was ', color, '.', ' You got ', points, ' points.', sep = '')
