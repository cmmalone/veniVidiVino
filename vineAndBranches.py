#########################################
### vineAndBranches.py
### written by Katie Malone (cmmalone.158@gmail.com)
### started 4 April 2013
### to run: $> python vineAndBranches.py
#########################################


import networkx as nx
import matplotlib.pyplot as plt


def AddClayCuredMeats( g ):
    g.add_edge('savory red', 'clay cured meats', weight = 3.0)
    g.add_edge('clay cured meats', 'high tannin ccm', weight = 2.0)
    g.add_edge('clay cured meats', 'round ccm', weight = 2.0)
    
    def AddHighTanninCCM( g ):
        g.add_edges_from( [('high tannin ccm', 'barolo'),
                           ('high tannin ccm', 'barbaresco'),
                           ('high tannin ccm', 'montefalco rosso'),
                           ('high tannin ccm', 'chianti') ] )
    def AddRoundCCM( g ):
        g.add_edges_from( [('round ccm', 'vacqueyras'),
                           ('round ccm', 'carignan'),
                           ('round ccm', 'gigondas'),
                           ('round ccm', 'brunello di montalcino') ] )
    AddHighTanninCCM( g )
    AddRoundCCM( g ) 



def AddTruffleForest( g ):
    g.add_edge('savory red', 'truffle forest', weight = 3.0)
    g.add_edge('truffle forest', 'round tf', weight = 2.0)
    g.add_edge('truffle forest', 'spicy juicy tf', weight = 2.0)
    def AddRoundTF( g ):
        g.add_edges_from( [('round tf', 'cote chalonnaise'),
                           ('round tf', 'bourgogne'),
                           ('round tf', 'dolcetto') ] )
    def AddSpicyJuicyTF( g ):
        g.add_edges_from( [('spicy juicy tf', 'pinotage'),
                           ('spicy juicy tf', 'beaujolais') ] )
    AddRoundTF( g )
    AddSpicyJuicyTF( g )

def AddSmokeTobaccoLeather( g ):
    g.add_edge('savory red', 'smoke tobacco leather', weight = 3.0)
    g.add_edge('smoke tobacco leather', 'high tannin stl', weight = 2.0)
    g.add_edge('smoke tobacco leather', 'round stl', weight = 2.0)
    def AddHighTanninSTL( g ):
        g.add_edges_from( [('high tannin stl', 'taurasi'),
                           ('high tannin stl', 'cahors'),
                           ('high tannin stl', 'rioja'),
                           ('high tannin stl', 'aglianico') ] )
    def AddRoundSTL( g ):
        g.add_edges_from( [('round stl', 'ribera del duero'),
                           ('round stl', 'graves'),
                           ('round stl', 'pessac-leognan'),
                           ('round stl', 'gran reserva'),
                           ('round stl', 'cornas'),
                           ('round stl', 'cannonau') ] )
    AddHighTanninSTL( g )
    AddRoundSTL( g )

 

def main():
    """
        Recreates the wine network structure found here:
        http://winefolly.com/review/different-types-of-wine/
    """    

    g = nx.Graph()

    g.add_edge('red', 'white', weight=5.0)
    
    g.add_edge('red', 'savory red', weight = 4.0)
    g.add_edge('red', 'sweet red', weight = 4.0)
    g.add_edge('red', 'fruity red', weight = 4.0)

    AddClayCuredMeats( g )
    AddTruffleForest( g )
    AddSmokeTobaccoLeather( g )


    g.add_edge('savory red', 'black pepper gravel', weight = 3.0)




    g.add_edge('black pepper gravel', 'high tannin bpg', weight = 2.0)
    g.add_edge('black pepper gravel', 'spicy juicy bpg', weight = 2.0)
    g.add_edge('black pepper gravel', 'round bpg', weight = 2.0)


 

    g.add_edge('fruity red', 'tart cherry cranberry', weight = 3.0)
    g.add_edge('fruity red', 'strawberry cherry', weight = 3.0)
    g.add_edge('fruity red', 'black cherry raspberry', weight = 3.0)
    g.add_edge('fruity red', 'blueberry blackberry', weight = 3.0)


    nx.draw(g) 
    plt.show()


if __name__=="__main__":
    main()
