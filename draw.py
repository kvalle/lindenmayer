import rewrite
import turtle as t

def draw(sequence, position=(0,0), heading=0, step_length=30, angle_increment=60):
    t.up()
    t.goto(position)
    t.right(heading)
    t.down()
    for s in sequence:
        if s is 'F':
            t.forward(step_length)
        elif s is 'f':
            t.up()
            t.forward(step_length)
            t.down()
        elif s is '+':
            t.left(angle_increment)
        elif s is '-':
            t.right(angle_increment)
        else:
            print "Symbol '"+ s +"' ignored because it was not recognized by the turtle!'"

def demo_koch(level = 3):
    fractal = rewrite.koch_fractal(level)
    step = 300/(3**level)
    draw(fractal, position=(-200,0),step_length=step, angle_increment=60)
    raw_input('Press return to end')

def demo_quadratic_koch(level=2):
    t.speed(10)
    fractal = rewrite.quadratic_koch_fractal(level)
    step = 100/(5*level+1)
    draw(fractal,step_length=step, angle_increment=90)
    raw_input('Press return to end')

if __name__=="__main__":
    demo_quadratic_koch()
