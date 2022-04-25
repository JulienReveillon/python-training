#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 16:26:32 2021

@author: julienreveillon
"""


import os

def findFile(filename, search_path):
   result = []

   for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   return result

print(findFile('deces.csv','/Users/julienreveillon'))