#########################################
### growHarvestPress.py
### written by Katie Malone (cmmalone.158@gmail.com)
### started 27 March 2013
### run via veniVidiVino.py
#########################################


import re
import copy
from scipy.sparse import lil_matrix
from stemming.porter2 import stem
from bottleLabel import bottleLabel


def dictionarizeTerms( wine_list ):
    ### store all the words in the description in a dictionary
    ### with entries of the form 'term':(index, counts)
    term_dictionary = {}
    term_index   = 1
    for wine in wine_list:
        if not wine.description == None:
            description = wine.description
            words = description.split(" ")
            for word in words:   ### strip away trailing punctuation
                words_2 = word.split("&")
                if ( len( words_2 )>1 and words_2[0] != '' ):
                    word = words_2[0]
                if word[-1] in ['.', ',', ';']:
                    word = word[:-1]
                word = word.lower()
                word = stem(word)
                ### add a new term to the dictionary
                if word not in term_dictionary.keys(): 
                    term_dictionary[word] = (term_index, 1)
                    term_index += 1
                ### increment the count for a term already in the dictionary
                else:
                    term_params = term_dictionary[word]
                    counter = term_params[1]
                    counter += 1
                    term_dictionary[word] = (term_params[0], counter)
    print term_dictionary


def tagStrip( string ):
    ### get rid of opening <strong> tags, where present
    if string[0:8] == "<strong>":
        string = string[8:]
    
        ### separate feature from contents, e.g. Oak: heavy ==> [Oak, heavy]
        feature_and_contents = string.split(":")
        if len(feature_and_contents) > 1:
            feature_and_contents[0] = feature_and_contents[0][0:-9]
            feature = feature_and_contents[0]
            contents = feature_and_contents[1]
            
            if feature == "Comparable</strong> <strong>Wines":
                feature = "Comparable Wines"
            if contents[0:6] == "&nbsp;" :
                contents = contents[6:]
            ### hacks for the wine description            

            #print feature
            return contents
        else:  ### these are the names (they don't have [feature, contents] form)
            return feature_and_contents[0]
    
    else:
        description = string[13:-1]
        return description


def processHTML():
    red_in = open("train/red_train.html", "rU")
    white_in = open("train/white_train.html", "rU")


    menu = []
    for line in red_in.readlines():
        ### the descriptions are all in a huge one-line block
        ### split roughly on the <font size="5"> html tag
        wines_list = line.split('<font size="5">')

        if len(wines_list)>1:
            for entry in wines_list:
 
                ### regexes to identify the different features in each entry
                name_str = re.search(r"<strong>[\w\s]+", entry)
                aging_str = re.search(r"<strong>Aging</strong>:[\w\s-]+", entry)
                comparable_wines_str = re.search(r"<strong>Comparable</strong> <strong>Wines</strong>:&nbsp; [\w\s,]+", entry)
                pairing_str = re.search(r"<strong>Pairing</strong>: [\w\s\.,]+", entry)
                body_str = re.search(r"<strong>Body</strong>: [\w\s,]+", entry)
                oak_str = re.search(r"<strong>Oak</strong>: [\w\s]+", entry)
                description_str = re.search(r"</font><br />[\w\s\.,:&;-]+", entry)

                ### the features are separated but still hold some html tags
                ### post-process to strip away tags and stuff 
                bL = bottleLabel()
                if name_str:
                    bL.name = tagStrip( name_str.group() )
                if aging_str:
                    bL.aging = tagStrip( aging_str.group() )
                if comparable_wines_str:
                    bL.comparable_wines = tagStrip( comparable_wines_str.group() )
                if pairing_str:
                    bL.pairing = tagStrip( pairing_str.group() )
                if body_str:
                    bL.body = tagStrip( body_str.group() )
                if oak_str:
                    bL.oak = tagStrip( oak_str.group() )
                if description_str:
                    bL.description = tagStrip( description_str.group() )
#                print bL.name
#                print bL.description
                menu.append( copy.deepcopy(bL) )
    return menu

