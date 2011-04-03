import rewrite
import turtle as t

def draw(sequence, position=(0,0), heading=0, step_length=30, angle_increment=60):
    t.up()
    t.goto(position)
    t.right(heading)
    t.down()
    for s in sequence:
        if s is 'f': t.forward(step_length)
        if s is '+': t.right(angle_increment)
        if s is '-': t.left(angle_increment)

def demo_koch():
    level = 3
    fractal = rewrite.koch_fractal(level)
    step = 300/(3**level)
    draw(fractal, position=(-200,0),step_length=step, angle_increment=60)

if __name__=="__main__":
    demo_koch()
    raw_input('Press return to end')
