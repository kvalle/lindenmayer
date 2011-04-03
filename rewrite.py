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

def koch_fractal(levels=2):
    axiom = 'f'
    production_rules = {'f': 'f+f--f+f'}
    for i in range(levels):
        axiom = rewrite(axiom, production_rules)
    return axiom

def test_rewrite():
    rules = {'a': 'ab',
             'b': 'c'}
    assert('ab'==rewrite('a', rules))
    assert('abc'==rewrite('ab', rules))
    rules = {'f': 'f+f--f+f'}
    s = rewrite('f', rules)
    s = rewrite(s, rules)
    t = 'f+f--f+f+f+f--f+f--f+f--f+f+f+f--f+f'
    assert(t==s)
    print 'ok'

def run_tests():
    test_rewrite()

if __name__=="__main__":
    run_tests()
