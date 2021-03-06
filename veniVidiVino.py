#########################################
### veniVidiVino.py
### written by Katie Malone (cmmalone.158@gmail.com)
### started 29 March 2013
### to run: $> python veniVidiVino.py 
#########################################

import growHarvestPress
import testCellar
import interface

import numpy
import scipy
import sklearn
import pickle

def main():

    wine_list = pickle.load( open("train/training_cellar.p", "rb") ) 
    interface.interface(wine_list)

    growHarvestPress.dictionarizeTerms( wine_list )


#    test_list = testCellar.soupWine()
#    growHarvestPress.dictionarizeTerms( test_list )


if __name__=="__main__":
    main()
