#########################################
### vineAndBranches.py
### written by Katie Malone (cmmalone.158@gmail.com)
### started 4 April 2013
### to run: $> python vineAndBranches.py
#########################################


import pickle
import networkx as nx
import matplotlib.pyplot as plt


def printTree( g, name ):
    from networkx import graphviz_layout
    pos=nx.graphviz_layout(g, prog='twopi', args='')
    plt.figure(figsize=(100,100))
    nx.draw(g, pos,node_size=6000, alpha=0.5, node_color="blue", with_labels=True)
    plt.axis('equal')
    plt.savefig(name)
   
def addWines( g, parent_node, wine_list ):
    edge_list = list()
    for wine in wine_list:
        edge_list.append((parent_node, wine))
    g.add_edges_from(edge_list)


def chainWines( g, wine_chain, wine_list, wine_weight):
    end = len(wine_chain) - 1
    for i in range(1, end + 1):
        g.add_edge(wine_chain[i-1], wine_chain[i], weight = wine_weight)
        wine_weight = wine_weight - 1.0
    addWines (g, wine_chain[end], wine_list )


def AddClayCuredMeats( g ):
    g.add_edge('savory red', 'clay cured meats', weight = 3.0)
    g.add_edge('clay cured meats', 'high tannin ccm', weight = 2.0)
    g.add_edge('clay cured meats', 'round ccm', weight = 2.0)
    
    addWines (g, 'high tannin ccm', ['barolo',  'barbaresco', 'montefalco rosso', 'chianti'] )
    addWines (g, 'round ccm', ['vacqueyras', 'carignan', 'gigondas', 'brunello di montalcino'] )
 

def AddTruffleForest( g ):
    g.add_edge('savory red', 'truffle forest', weight = 3.0)
    g.add_edge('truffle forest', 'round tf', weight = 2.0)
    g.add_edge('truffle forest', 'spicy juicy tf', weight = 2.0)

    addWines (g, 'round tf', ['cote chalonnaise', 'bourgogne', 'dolcetto'] )
    addWines (g, 'spicy juicy tf', ['pinotage', 'beaujolais'] )

def AddSmokeTobaccoLeather( g ):
    g.add_edge('savory red', 'smoke tobacco leather', weight = 3.0)
    g.add_edge('smoke tobacco leather', 'high tannin stl', weight = 2.0)
    g.add_edge('smoke tobacco leather', 'round stl', weight = 2.0)

    addWines (g, 'high tannin stl', ['taurasi', 'cahors', 'rioja', 'aglianico'] )
    addWines (g, 'round stl', ['ribera del duero', 'graves', 'pessac-leognan', 'gran reserva', 'cornas', 'cannonau'] )


