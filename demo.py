from rewrite import rewrite
import draw
import turtle
import systems

class Demo:
    def koch(self, level = 3):
        fractal = systems.koch_fractal(level)
        step = 300/(3**level)
        koopa = draw.KoopaTroopa(position=(-200,0),step=step, angle=60)
        koopa.draw(fractal)
        raw_input('')

    def koch_quad(self, level=2):
        fractal = systems.quadratic_koch_fractal(level)
        step = 100/(5*level+1)
        koopa = draw.KoopaTroopa(step=step, angle=90)
        koopa.draw(fractal)
        raw_input('')

    def tree(self, level=3):
        tree = systems.tree(level)
        turtle.bgcolor('black')
        koopa = draw.KoopaTroopa(position=(0,-250),step=12, angle=29, heading=270)
        koopa.color('green')
        koopa.width(2)
        koopa.draw(tree)
        raw_input('')

    def tree2(self, level=3):
        tree = systems.tree2(level)
        turtle.bgcolor('black')
        koopa = draw.KoopaTroopa(position=(0,-250),step=10, angle=29, heading=270)
        koopa.speed(8)
        koopa.color('green')
        koopa.width(2)
        koopa.draw(tree)
        raw_input('')

    def triangles(self, level=4):
        triangle = systems.triangles(level)
        turtle.bgcolor('black')
        koopa = draw.KoopaTroopa(position=(0,250),step=100, angle=120, heading=120)
        koopa.add_mappings({'l':'left', 'r':'left'})
        koopa.color('red')
        koopa.draw(triangle)
        raw_input('')

    def sierpinski(self, level=6):
        path = systems.sierpinski(level)
        turtle.bgcolor('black')
        koopa = draw.KoopaTroopa(position=(-200,-200),step=7, angle=60)
        koopa.add_mappings({'a':'draw', 'b':'draw'})
        koopa.color('green')
        koopa.width(2)
        koopa.speed(10)
        koopa.draw(path)
        raw_input()

    def shrooms(self, level=6):
        path = systems.shroom_fractal(level)
        turtle.bgcolor('black')
        turtle.setup(width=1000)
        koopa = draw.KoopaTroopa(position=(-360,-150), heading=330, step=3, angle=60)
        koopa.add_mappings({'a':'draw', 'b':'draw'})
        koopa.color('yellow')
        koopa.speed(10)
        koopa.draw(path)
        koopa.hideturtle()
        raw_input('')
    
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
    
