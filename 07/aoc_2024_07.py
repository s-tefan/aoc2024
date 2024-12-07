'''
AoC 2024 Day 7
'''
def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]

def fix(lines):
    def linefix(line):
        a, b = line.split(': ')
        c = [int(d) for d in b.split()]
        return {'value': int(a), 'operands': c}
    return [linefix(line) for line in lines]

def greja(equation, value = None):
    if not equation['operands']:
        return value == equation['value']
    elif value != None and value > equation['value']:
        return False
    else:
        firstoperand, the_rest = equation['operands'][0], equation['operands'][1:] 
        return greja({'value': equation['value'], 'operands': the_rest}, (0 if value == None else value) + firstoperand) or \
        greja({'value': equation['value'], 'operands': the_rest}, (1 if value == None else value) * firstoperand) 

def greja2(equation, value = None):
    if not equation['operands']:
        return value == equation['value']
    elif value != None and value > equation['value']:
        return False
    else:
        firstoperand, the_rest = equation['operands'][0], equation['operands'][1:] 
        return greja2({'value': equation['value'], 'operands': the_rest}, (0 if value == None else value) + firstoperand) or \
        greja2({'value': equation['value'], 'operands': the_rest}, (1 if value == None else value) * firstoperand) or \
        greja2({'value': equation['value'], 'operands': the_rest}, int(('' if value == None else str(value)) + str(firstoperand)))
    
def partone(eqs):
    return sum(map(lambda a: a['value'], filter(greja, eqs)))

def parttwo(eqs):
    return sum(map(lambda a: a['value'], filter(greja2, eqs)))

data = fix(read_input("07/input.txt"))
print(partone(data))
print(parttwo(data))
      