##
#  Unit tests for the L-systems and the rewrite-engine.
##

import unittest
import rewrite as rw
import systems

class SystemsTests(unittest.TestCase):
    def test_lindenmayer_leaf(self):
        expected = 'fDgRdRaDiDgRk'
        self.assertEqual(expected, systems.lindenmayer_leaf(4))

    def test_koch(self):
        expected = 'F+F--F+F+F+F--F+F--F+F--F+F+F+F--F+F+F+F--'
        expected += 'F+F+F+F--F+F--F+F--F+F+F+F--F+F--F+F--F+F'
        expected += '+F+F--F+F--F+F--F+F+F+F--F+F+F+F--F+F+F+F'
        expected += '--F+F--F+F--F+F+F+F--F+F'
        self.assertEqual(expected, systems.koch_fractal(3))

    def test_quadratic_koch_fractal(self):
        expected = 'F+F-F-FF+F+F-F+F+F-F-FF+F+F-F+F+F-F-FF+F+F-F+F+F-F-FF+F+F-F'
        self.assertEqual(expected, systems.quadratic_koch_fractal(1))

    def test_hilbert_fractal(self):
        expected = '+-aF+bFb+Fa-F-+bF-aFa-Fb+F+bF-aFa-Fb+-F-aF+bFb+Fa-+'
        self.assertEqual(expected, systems.hilbert_fractal(2))

    def test_shroom_fractal(self):
        expected = 'a-b+a+b+a-b-a-b+a-b+a-b-a-b+a+b+a-b'
        self.assertEqual(expected, systems.shroom_fractal(2))


class RewriteTests(unittest.TestCase):
    def test_rewrite_once(self):
        rules = {'a': 'ab', 'b': 'c'}
        self.assertEqual('ab', rw.rewrite_once('a', rules))
        self.assertEqual('abc', rw.rewrite_once('ab', rules))

    def test_rewrite_iter(self):
        rules = {'F': 'F+F--F+F'}
        expected = 'F+F--F+F+F+F--F+F--F+F--F+F+F+F--F+F'
        self.assertEqual(expected, rw.rewrite('F', rules, 2))

    def test_rewrite_converges(self):
        rules = {'a': 'bc', 'b':'ef', 'c':'gh'}
        self.assertEqual('efgh', rw.rewrite('a', rules))

    def test_rewrite_max_itr(self):
        rules = {'a': 'ab'}
        self.assertEqual('abbbb', rw.rewrite('a', rules, max_itr=4))

    def test_zero_iterations(self):
        rules = {'a': 'b'}
        self.assertEqual('a', rw.rewrite('a', rules, max_itr=-0))

if __name__ == "__main__":
    unittest.main()
