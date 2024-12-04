def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]

def fix(lines):
    return ''.join(lines)

class Universal(frozenset):
    def __contains__(self, _):
        return True

digits = '1234567890'
anything = Universal()

rules = {
    ('waiting', 'm', 'u'): 'start',
    ('start', 'm', 'u'): 'start',
    ('start', 'u', 'l'): 'start',
    ('start', 'l', '('): 'first',
    ('first', '(', digits): 'first',
    ('first', digits, digits): 'first',
    ('first', digits, ','): 'comma',
    ('comma', ',', digits): 'second',
    ('second', ',', digits): 'second',
    ('second', digits, digits): 'second',
    ('second', digits, ')'): 'end',
    ('end', ')', anything): 'waiting',
    ('waiting', anything, anything): 'waiting'
         }

rules2 = {
        ('waiting', 'd', 'o'): 'predo',
        ('predo', 'd', 'o'): 'predo',
        ('predo', 'o', '('): 'predo',
        ('predo', 'o', "n"): 'predont', 
        ('predont', 'n', "'"): 'predont',
        ('predont', "'", 't'): 'predont',
        ('predont', "t", '('): 'predont',
        ('predo','(', ')'): 'do',
        ('predont','(', ')'): 'dont',
        ('do', anything, anything): 'waiting',
        ('dont', anything, anything): 'waiting'
    }
rules2.update(rules)


def doit(text):
    s = 0    
    state, prev, next = 'waiting', '', '' 
    firstdig, seconddig = '',''

    for next_char in text:
        prev, next = next, next_char
        rule_used = False
        #print(state, prev, next)

        for rule in rules:
            if state == rule[0] and (prev in rule[1] and next in rule[2]):
                if state == 'waiting':
                    pass
                elif state == 'start':
                    pass
                elif state == 'first':
                    firstdig += prev if prev in digits else ''
                elif state == 'comma':
                    firstnumber = int(firstdig)
                    firstdig = ''
                elif state == 'second':
                    seconddig += prev if prev in digits else ''
                elif state == 'end':
                    secondnumber = int(seconddig) if seconddig else 0
                    seconddig = ''
                    s += firstnumber * secondnumber
                    #print(firstnumber, secondnumber)
                state = rules[rule]
                rule_used = True
                break
        if not rule_used:
            state, prev, next = 'waiting', '', '' 
            firstdig, seconddig = '',''
    return s

def doit2(text):
    s = 0    
    state, prev, next = 'waiting', '', '' 
    firstdig, seconddig = '',''
    doflag = True

    for next_char in text:
        prev, next = next, next_char
        rule_used = False
        #print(state, prev, next)

        for rule in rules2:
            if state == rule[0] and (prev in rule[1] and next in rule[2]):
                if state == 'waiting':
                    pass
                elif state == 'start':
                    pass
                elif state == 'first':
                    firstdig += prev if prev in digits else ''
                elif state == 'comma':
                    firstnumber = int(firstdig)
                    firstdig = ''
                elif state == 'second':
                    seconddig += prev if prev in digits else ''
                elif state == 'end':
                    secondnumber = int(seconddig) if seconddig else 0
                    seconddig = ''
                    if doflag:
                        s += firstnumber * secondnumber
                    print(doflag,firstnumber, secondnumber)
                elif state == 'do':
                    print("DO")
                    doflag = True
                elif state == 'dont':
                    print("DON'T")
                    doflag = False                
                state = rules2[rule]
                rule_used = True
                break
        if not rule_used:
            state, prev, next = 'waiting', '', '' 
            firstdig, seconddig = '',''
    return s

text = fix(read_input('03/input.txt'))

def partone(text):
   return doit(text)

def parttwo(text):
   return doit2(text)

print(partone(text))
print(parttwo(text))
      