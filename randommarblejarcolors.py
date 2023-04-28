# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 17:28:36 2022

@author: Rochelle Kaper
"""

import numpy
from PIL import Image, ImageDraw
import glob
from natsort import natsorted 
import random

f_out = open("random.txt", "w")
    
def generate_random_marblejar(amount): 
    #specify number of images you want generated
    #specify if this is marble jar 1 (left) or marble jar 2 (right)
    file_colors = dict()
    #Dictionary stores the jar image file path as the value & the key is the associated marble jar color list
    col_list_of_lists = [] #list of all marble color lists 
    
    img_list = [] #list of marble jar images
    for i in range(amount):
        random_num_list = list(numpy.random.choice(range(2,5),size=9, p=[0.5, 0.33, 0.17]))
        col_list = [1] * 9 
        
        for index, val in enumerate(random_num_list):
             if val == 2:        
                 col_list[index] = 'green'
             if val == 3:        
                 col_list[index] = 'darkorange'   
             if val == 4:        
                 col_list[index] = 'purple'
        #print(col_list)
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
        img.save(r'/Users/rochellekaper/Desktop/Both_Tasks/green_orange_purple/Stimuli/reg_trials/rand_marblejar'+"_"+str(i)+".jpg")
        img_list.append(img)
    
    files = list(zip(glob.glob('/Users/rochellekaper/Desktop/Both_Tasks/green_orange_purple/Stimuli/reg_trials/rand*.jpg')))
    files = natsorted(files)

    
    for filename, i in zip(files, range(len(col_list_of_lists))): 
        filename = '.' + str(filename)[61:-3] #relative path 
        file_colors[filename] = col_list_of_lists[i]
        

    return img_list, file_colors

rand, rand_files = generate_random_marblejar(225)

with open("random.txt", 'w') as f: 
    for key, value in rand_files.items(): 
        f.write('%s:%s\n' % (key, value))    


f_out.close




