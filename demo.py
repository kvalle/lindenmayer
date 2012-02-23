from rewrite import rewrite
import draw
import turtle
import systems

class Demo:

    def __init__(self):
        turtle.bgcolor('black')

    def _list_demos(self):
        return [method for method in dir(self) if not method[0]=="_"]
        
    def _draw(self, demo, levels):
        fun = getattr(self,demo)
        koopa, path = fun(levels) if levels else fun()
        koopa.width(2)
        koopa.color('white')
        koopa.speed(8)
        koopa.draw(path)
        raw_input()

    def koch(self, levels = 3):
        path = systems.koch_fractal(levels)
        koopa = draw.KoopaTroopa(position=(-200,0), step=300/(3**levels), angle=60)
        return koopa, path

    def koch_quad(self, levels=2):
        path = systems.quadratic_koch_fractal(levels)
        koopa = draw.KoopaTroopa(step=100/(5*levels+1), angle=90)
        return koopa, path

    def tree(self, levels=3):
        path = systems.tree(levels)
        koopa = draw.KoopaTroopa(position=(0,-250), step=12, angle=29, heading=270)
        return koopa, path

    def tree2(self, levels=3):
        path = systems.tree2(levels)
        koopa = draw.KoopaTroopa(position=(0,-250), step=10, angle=29, heading=270)
        return koopa, path

    def triangles(self, levels=4):
        path = systems.triangles(levels)
        koopa = draw.KoopaTroopa(position=(0,250), step=100, angle=120, heading=120)
        koopa.add_mappings({'l':'left', 'r':'left'})
        return koopa, path

    def sierpinski(self, levels=6):
        path = systems.sierpinski(levels)
        koopa = draw.KoopaTroopa(position=(-200,-200), step=7)
        koopa.add_mappings({'a':'draw', 'b':'draw'})
        return koopa, path

    def shrooms(self, levels=6):
        path = systems.shroom_fractal(levels)
        koopa = draw.KoopaTroopa(position=(-360,-150), step=3, heading=330)
        koopa.add_mappings({'a':'draw', 'b':'draw'})
        koopa.hideturtle()
        return koopa, path
    
if __name__=='__main__':
    import sys
    
    def print_usage_and_die():
        print "Usage:"
        print "  python demo.py DEMO [LEVEL]"
        print
        print "DEMO\t{" + ", ".join(Demo()._list_demos())+"}"
        print "LEVEL\tSpecify number of iterations for rewrite-engine"
        sys.exit()
    
    def level(arg):
        try:
            level = int(arg)
            assert level > 0
            return level
        except:
            print "! LEVEL must be positive integer"
            sys.exit() 
        
    if len(sys.argv) == 1:
        print_usage_and_die()
    level = level(sys.argv[2]) if len(sys.argv) > 2 else None
    Demo()._draw(sys.argv[1], level)
    
