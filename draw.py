import turtle as t
import rewrite as rw

def koch_fractal(levels=2):
    axiom = 'f'
    production_rules = {'f': 'f+f--f+f'}
    step = 300/(3**levels)
    for i in range(levels):
        axiom = rw.rewrite(axiom, production_rules)
    draw(axiom, step)

def draw(sequence, step):
    for s in sequence:
        if s is 'f': t.forward(step)
        if s is '+': t.right(60)
        if s is '-': t.left(60)

if __name__=="__main__":
    koch_fractal(1)
    raw_input('Press return to end')
