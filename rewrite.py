##
#  Rewriting-engine for L-systems.
##

def rewrite_once(axiom, rules):
    i = 0
    while i < len(axiom):
        letter = axiom[i]
        if letter in rules.keys():
            index = i + axiom[i:].index(letter)
            axiom = axiom[:index]+rules[letter]+axiom[index+1:]
            i += len(rules[letter])
            continue
        i += 1
    return axiom

def rewrite(axiom, rules, max_itr=None):
    """Warning: Termination not guaranteed!"""
    itr = 0
    while max_itr is None or itr < max_itr:
        itr += 1
        tmp = rewrite_once(axiom, rules)
        if tmp == axiom: 
            break
        axiom = tmp
    return axiom

if __name__ == "__main__":
    pass
