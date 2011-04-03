import rewrite
import turtle as t

class Turtle():
    def __init__(self, position=(0,0), heading=0, step=30, angle=60):
        self.position = position
        self.heading = heading
        self.step = step
        self.angle = angle
        self.setup()

    def setup(self):
        t.clear()
        t.up()
        t.goto(self.position)
        t.right(self.heading)
        t.down()

    def draw(self, sequence):
        for s in sequence:
            if s is 'F':
                t.forward(self.step)
            elif s is 'f':
                t.up()
                t.forward(self.step)
                t.down()
            elif s is '+':
                t.left(self.angle)
            elif s is '-':
                t.right(self.angle)
            else:
                print "Symbol '"+ s +"' ignored because it was not recognized by the turtle!'"

def demo_koch(level = 3):
    fractal = rewrite.koch_fractal(level)
    step = 300/(3**level)
    koopa = Turtle(position=(-200,0),step=step, angle=60)
    koopa.draw(fractal)
    raw_input('Press return to end')

def demo_quadratic_koch(level=2):
    t.speed(10)
    fractal = rewrite.quadratic_koch_fractal(level)
    step = 100/(5*level+1)
    koopa = Turtle(step=step, angle=90)
    koopa.draw(fractal)
    raw_input('Press return to end')

if __name__=="__main__":
    demo_koch()
    demo_quadratic_koch()
