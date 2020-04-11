# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 12:54:22 2020

@author: Tudor's Pal
"""

import random
import os
import skimage as sk
from skimage import img_as_ubyte

class ImageAugment:

    def __init__(self, folder_path, destination_path = os.getcwd() , images_to_generate = 1, file_extension = ".png", rotate = True, noise = True, horizontal_flip = True):
        self.folder_path = folder_path
        self.destination_path = destination_path
        self.file_extension = file_extension
        self.generate_limit = images_to_generate
        self.transformations = {'rotate' : rotate, 'noise' : noise, 'horizontal_flip': horizontal_flip}
        self.image_paths = [os.path.join(self.folder_path, img) for img in os.listdir(self.folder_path) ]
        self.images = sk.io.imread_collection(self.image_paths)
        self.save_all()

    def rotate(self, image_array):
        return sk.transform.rotate(image_array, random.uniform(-360, 360))

    def random_noise(self, image_array):
        return sk.util.random_noise(image_array)

    def horizontal_flip(self, image_array):
        if random.uniform(0,1) >= 0.5:
            return image_array[:, ::-1]
        else:
            return image_array

    def apply_transformations(self, image_array):
        counter = 0
        transformed_images = []
        while counter != self.generate_limit:
            counter +=1
            original_image  = image_array
            if self.transformations['rotate']:
                original_image = self.rotate(original_image)
            if self.transformations['noise']:
                original_image = self.random_noise(original_image)
            if self.transformations['horizontal_flip']:
                original_image = self.horizontal_flip(original_image)
            transformed_images.append(original_image)
        return transformed_images

    def transform_all(self):
        transformed_images = []
        for image in self.images:
            transformed_images.extend(self.apply_transformations(image))
        return transformed_images

    def save_all(self):
        transformed_images = self.transform_all()
        img_num = 0
        for image in transformed_images:
            new_path = os.path.join(self.destination_path, "augmentedImg_" + str(img_num) + self.file_extension)
            #sk.io.imsave(new_path, image)
            sk.io.imsave(new_path, img_as_ubyte(image))
            img_num+=1









