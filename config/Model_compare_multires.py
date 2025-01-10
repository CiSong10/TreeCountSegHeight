#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 22:23:40 2021

@author: sizhuo
"""

import os

class Configuration:
    def __init__(self):
        self.input_image_dir = './example_extracted_data/'
        self.input_image_type = '.png'
        self.channel_names = ['red', 'green', 'blue']
        self.label_names = ['annotation', 'boundary', 'ann_kernel']
        self.data_all = self.channel_names + self.label_names
        # self.aux_prefs = ['ndvi_2018_', 'CHM_']
        self.detchm=0 # for det chm use /extracted_data_2aux_test_v4_centroids_all_classes_final_detchm/
        self.trained_model_paths = [
                                    './saved_models/segcountdensity/trees_20210620-0202_Adam_e4_redgreenblue_256_84_frames_weightmapTversky_MSE100_5weight_complex5.h5'
                                   ]
        
        # Output related variables
        self.output_dir = './test_check/'#'/home/sizhuo/Desktop/code_repository/TreeCountSegHeight-main/example_extracted_data/'
        self.operator = 'MAX' 
        self.output_image_type = '.tif' #'.png'
        self.outputseg_prefix = 'seg'
        self.outputdens_prefix = 'density'
        self.overwrite_analysed_files = False
        self.output_dtype='float32'
        self.multires = False # False for detchm
        self.single_raster = False
        self.inputBN = False
        self.input_size = 256
        self.input_shape = (self.input_size, self.input_size, len(self.channel_names))
        self.input_label_channel = [self.data_all]
        self.aux_data = False # True for detchm
        self.BATCH_SIZE = 8 # Depends upon GPU memory and WIDTH and HEIGHT (Note: Batch_size for prediction can be different then for training.
        self.WIDTH=256 # Should be same as the WIDTH used for training the model
        self.HEIGHT=256 # Should be same as the HEIGHT used for training the model
        self.STRIDE=196 #224 (a bit overlap) or 196   # STRIDE = WIDTH means no overlap, STRIDE = WIDTH/2 means 50 % overlap in prediction
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
