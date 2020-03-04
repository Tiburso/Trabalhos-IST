def baralho():
    deck = []
    nipes = ['esp', 'copas', 'ouros', 'paus']
    valor = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    for i in nipes:
        for i_ in valor:
            dc = {}
            dc['np'] = i
            dc['vlr'] = i_
            deck += [dc]
    return deck
    