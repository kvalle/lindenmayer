def rewrite(axiom, rules):
    i = 0
    while i < len(axiom):
        x = axiom[i]
        if x in rules.keys():
            index = i + axiom[i:].index(x)
            axiom = axiom[:index]+rules[x]+axiom[index+1:]
            i += len(rules[x])
            continue
        i += 1
    return axiom

def rewrite_iter(axiom, rules, iterations):
    for i in range(iterations):
        axiom = rewrite(axiom, rules)
    return axiom

def rewrite_converge(axiom, rules):
    """Warning: Termination not guaranteed!"""
    while True:
        tmp = rewrite(axiom, rules)
        if tmp==axiom: break
        axiom = tmp
    return axiom

def koch_fractal(levels=2):
    axiom = 'f'
    production_rules = {'f': 'f+f--f+f'}
    axiom = rewrite_iter(axiom, production_rules, levels)
    return axiom

def test_rewrite():
    rules = {'a': 'ab', 'b': 'c'}
    assert('ab'==rewrite('a', rules))
    assert('abc'==rewrite('ab', rules))

    rules = {'f': 'f+f--f+f'}
    s = rewrite_iter('f', rules, 2)
    t = 'f+f--f+f+f+f--f+f--f+f--f+f+f+f--f+f'
    assert(t==s)

    rules = {'a': 'bc', 'b':'ef', 'c':'gh'}
    assert('efgh'==rewrite_converge('a',rules))
    print 'ok'

def run_tests():
    test_rewrite()

if __name__=="__main__":
    run_tests()
