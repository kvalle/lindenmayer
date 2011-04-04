import rewrite
import turtle as t

class KoopaTroopa(t.Turtle):
    def __init__(self, step=30, angle=60, position=(0,0), heading=0):
        super(KoopaTroopa, self).__init__()
        self._step = step
        self._angle = angle
        self._states = []
        self.up()
        self.goto(position)
        self.right(heading)
        self.down()

    def save_state(self):
        p = self.position()
        h = self.heading()
        self._states.append((p,h))

    def restore_state(self):
        if not self._states:
            raise Exception('No states to restore from!')
        p,h = self._states[-1]
        self.up()
        self.goto(p)
        self.setheading(h)
        self.down()
        self._states = self._states[:-1]

    def draw(self, sequence):
        for s in sequence:
            if s is 'F':
                self.forward(self._step)
            elif s is 'f':
                self.up()
                self.forward(self._step)
                self.down()
            elif s is '+':
                self.left(self._angle)
            elif s is '-':
                self.right(self._angle)
            elif s is '[':
                self.save_state()
            elif s  is ']':
                self.restore_state()
            else:
                print "Symbol '"+ s +"' ignored because it was not recognized by the turtle!"

def demo_koch(level = 3):
    fractal = rewrite.koch_fractal(level)
    step = 300/(3**level)
    koopa = KoopaTroopa(position=(-200,0),step=step, angle=60)
    koopa.draw(fractal)
    raw_input('Press return to end')

def demo_quadratic_koch(level=2):
    fractal = rewrite.quadratic_koch_fractal(level)
    step = 100/(5*level+1)
    koopa = KoopaTroopa(step=step, angle=90)
    koopa.draw(fractal)
    raw_input('Press return to end')

def demo_tree():
    axiom = 'F'
    rules = {'F': 'F[+F]F[-F[+F][-F]]F'}
    tree = rewrite.rewrite_iter(axiom, rules, 3)
    t.bgcolor('black')
    koopa = KoopaTroopa(position=(0,-250),step=12, angle=29, heading=270)
    koopa.color('green')
    koopa.draw(tree)
    raw_input('Press return to end')

def demo_triangles():
    axiom = 'a'
    rules = {'a': 'FaFbF-', 'b':'-FaFbF'}
    tree = rewrite.rewrite_iter(axiom, rules, 4)
    tree = tree.replace('a','+')
    tree = tree.replace('b','+')
    koopa = KoopaTroopa(position=(0,250),step=100, angle=120, heading=120)
    koopa.draw(tree)
    raw_input('Press return to end')

if __name__=="__main__":
    #~ demo_koch()
    #~ demo_quadratic_koch()
    demo_tree()
    #~ demo_triangles()
