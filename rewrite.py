##
#  Rewriting system
##

def rewrite_once(axiom, rules):
    i = 0
    while i < len(axiom):
        x = axiom[i]
        if x in rules.keys():
            index = i + axiom[i:].index(x)
            axiom = axiom[:index]+rules[x]+axiom[index+1:]
            i += len(rules[x])
            continue
        i += 1
    return axiom

def rewrite(axiom, rules, max_itr=None):
    """Warning: Termination not guaranteed!"""
    itr = 0
    while not max_itr or itr<max_itr:
        itr += 1
        tmp = rewrite_once(axiom, rules)
        if tmp==axiom: break
        axiom = tmp
    return axiom

##
#  Generators
##

def koch_fractal(levels):
    axiom = 'F'
    production_rules = {'F': 'F+F--F+F'}
    return rewrite(axiom, production_rules, levels)

def quadratic_koch_fractal(levels):
    axiom = 'F+F+F+F'
    production_rules = {'F': 'F+F-F-FF+F+F-F'}
    return rewrite(axiom, production_rules, levels)

def lindenmayer_leaf(depth):
    """
    Generator for Lindernmayer's moss leaf L-system. See example
    in [1] on page 275.

    [1] Floreano, D. and Mattiussi, C., 2008, Bio-inspired Artificial Intelligence
    """
    axiom = 'a'
    rules = {'a':'cRb','e':'f','i':'j','m':'fDg','b':'aDi','f':'hRh',
            'j':'gRk','c':'d','g':'g','k':'lDl','d':'eDg','h':'m','l':'j'}
    return rewrite(axiom, rules, depth)

def shroom_fractal(levels):
    axiom = 'a-b'
    rules = {'a': 'b+a-b', 'b':'a-b+a'}
    return rewrite(axiom, rules, levels)

def hilbert_fractal(levels):
    axiom = 'a'
    rules = {'a': '+bF-aFa-Fb+',
             'b': '-aF+bFb+Fa-'}
    return rewrite(axiom, rules, levels)

if __name__=="__main__":
    pass
