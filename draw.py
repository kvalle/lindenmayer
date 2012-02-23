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


if __name__=="__main__":
    pass
