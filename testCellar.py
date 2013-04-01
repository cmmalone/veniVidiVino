#########################################
### testCellar.py
### written by Katie Malone (cmmalone.158@gmail.com)
### started 30 March 2013
### currently standalone 
#########################################

import bottleLabel

import urllib
from bs4 import BeautifulSoup


def soupWine():

    test_whites = urllib.urlopen("http://www.frenchwinesfood.com/SolAuRaisin/CepagesBlancs.aspx")
    test_reds   = urllib.urlopen("http://www.frenchwinesfood.com/solauraisin/cepages.aspx")
    test_cellar = []

    white_soup = BeautifulSoup( test_whites.read() )
    white_name = white_soup.findAll('h1')
    white_description = white_soup.findAll('p', attrs = {'class':'Description'} )

    red_soup = BeautifulSoup( test_reds.read() )
    red_name = red_soup.findAll('h1')
    red_description = red_soup.findAll('p', attrs = {'class':'Description'} )

    for color_soup in [red_soup, white_soup]:
        names = color_soup.findAll('h1')
        descriptions = color_soup.findAll('p', attrs = {'class':'Description'} )
        for i in range(0, len(names)):
            name = (str(names[i]).split('</a>'))[-1][:-5]
            description = descriptions[i]
            bL = bottleLabel.bottleLabel()
            bL.name = str(name).lower()
            bL.description = str(description).lower()
            test_cellar.append( bL )

    return test_cellar


#if __name__ == '__main__':
#    main()
