#########################################
### interface.py
### written by Katie Malone (cmmalone.158@gmail.com)
### started 15 April 2013 
### run via veniVidiVino.py
#########################################


import sys
import growHarvestPress
import pickle

def interface(wine_list):
    desired_wine = raw_input("What wine would you like a pairing for? ")
    desired_wine = desired_wine.lower()
    print "you entered ", desired_wine

    wine_names = []
    for wine in wine_list:
        wine_names.append( wine.name )

    if desired_wine in wine_names:
        print "this is a wine that appears in the training set"
        print "here's what the training data recommends for pairing: " 
        for wine in wine_list:
            if wine.name == desired_wine:
                print wine.pairing 

    else:
        print "that wine is not in the training set" 
        wine_tree = pickle.load( open("train/tree.p", "rb") )
        if desired_wine in wine_tree:
            print "but it is in the tree!"
