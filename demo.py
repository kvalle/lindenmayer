import rewrite
import draw
import turtle

def demo_koch(level = 3):
    fractal = rewrite.koch_fractal(level)
    step = 300/(3**level)
    koopa = draw.KoopaTroopa(position=(-200,0),step=step, angle=60)
    koopa.draw(fractal)
    raw_input('Press return to end')

def demo_quadratic_koch(level=2):
    fractal = rewrite.quadratic_koch_fractal(level)
    step = 100/(5*level+1)
    koopa = draw.KoopaTroopa(step=step, angle=90)
    koopa.draw(fractal)
    raw_input('Press return to end')

def demo_tree():
    axiom = 'F'
    rules = {'F': 'F[+F]F[-F[+F][-F]]F'}
    tree = rewrite.rewrite(axiom, rules, 3)
    turtle.bgcolor('black')
    koopa = draw.KoopaTroopa(position=(0,-250),step=12, angle=29, heading=270)
    koopa.color('green')
    koopa.width(2)
    koopa.draw(tree)
    raw_input('Press return to end')

def demo_tree2():
    axiom = 'F'
    rules = {'F': 'F[-FF]F[+F[-F]F]F'}
    tree = rewrite.rewrite(axiom, rules, 3)
    turtle.bgcolor('black')
    koopa = draw.KoopaTroopa(position=(0,-250),step=10, angle=29, heading=270)
    koopa.speed(8)
    koopa.color('green')
    koopa.width(2)
    koopa.draw(tree)
    raw_input('Press return to end')

def demo_triangles():
    axiom = 'l'
    rules = {'l': 'FlFrF-', 'r':'-FlFrF'}
    tree = rewrite.rewrite(axiom, rules, 4)
    turtle.bgcolor('black')
    koopa = draw.KoopaTroopa(position=(0,250),step=100, angle=120, heading=120)
    koopa.add_mappings({'l':'left', 'r':'left'})
    koopa.color('red')
    koopa.draw(tree)
    raw_input('Press return to end')

def demo_sierpinski():
    axiom = 'a'
    rules = {'a': 'b-a-b', 'b':'a+b+a'}
    path = rewrite.rewrite(axiom, rules, 6)
    turtle.bgcolor('black')
    koopa = draw.KoopaTroopa(position=(-200,-200),step=7, angle=60)
    koopa.add_mappings({'a':'draw', 'b':'draw'})
    koopa.color('green')
    koopa.width(2)
    koopa.speed(10)
    koopa.draw(path)
    raw_input('Press return to end')

def demo_shrooms():
    path = rewrite.shroom_fractal(6)
    turtle.bgcolor('black')
    turtle.setup(width=1000)
    koopa = draw.KoopaTroopa(position=(-360,-150), heading=330, step=3, angle=60)
    koopa.add_mappings({'a':'draw', 'b':'draw'})
    koopa.color('yellow')
    koopa.speed(10)
    koopa.draw(path)
    koopa.hideturtle()
    raw_input('Press return to end')
    
if __name__=='__main__':
    demo_shrooms()
    
    