def main():
    """
        Recreates the wine network structure found here:
        http://winefolly.com/review/different-types-of-wine/
    """    

    g = nx.DiGraph()

    #g.add_edge('red', 'white', weight=5.0)


    ################################################################ reds
    
    g.add_edge('wine', 'red', weight=5.0)
 
    g.add_edge('red', 'savory red', weight = 4.0)
    AddClayCuredMeats( g )
    AddTruffleForest( g )
    AddSmokeTobaccoLeather( g )

    chainWines( g, ['red', 'savory red', 'black pepper gravel', 'high tannin bpg'], ['cahors', 'st. julien', 'pauillac', 'st. estephe', 'haut medoc', 'medoc'], wine_weight = 4.0)
    chainWines( g, ['red', 'savory red', 'black pepper gravel', 'spicy juicy bpg'], ['chinon', 'montepulciano', 'bardolino', 'barbera dalba', 'bourgueil'], wine_weight = 4.0)
    chainWines( g, ['red', 'savory red', 'black pepper gravel', 'round bpg'], ['rhone', 'st. joseph', 'fronsac', 'cotes de castillon', 'bandol', 'hermitage', 'st. emilion', 'pomerol'], wine_weight = 4.0)

    g.add_edge('red', 'sweet red', weight = 4.0)
    addWines( g, 'sweet red', ['some bulk wines', 'recioto della valpolicella', 'occhio di pernice'])

    #g.add_edge('red', 'fruity red', weight = 4.0)

    chainWines( g, ['red', 'fruity red', 'tart cherry cranberry', 'spicy juicy tcc'], ['blaufrankisch', 'gamay', 'zweigelt'], wine_weight = 4.0)
    chainWines( g, ['red', 'fruity red', 'tart cherry cranberry', 'round tcc'], ['oregon pinot noir', 'spatburgunder', 'st. laurent'], wine_weight = 4.0)

    chainWines( g, ['red', 'fruity red', 'strawberry cherry', 'spicy sc'], ['counoise', 'carmenere', 'zinfandel', 'primitivo', 'barbera', 'grenache'], wine_weight = 4.0)
    chainWines( g, ['red', 'fruity red', 'strawberry cherry', 'round sc'], ['cites dy rgibe', 'california pinot noir', 'chile pinot noir', 'new zealand pino noir'], wine_weight = 4.0)

    chainWines( g, ['red', 'fruity red', 'black cherry raspberry', 'spicy bcr'], ['cabernet franc', 'sangiovese'], wine_weight = 4.0)
    chainWines( g, ['red', 'fruity red', 'black cherry raspberry', 'round bcr'], ['merlot', 'valpolicella', 'chateauneuf du pape', 'amarone'], wine_weight = 4.0)
    chainWines( g, ['red', 'fruity red', 'black cherry raspberry', 'high tannin bcr'], ['tempranillo', 'priorat', 'cabernet sauvignon', 'super tuscan'], wine_weight = 4.0)




    ################################################################ whites
    g.add_edge('wine', 'white', weight=5.0)

    chainWines( g, ['white', 'dry white', 'light grapefruit floral'], ['vermentino', 'moschofilero', 'verdicchio', 'orbieto', 'pinot blanc', 'greco di tufo'], wine_weight = 4.0 )
    chainWines( g, ['white', 'dry white', 'light citrus lemon'], ['grenache blanc', 'pino grigio', 'albarino', 'gruner veltliner', 'chablis', 'picpoul', 'unoaked chardonnay', 'vinho verde', 'muscadet', 'assyrtiko', 'silvaner'], wine_weight = 4.0 )
    chainWines( g, ['white', 'dry white', 'light herbal grassy'], ['verdejo', 'cheverny', 'sauvignon blanc', 'touraine', 'ugni blanc', 'sancerre', 'white bordeaux', 'pouilly fume', 'entre-deux-mers'], wine_weight = 4.0 )
    chainWines( g, ['white', 'dry white', 'rich creamy nutty'], ['chardonnay', 'montrachet', 'macconais', 'soave', 'white bordeaux', 'savennieres', 'viognier', 'cote de beaune', 'meursault'], wine_weight = 4.0 )
    chainWines( g, ['white', 'dry white', 'medium perfume floral'], ['semillon', 'marsanne', 'fiano', 'tokaji dry', 'viognier', 'chenin blanc', 'roussanne', 'condrieu', 'malvasia dry', 'vouvray', 'torrontes'], wine_weight = 4.0 )


    chainWines( g, ['white', 'sweet white', 'rich tropical honey'], ['tokaji 3-6 puttonyos', 'moscato', 'orvieto abbroccato', 'sauternes', 'riesling auslese', 'malvasia', 'chenin blanc moelleux', 'late harvest'],  wine_weight = 4.0 )
    chainWines( g, ['white', 'sweet white', 'off-dry apricots peaches'], ['cour-cheverny', 'chenin blanc', 'muller-thurgau', 'gewurtztraminer', 'vouvray', 'riesling kabinett', 'riesling spatlese'],  wine_weight = 4.0 )




    ################################################################ roses
    g.add_edge('wine', 'rose', weight=5.0)

    chainWines( g, ['rose', 'dry rose', 'savory meaty dr'], ['loire rose', 'bandol rose', 'cabernet franc rose', 'syrah rose', 'caberneet sauvignon rose'], wine_weight = 4.0)
    chainWines( g, ['rose', 'dry rose', 'fruity floral dr'], ['pinot noir rose', 'grenache rose', 'provence rose', 'sangiovese rose', 'rosado', 'tavel'], wine_weight = 4.0)
    chainWines( g, ['rose', 'semi-sweet rose'], ['blush wine', 'garnacha rosado', 'rose danjou', 'vin gris', 'white zinfandel', 'white merlot'], wine_weight = 4.0)


    ################################################################ sparklings
    g.add_edge('wine', 'sparkling wine', weight=5.0)

    chainWines( g, ['sparkling wine', 'white sparkling wines', 'dry creamy rich'], ['vintage champagne', 'blanc de noirs', 'blanc de blancs', 'vintage franciacorta', 'vintage sparkling wine'], wine_weight = 4.0 )
    chainWines( g, ['sparkling wine', 'white sparkling wines', 'dry light citrus'], ['prosecco extra-brut', 'blanc de blancs', 'extra-brut', 'cava', 'sec', 'brut nature', 'non-vintage champagne (brut)'], wine_weight = 4.0 )
    chainWines( g, ['sparkling wine', 'white sparkling wines', 'semi-sweet floral'], ['champagne extra dry', 'prosecco', 'sparkling riesling', 'moscato', 'vouvray (mousseux)'], wine_weight = 4.0 )
    chainWines( g, ['sparkling wine', 'white sparkling wines', 'sweet apricots rich'], ['asti spumante', 'doux', 'demi-sec', 'valdobbiadene', 'spumante', 'moscato dasti'], wine_weight = 4.0 )


    chainWines( g, ['sparkling wine', 'red sparkling wines', 'semi-sweet raspberry cherry'], ['lambrusco amabile', 'brachetto dacqui'], wine_weight = 4.0 )
    chainWines( g, ['sparkling wine', 'red sparkling wines', 'sweet blueberry cherry'], ['lambrusco dolce', 'lambrusco amabile'], wine_weight = 4.0 )
    chainWines( g, ['sparkling wine', 'red sparkling wines', 'dry raspberry blueberry'], ['sparkling shiraz', 'lambrusco secco', 'lambrusco spumante'], wine_weight = 4.0 )

    chainWines( g, ['sparkling wine', 'rose sparkling wines', 'dry strawberry light'], ['rose champagne', 'rose sparkling wine', 'cava brut rose'], wine_weight = 4.0 )
    chainWines( g, ['sparkling wine', 'rose sparkling wines', 'semi-sweet strawberry orange'], ['moscato rose', 'brachetto dacqui rose', 'cava rose'], wine_weight = 4.0 )

   ################################################################ fortified wine
    g.add_edge('wine', 'fortified wine', weight=5.0)

    chainWines( g, ['fortified wine', 'red fortified'], ['vintage port', 'ruby port', 'LBV port', 'banyuls', 'maury', 'rasteau'], wine_weight = 4.0)
    chainWines( g, ['fortified wine', 'white fortified'], ['muscat de frontignan', 'muscat de beaumes de venise', 'muscat de rivesaltes'], wine_weight = 4.0)
    chainWines( g, ['fortified wine', 'nutty fortified', 'sweet nutty'], ['montilla-moriles', 'vin santo', 'cream sherry', 'tawny port', 'moscatel de setubal'], wine_weight = 4.0)
    chainWines( g, ['fortified wine', 'nutty fortified', 'dry semi-sweet nutty'], ['fino sherry', 'oloroso sherry', 'madeira', 'amontillado sherry', 'marsala'], wine_weight = 4.0)
   
    
    
    
    printTree( g, 'train/treeCheck.png' )

 



#    g.add_edge('savory red', 'black pepper gravel', weight = 3.0)
#
#    g.add_edge('black pepper gravel', 'high tannin bpg', weight = 2.0)
#    g.add_edge('black pepper gravel', 'spicy juicy bpg', weight = 2.0)
#    g.add_edge('black pepper gravel', 'round bpg', weight = 2.0)
#
#    g.add_edge('fruity red', 'tart cherry cranberry', weight = 3.0)
#    g.add_edge('fruity red', 'strawberry cherry', weight = 3.0)
#    g.add_edge('fruity red', 'black cherry raspberry', weight = 3.0)
#    g.add_edge('fruity red', 'blueberry blackberry', weight = 3.0)

    #print(g.nodes())
    #nx.draw(g) 
    #plt.show()

   # wines_in_tree = [k for k,v in g.out_degree().iteritems() if v==0]

    #for vino in wines_in_tree:
     #   print vino 

    pickle.dump( g, open("train/tree.p", "wb") )

#    pickle.dump( wines_in_tree, open("train/tree.p", "wb") )
    #return wines_in_tree


if __name__=="__main__":
    main()
