import rewrite
import turtle as t

class Turtle():
    def __init__(self, position=(0,0), heading=0, step=30, angle=60):
        self.turtle = t.Turtle()
        self.position = position
        self.heading = heading
        self.step = step
        self.angle = angle
        self.states = []
        self.setup()

    def setup(self):
        self.turtle.clear()
        self.turtle.up()
        self.turtle.goto(self.position)
        self.turtle.right(self.heading)
        self.turtle.down()

    def save_state(self):
        p = self.turtle.position()
        h = self.turtle.heading()
        self.states.append((p,h))

    def restore_state(self):
        if not self.states:
            raise Exception('No states to restore from!')
        p,h = self.states[-1]
        self.turtle.up()
        self.turtle.goto(p)
        self.turtle.setheading(h)
        self.turtle.down()
        self.states = self.states[:-1]

    def draw(self, sequence):
        for s in sequence:
            if s is 'F':
                self.turtle.forward(self.step)
            elif s is 'f':
                self.turtle.up()
                self.turtle.forward(self.step)
                self.turtle.down()
            elif s is '+':
                self.turtle.left(self.angle)
            elif s is '-':
                self.turtle.right(self.angle)
            elif s is '[':
                self.save_state()
            elif s  is ']':
                self.restore_state()
            else:
                print "Symbol '"+ s +"' ignored because it was not recognized by the turtle!'"

def demo_koch(level = 3):
    fractal = rewrite.koch_fractal(level)
    step = 300/(3**level)
    koopa = Turtle(position=(-200,0),step=step, angle=60)
    koopa.draw(fractal)
    raw_input('Press return to end')

def demo_quadratic_koch(level=2):
    fractal = rewrite.quadratic_koch_fractal(level)
    step = 100/(5*level+1)
    koopa = Turtle(step=step, angle=90)
    koopa.draw(fractal)
    raw_input('Press return to end')

def demo_tree():
    axiom = 'F'
    rules = {'F': 'F[+F]F[-F[+F][-F]]F'}
    tree = rewrite.rewrite_iter(axiom, rules, 3)
    koopa = Turtle(position=(0,-250),step=12, angle=29, heading=270)
    koopa.draw(tree)
    raw_input('Press return to end')

if __name__=="__main__":
    #~ demo_koch()
    #~ demo_quadratic_koch()
    demo_tree()
