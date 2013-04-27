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
        #wine_tree = pickle.load( open("train/tree.p", "rb") )
        #if desired_wine in wine_tree:
         #   print "but it is in the tree!"
        wine_tree = pickle.load( open("train/tree.p", "rb") )
        if wine_tree.has_node( desired_wine ):
            print "but it is in the tree!"
            
            parent_node = wine_tree.predecessors(desired_wine)[0]

            while (len(wine_tree.edges(parent_node)) == 1):
                parent_node = wine_tree.predecessors(parent_node)[0]

            print desired_wine.title(), "is similar to the following wines and pairings:"

            for vino in wine_tree.successors(parent_node):
                if vino in wine_names:
                    for vin in wine_list:
                        if vino == vin.name:
                            print "   ", vin.name.title(), ":", vin.pairing
                            
          
        else:
            if raw_input("Would you like to describe the wine? (yes or no) ") == "no":
                print "If you drink enough of it, it won't matter what you pair it with I guess."
            else:
                wine_leaves = [k for k,v in wine_tree.out_degree().iteritems() if v==0]
                option_level = 'wine'
                option_list = wine_tree.successors(option_level)
                while(len(option_list) > 0):
                    print "Options:"
                    for option in option_list:
                        print "   ", option
                    option_level = raw_input('Choose an option ')
                    option_list = wine_tree.successors(option_level)
                    if(set(option_list).intersection(set(wine_leaves))):
                        break
                
                print "Your wine is similar to the following wines and pairings:"
                for vino in wine_tree.successors(option_level):
                    if vino in wine_names:
                        for vin in wine_list:
                            if vino == vin.name:
                                print "   ", vin.name.title(), ":", vin.pairing
                                    
                #option_level

                 #for option in wine_tree.successors(raw_input()):
                  #   print option

#need to loop until we reach edges
                


