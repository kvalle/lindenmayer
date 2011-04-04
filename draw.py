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
        self.commands = {
            'draw':(self.forward, [self._step]),
            'go':(self.forward_up, [self._step]),
            'left':(self.left, [self._angle]),
            'right':(self.right, [self._angle]),
            'mark':(self.mark, []),
            'recall':(self.recall, [])
        }
        self.set_mappings({'F':'draw','f':'go','+':'left',
                            '-':'right','[':'mark',']':'recall'})

    def _check_mappings(self, mappings):
        for cmd in mappings.values():
            if cmd not in self.commands.keys():
                error = "Cannot add mapping to non-existing command '"+cmd+"'!\n"
                error += "Available commands are: "+str(self.commands.keys())
                raise Exception(error)

    def add_mappings(self, mappings):
        self._check_mappings(mappings)
        self.mapping.update(mappings)

    def set_mappings(self, mappings):
        self._check_mappings(mappings)
        self.mapping = mappings

    def mark(self):
        p = self.position()
        h = self.heading()
        self._states.append((p,h))

    def recall(self):
        if not self._states:
            raise Exception('No states to restore from!')
        p,h = self._states[-1]
        self.up()
        self.goto(p)
        self.setheading(h)
        self.down()
        self._states = self._states[:-1]

    def forward_up(step):
        self.up()
        self.forward(step)
        self.down()

    def draw(self, sequence):
        for s in sequence:
            if s in self.mapping.keys():
                cmd = self.mapping[s]
                fun, args = self.commands[cmd]
                fun(*args)
            else:
                print "Symbol '"+ s +"' ignored because it was not recognized by the turtle!"

##
#  Demo functions
##

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
    tree = rewrite.rewrite(axiom, rules, 3)
    t.bgcolor('black')
    koopa = KoopaTroopa(position=(0,-250),step=12, angle=29, heading=270)
    koopa.color('green')
    koopa.draw(tree)
    raw_input('Press return to end')

def demo_triangles():
    axiom = 'l'
    rules = {'l': 'FlFrF-', 'r':'-FlFrF'}
    tree = rewrite.rewrite(axiom, rules, 4)
    t.bgcolor('black')
    koopa = KoopaTroopa(position=(0,250),step=100, angle=120, heading=120)
    koopa.add_mappings({'l':'left', 'r':'left'})
    koopa.color('red')
    koopa.draw(tree)
    raw_input('Press return to end')

def demo_sierpinski():
    axiom = 'a'
    rules = {'a': 'b-a-b', 'b':'a+b+a'}
    path = rewrite.rewrite(axiom, rules, 6)
    t.bgcolor('black')
    koopa = KoopaTroopa(position=(-200,-200),step=7, angle=60)
    koopa.add_mappings({'a':'draw', 'b':'draw'})
    koopa.color('green')
    koopa.width(2)
    koopa.speed(10)
    koopa.draw(path)
    raw_input('Press return to end')

if __name__=="__main__":
    #~ demo_koch()
    #~ demo_quadratic_koch()
    #~ demo_tree()
    #~ demo_triangles()
    demo_sierpinski()
