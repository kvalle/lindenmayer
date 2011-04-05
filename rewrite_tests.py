import unittest
import rewrite as rw

class GeneratorTests(unittest.TestCase):
    def test_lindenmayer(self):
        s = rw.lindenmayer_leaf(4)
        self.assertEqual(s,'fDgRdRaDiDgRk')

    def test_koch(self):
        k = 'F+F--F+F+F+F--F+F--F+F--F+F+F+F--F+F+F+F--'
        k += 'F+F+F+F--F+F--F+F--F+F+F+F--F+F--F+F--F+F'
        k += '+F+F--F+F--F+F--F+F+F+F--F+F+F+F--F+F+F+F'
        k += '--F+F--F+F--F+F+F+F--F+F'
        self.assertEqual(k,rw.koch_fractal(3))

    def test_quadratic_koch_fractal(self):
        f = 'F+F-F-FF+F+F-F+F+F-F-FF+F+F-F+F+F-F-FF+F+F-F+F+F-F-FF+F+F-F'
        self.assertEqual(f,rw.quadratic_koch_fractal(1))

    def test_hilbert_fractal(self):
        f = '+-aF+bFb+Fa-F-+bF-aFa-Fb+F+bF-aFa-Fb+-F-aF+bFb+Fa-+'
        self.assertEqual(f,rw.hilbert_fractal(2))

    def test_shroom_fractal(self):
        f = 'a-b+a+b+a-b-a-b+a-b+a-b-a-b+a+b+a-b'
        self.assertEqual(f,rw.shroom_fractal(2))


class RewriteTests(unittest.TestCase):
    def test_rewrite_once(self):
        rules = {'a': 'ab', 'b': 'c'}
        self.assertEqual('ab',rw.rewrite_once('a', rules))
        self.assertEqual('abc',rw.rewrite_once('ab', rules))

    def test_rewrite_iter(self):
        rules = {'F': 'F+F--F+F'}
        s = rw.rewrite('F', rules, 2)
        t = 'F+F--F+F+F+F--F+F--F+F--F+F+F+F--F+F'
        self.assertEqual(t,s)

    def test_rewrite_converges(self):
        rules = {'a': 'bc', 'b':'ef', 'c':'gh'}
        self.assertEqual('efgh',rw.rewrite('a', rules))

    def test_rewrite_max_itr(self):
        rules = {'a': 'ab'}
        self.assertEqual('abbbb',rw.rewrite('a', rules, max_itr=4))

if __name__ == "__main__":
    unittest.main()
