#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Muhammad Umair Mughal
# DATE CREATED: 16.06.2024              
# REVISED DATE: 03.07.2024
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir
#
#
# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    
    # Get list of files in directory
    filenames = listdir(image_dir)
    
    # Initialize an empty dictionary for results
    results_dic = {}
    
    # Iterate over each filename in the directory
    for filename in filenames:
        # Skip hidden files
        if filename.startswith('.'):
            continue
        
        # Process the filename to extract the pet label
        pet_label = extract_pet_label(filename)
        
        # Add the filename and pet label to the dictionary
        if filename not in results_dic:
            results_dic[filename] = [pet_label]
        else:
            print(f"Warning: Duplicate file {filename} exists in results_dic")
    
    for key in results_dic:
        print('\nfilename = ', key, '    pet label = ', results_dic[key][0])
    
    # count length in full dictionary
    number_of_items_full_dic = len(results_dic)
    print('\nDictionary has {} items'.format(number_of_items_full_dic))

    
    return results_dic

def extract_pet_label(filename):
    """
    Extracts the pet label from a given filename.
    
    Parameters:
     filename - The filename of the image (string)
     
    Returns:
     pet_label - The pet label extracted and formatted (string)
    """
    # Convert filename to lowercase and split on underscores
    words = filename.lower().split('_')
    
    # Filter out non-alphabetic words and join remaining words with a space
    pet_label = ' '.join([word for word in words if word.isalpha()]).strip()
    
    return pet_label
