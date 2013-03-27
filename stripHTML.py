#########################################
### stripHTML.py
### written by Katie Malone (cmmalone.158@gmail.com)
### started 27 March 2013
### to run: $> python stripHTML.py
#########################################


import re


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
                print



if __name__=="__main__":
    main()
