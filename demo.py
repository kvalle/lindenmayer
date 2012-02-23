from rewrite import rewrite
import draw
import turtle
import systems

class Demo:

    def __init__(self):
        turtle.bgcolor('black')
        
    def _draw(self):
        self.koopa.width(2)
        self.koopa.color('white')
        self.koopa.speed(8)
        self.koopa.draw(self.path)
        raw_input()

    def koch(self, levels = 3):
        self.path = systems.koch_fractal(levels)
        self.koopa = draw.KoopaTroopa(position=(-200,0),step=300/(3**level), angle=60)
        self._draw()

    def koch_quad(self, levels=2):
        self.path = systems.quadratic_koch_fractal(levels)
        self.koopa = draw.KoopaTroopa(step=100/(5*level+1), angle=90)
        self._draw()

    def tree(self, levels=3):
        self.path = systems.tree(levels)
        self.koopa = draw.KoopaTroopa(position=(0,-250),step=12, angle=29, heading=270)
        self._draw()

    def tree2(self, levels=3):
        self.path = systems.tree2(levels)
        self.koopa = draw.KoopaTroopa(position=(0,-250),step=10, angle=29, heading=270)
        self._draw()

    def triangles(self, levels=4):
        self.path = systems.triangles(levels)
        self.koopa = draw.KoopaTroopa(position=(0,250),step=100, angle=120, heading=120)
        self.koopa.add_mappings({'l':'left', 'r':'left'})
        self._draw()

    def sierpinski(self, levels=6):
        self.path = systems.sierpinski(levels)
        self.koopa = draw.KoopaTroopa(position=(-200,-200),step=7, angle=60)
        self.koopa.add_mappings({'a':'draw', 'b':'draw'})
        self._draw()

    def shrooms(self, levels=6):
        self.path = systems.shroom_fractal(levels)
        self.koopa = draw.KoopaTroopa(position=(-360,-150), heading=330, step=3, angle=60)
        self.koopa.add_mappings({'a':'draw', 'b':'draw'})
        self.koopa.hideturtle()
        self._draw()
    
if __name__=='__main__':
    import sys
    
    def print_usage_and_die():
        print "Usage:"
        print "  python demo.py DEMO [LEVEL]"
        print
        print "DEMO\t{" + ", ".join(demos)+"}"
        print "LEVEL\tSpecify number of iterations for rewrite-engine"
        sys.exit()
    
    def get_demo_method():    
        try:
            return getattr(Demo(),sys.argv[1])
        except AttributeError:
            print "! Specified DEMO not one of: " + ", ".join(demos)
            sys.exit() 
            
    def get_level():
        try:
            level = int(sys.argv[2])
            assert level > 0
            return level
        except:
            print "! LEVEL must be positive integer"
            sys.exit() 
        
    demos = [method for method in dir(Demo) if not method[0]=="_"]
    if len(sys.argv) == 1:
        print_usage_and_die()
    demo = get_demo_method()
    if len(sys.argv) > 2:
        level = get_level()
        demo(level)
    else:
        demo()
    
