Fun With L-systems and Turtle Graphics
======================================

A simple implementation of a Lindenmayer system for playing around with rewriting rules, turtle graphics and fractals.
Most of the code is inspired by Chapter 4 of [1].

Lindenmayer Systems
-------------------

L-systems are rewriting systems that operates on strings of symbols.
Given an alphabet A and a set of production rules π, the system iteratively updates the contents of an axiom ω.
The system can be run to the string contents converge or for a number of iterations.
The production rules are applied in parallel.

For example:

    A = {a, b, +, -}
    ω = a-b
    π = {a → b+a-b, b → a-b+a}

should produce the following results

    0: a-b
    1: b+a-b-a-b+a
    2: a-b+a+b+a-b-a-b+a-b+a-b-a-b+a+b+a-b
    3: b+a-b-a-b+a+b+a-b+a-b+a+b+a-b-a-b+a-b+a-b-a-b+a+b+a-b-a-b+a+b+a-b-a-b+a-b+a-b-a-b+a+b+a-b+a-b+a+b+a-b-a-b+a

Turtle Graphics
---------------

L-systems are no fun unless the resulting strings are interpreted and used for something.
Turtle graphics are a popular way to interpret and visualize the strings.

The turtle represent a simple drawing tool, able to execute a few drawing commands such as moving forward while drawing a line, and turning left and right.
A few additional commands such as moving without drawing and saving and restoring the turtle's state enables drawing of trees and other recursively branching structures.

The result of six iterations of the above example as drawn by the turtle, with both `a` and `b` corresponding to *draw forward*, and `+` and `-` meaning *turn left* and *turn right*, respectively:

![Image of example fractal](https://github.com/kvalle/lindenmayer/raw/master/imgs/example.png)

---

[1] Bio-Inspired Artificial Intelligence, 2008, D. Florreano and C. Mattiussi, MIT Press

