##
#  Implementations of L-systems.
##

from rewrite import rewrite

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
    rules = {'a':'cRb', 'e':'f', 'i':'j', 'm':'fDg', 'b':'aDi', 'f':'hRh',
            'j':'gRk', 'c':'d' ,'g':'g' ,'k':'lDl' ,'d':'eDg' ,'h':'m' ,'l':'j'}
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

def tree(levels):
    axiom = 'F'
    rules = {'F': 'F[+F]F[-F[+F][-F]]F'}
    return rewrite(axiom, rules, levels)
    
def tree2(levels):
    axiom = 'F'
    rules = {'F': 'F[-FF]F[+F[-F]F]F'}
    return rewrite(axiom, rules, levels)

def triangles(levels):
    axiom = 'l'
    rules = {'l': 'FlFrF-', 'r':'-FlFrF'}
    return rewrite(axiom, rules, levels)
    
def sierpinski(levels):
    axiom = 'a'
    rules = {'a': 'b-a-b', 'b':'a+b+a'}
    return rewrite(axiom, rules, levels)
    

