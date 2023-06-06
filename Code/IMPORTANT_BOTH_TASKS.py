#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 14:16:49 2023

@author: rochellekaper
"""

''' Best file!!! Code to generate shared marble jar stimuli for both Change Detection and Jar Selection Tasks along with 3rd jars for Change Detection. 
Will also output a dictionary of the file path and marble jar colors for each jar to use for Jar Selection Task. 
There is also a function to output jars equal to the same amount of points.
'''


''' NOTE: The colors to chance of being generated in jar is dependent on the color to points 
mapping (6 options). Path will also be changed depending on the mapping to be put in the right
folder. '''

import numpy
from PIL import Image, ImageDraw
import glob
from natsort import natsorted 
import random

r_l_out = open("path_col.txt", "w")


def generate_marblejar_right_left(amount_of_jars, whichjar): 
    #specify number of images you want generated
    #specify if this is marble jar 1 (left) or marble jar 2 (right)
    file_colors = dict()
    #Dictionary stores the jar image file path as the value & the key is the associated marble jar color list
    col_list_of_lists = [] #list of all marble color lists 
    
    img_list = [] #list of marble jar images
    for i in range(amount_of_jars):
        random_num_list = list(numpy.random.choice(range(2,5),size=9, p=[0.5, 0.33, 0.17]))
        col_list = [1] * 9 
        
        for index, val in enumerate(random_num_list):
             if val == 2:        
                 col_list[index] = 'darkorange'
             if val == 3:        
                 col_list[index] = 'green'   
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
        img.save(r'/Users/rochellekaper/Desktop/Both_Tasks/orange_green_purple/Stimuli/reg_trials/marblejar'+"_"+str(whichjar)+"_"+str(i)+".jpg")
        img_list.append(img)
    
    files = list(zip(glob.glob('/Users/rochellekaper/Desktop/Both_Tasks/orange_green_purple/Stimuli/reg_trials/marblejar_' + str(whichjar) + '*.jpg')))
    files = natsorted(files)

    
    for filename, i in zip(files, range(len(col_list_of_lists))): 
        filename = '.' + str(filename)[61:-3] #relative path 
        file_colors[filename] = col_list_of_lists[i]
        

    return img_list, file_colors


def rollDice(amount_of_jars):
    ''' Randomize whether marble jar 3 will be the same or different. Returns 'same' or 'different' '''
    jar3 = ''
    jar3_list = [] 
    for i in range(amount_of_jars):
        roll = numpy.random.choice(range(1,3))
        if roll == 1:
            jar3 = 'same'
            jar3_list.append(jar3)
            
        else:
            jar3 = 'different'
            jar3_list.append(jar3)
    return jar3_list


def generate_jar3(jar_images, list_jar3, whichjar):
    file_colors = dict()
    #Dictionary stores the jar image file path as the value & the key is the associated marble jar color list
    col_list_of_lists = [] #list of all marble color lists 
    img_list = [] #list of marble jar images
    
    
    for i, j in enumerate(list_jar3):
        if j == 'same':
            jar_images[i].save(r'/Users/rochellekaper/Desktop/Both_Tasks/orange_green_purple/Stimuli/reg_trials/marblejar3'+"_"+ whichjar+"_"+str(j)+"_"+str(i)+".jpg")
            img_list.append(jar_images[i])

        if j == 'different':
            random_num_list = list(numpy.random.choice(range(2,5),size=9, p=[0.4, 0.4, 0.2]))
            col_list = [1] * 9 
            
            for index, val in enumerate(random_num_list):
                 if val == 2:        
                     col_list[index] = 'darkorange'
                 if val == 3:        
                     col_list[index] = 'green'   
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
            img.save(r'/Users/rochellekaper/Desktop/Both_Tasks/orange_green_purple/Stimuli/reg_trials/marblejar3'+"_"+str(whichjar)+"_"+str(j)+"_"+str(i)+".jpg")
            img_list.append(img)
            
    files = list(zip(glob.glob('/Users/rochellekaper/Desktop/Both_Tasks/orange_green_purple/Stimuli/reg_trials/marblejar3_' + str(whichjar) + '*.jpg')))
    files = natsorted(files)


        
    for filename, i in zip(files, range(len(col_list_of_lists))): 
       filename = '.' + str(filename)[61:-3] #relative path 
       file_colors[filename] = col_list_of_lists[i]
   
    return img_list, file_colors

#risk aversion
def specify_jar_pts(points, num_jars): #takes in total amount of points you want jar to equal & how many jars being generated (multiples of 3)
    file_colors = dict()
    #Dictionary stores the jar image file path as the value & the key is the associated marble jar color list
    col_list_of_lists = [] #list of all marble color lists 
    img_list = [] #list of marble jar images
    
    for i in range(num_jars):
    
        random_num_list = list(numpy.random.choice(range(2,5),size=9))
        while sum(random_num_list) != points:
            random_num_list = list(numpy.random.choice(range(2,5),size=9, p=[0.4, 0.4, 0.2]))
            if sum(random_num_list) == points:
                break
        col_list = [1] * 9 
    
        for index, val in enumerate(random_num_list):
             if val == 2:        
                 col_list[index] = 'darkorange'
             if val == 3:        
                col_list[index] = 'green'
             if val == 4:        
                 col_list[index] = 'purple'   
        random.shuffle(col_list)
        col_list_of_lists.append(col_list)
        
        w, h = 250, 250
        shape = [(1,1), (w-1, h-1)]
        # creating new Image object
        img = Image.new("RGB", (w, h),)
        # create rectangle (jar)
        img1 = ImageDraw.Draw(img) 
        img1.rectangle(shape, fill ="white", outline ="black")
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
        img.save(r'/Users/rochellekaper/Desktop/Both_Tasks/orange_green_purple/Stimuli/marblejar'+"_"+str(points)+"points"+str(i)+".jpg")
        img_list.append(img)
   
    files = list(zip(glob.glob('/Users/rochellekaper/Desktop/Both_Tasks/orange_green_purple/Stimuli/marblejar_' +str(points) + '*.jpg')))
    files = natsorted(files)

    for filename, i in zip(files, range(len(col_list_of_lists))): 
        filename = '.' + str(filename)[61:-3] #relative path 
        file_colors[filename] = col_list_of_lists[i]
            

    return img_list, file_colors
 
    

# right_jars, file_colors_right = generate_marblejar_right_left(112, 'right')
# left_jars, file_colors_left = generate_marblejar_right_left(113, 'left')


# jar_3_list_right = rollDice(112)
# right3, right3_files = generate_jar3(right_jars, jar_3_list_right, 'right')
# jar_3_list_left = rollDice(113)
# left3, left3_files = generate_jar3(left_jars, jar_3_list_left, 'left')



# #write out dictionaries to text file 
# with open("path_col.txt", 'w') as f: 
#     for key, value in file_colors_right.items(): 
#         f.write('%s:%s\n' % (key, value))    
#     for key, value in file_colors_left.items(): 
#         f.write('%s:%s\n' % (key, value))    
        
#     for key, value in right3_files.items(): 
#         f.write('%s:%s\n' % (key, value))    

#     for key, value in left3_files.items(): 
#         f.write('%s:%s\n' % (key, value))    

 
# r_l_out.close() 



''' Risk Aversion Trials '''

#Generate 3 marble jars that all equal to the same amount of points. Generating 3 incase it is a Change Detection Task
#Need to randomize whether the 3rd jar is same or different (or do it manually as I am now.)     


# imgs, files_col = specify_jar_pts(29, 15)
# imgs1, files_col1 = specify_jar_pts(28, 30)
# imgs2, files_col2 = specify_jar_pts(27, 30)
# imgs3, files_col3 = specify_jar_pts(26, 30)
# imgs4, files_col4 = specify_jar_pts(25, 30)
# imgs5, files_col5 = specify_jar_pts(24, 30)
# imgs6, files_col6 = specify_jar_pts(23, 30)
# imgs7, files_col7 = specify_jar_pts(22, 15)
# imgs8, files_col8 = specify_jar_pts(30, 15)


# #write out to text file

             
# with open("file_colors_riskaversion.txt", 'w') as r: 
#     for key, value in files_col.items(): 
#         r.write('%s:%s\n' % (key, value))  
#     for key, value in files_col1.items(): 
#         r.write('%s:%s\n' % (key, value))     
#     for key, value in files_col2.items(): 
#         r.write('%s:%s\n' % (key, value))  
#     for key, value in files_col3.items(): 
#         r.write('%s:%s\n' % (key, value))        
#     for key, value in files_col4.items(): 
#         r.write('%s:%s\n' % (key, value))        
#     for key, value in files_col5.items(): 
#         r.write('%s:%s\n' % (key, value))
#     for key, value in files_col6.items(): 
#         r.write('%s:%s\n' % (key, value))
#     for key, value in files_col7.items(): 
#         r.write('%s:%s\n' % (key, value))   
#     for key, value in files_col8.items(): 
#         r.write('%s:%s\n' % (key, value))   






   