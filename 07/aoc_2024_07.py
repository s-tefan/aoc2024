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

def greja(equation, part, value = None):
    if not equation['operands']:
        return value == equation['value']
    elif value != None and value > equation['value']:
        return False
    else:
        firstoperand, the_rest = equation['operands'][0], equation['operands'][1:] 
        return greja({'value': equation['value'], 'operands': the_rest}, \
                     value = (0 if value == None else value) + firstoperand, part = part) or \
        greja({'value': equation['value'], 'operands': the_rest}, \
              value = (1 if value == None else value) * firstoperand, part = part) or \
        (False if part == 1 else greja({'value': equation['value'], 'operands': the_rest},\
                                       value = int(('' if value == None else str(value)) + str(firstoperand)), part = part))

eqs = fix(read_input("07/input.txt"))
print(sum(map(lambda a: a['value'], filter(lambda x:greja(x, part = 1), eqs))))
print(sum(map(lambda a: a['value'], filter(lambda x:greja(x, part = 2), eqs))))
      