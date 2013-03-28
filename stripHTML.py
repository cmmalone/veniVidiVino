#########################################
### stripHTML.py
### written by Katie Malone (cmmalone.158@gmail.com)
### started 27 March 2013
### to run: $> python stripHTML.py
#########################################


import re


def tagStrip( string ):
    ### get rid of opening <strong> tags, where present
    if string[0:8] == "<strong>":
        string = string[8:]
#        print string
    
        ### separate feature from description, e.g. Oak: heavy ==> [Oak, heavy]
        feature_and_description = string.split(":")
        if len(feature_and_description) > 1:
            feature_and_description[0] = feature_and_description[0][0:-9]
            feature = feature_and_description[0]
            description = feature_and_description[1]
            print feature
            print description
            print


def main():
    red_in = open("train/red_train.html", "rU")
    white_in = open("train/white_train.html", "rU")


    for line in red_in.readlines():
        ### the descriptions are all in a huge one-line block
        ### split roughly on the <font size="5"> html tag
        wines_list = line.split('<font size="5">')

        if len(wines_list)>1:
            for entry in wines_list:
                print entry
            
                ### regexes to identify the different features in each entry
                name_str = re.search(r"<strong>[\w\s]+", entry)
                aging_str = re.search(r"<strong>Aging</strong>:[\w\s-]+", entry)
                comparable_wines_str = re.search(r"<strong>Comparable</strong> <strong>Wines</strong>:&nbsp; [\w\s,]+", entry)
                pairing_str = re.search(r"<strong>Pairing</strong>: [\w\s\.,]+", entry)
                body_str = re.search(r"<strong>Body</strong>: [\w\s,]+", entry)
                oak_str = re.search(r"<strong>Oak</strong>: [\w\s]+", entry)
                description_str = re.search(r"</font><br />[\w\s\.,:&;]+", entry)

                ### the features are separated but still hold some html tags
                ### post-process to strip away tags and stuff 
                if name_str:
                    tagStrip( name_str.group() )
                if aging_str:
                    tagStrip( aging_str.group() ) 
                if comparable_wines_str:
                    tagStrip( comparable_wines_str.group() )
                if pairing_str:
                    tagStrip( pairing_str.group() )
                if body_str:
                    tagStrip( body_str.group() )
                if oak_str:
                    tagStrip( oak_str.group() )
                if description_str:
                    tagStrip( description_str.group() )
                print



if __name__=="__main__":
    main()
