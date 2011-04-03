import rewrite
import turtle as t

def draw(sequence, step):
    for s in sequence:
        if s is 'f': t.forward(step)
        if s is '+': t.right(60)
        if s is '-': t.left(60)

def demo_koch():
    level = 3
    fractal = rewrite.koch_fractal(level)
    step = 300/(3**level)
    draw(fractal, step)

if __name__=="__main__":
    demo_koch()
    raw_input('Press return to end')
