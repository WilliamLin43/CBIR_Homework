#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 00:31:37 2019

@author: uditya
"""

import ColorDescriptor
import Searcher
import argparse
import cv2

# creating the argument parser and parsing the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True, help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True, help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = True, help = "Path to the result path")
args = vars(ap.parse_args())


#intializing the color descriptor
cd = ColorDescriptor.ColorDescriptor((8,12,3))

#loading the query image and describe it
query = cv2.imread(args["query"])

queryFeatures = cd.describe(query)

#performing the search
s1 = Searcher.Searcher(args["index"])

results = s1.search(queryFeatures)

#print(results)

#displaying the query
cv2.imshow("Query",query)
cv2.waitKey(0)

#loop over the results
i = 1
for (score, resultID) in results:
    #load the result image and display it
    resultID = resultID.replace("\\","/")
    print(resultID)
    Image = cv2.imread(resultID)
    cv2.imshow("Result",Image)
    cv2.waitKey(0)
    
    cv2.imwrite(args["result_path"] + "/" +str(i)+"_" + resultID[9:], Image)
    
    result1 = cv2.imread(args["result_path"] + "/"+str(i)+"_"  + resultID[9:])
    result = cv2.resize(result1,(300,300))
    cv2.imshow("Result",result)
    cv2.waitKey(0)
    i += 1
