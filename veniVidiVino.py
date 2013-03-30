#########################################
### veniVidiVino.py
### written by Katie Malone (cmmalone.158@gmail.com)
### started 29 March 2013
### to run: $> python veniVidiVino.py 
#########################################

import growHarvestPress

import numpy
import scipy
import sklearn

def main():
    wine_list = growHarvestPress.processHTML()

#    for wine in wine_list[1:]:
#        print wine.name
#        print wine.description

    growHarvestPress.dictionarizeTerms( wine_list )


if __name__=="__main__":
    main()
