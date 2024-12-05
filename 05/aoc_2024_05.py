'''
AoC 2024 Day 5
'''

def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]

def fix(lines):
    rules, lists = [], []
    mupp = True
    for line in lines:
        if line == '':
            mupp = False
        elif mupp:
            rules.append(tuple(map(int, line.split('|'))))
        else:
            lists.append(tuple(map(int, line.split(','))))
    return rules, lists


def partone(rules, lists):
    s = 0
    incorrect = []
    for pages in lists:
        ok = True
        for k, first in enumerate(pages):
            for second in pages[k+1:]:
                for rule in rules:
                    if (second, first) == rule:
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                break
        if ok:
            s += pages[(len(pages)-1)//2]
        else:
            incorrect.append(pages)
    return s, incorrect
 
    

def sort(alist, rules):
    if alist:
        a = alist[0]
        before, after = [], []
        blist = alist[1:]
        for k in blist:
            if (k,a) in rules:
                before.append(k)
            elif (a,k) in rules:
                after.append(k)
            else:
                raise(Exception(f"Njae, nu saknas det en sorteringsregel för {(a,k)}"))
        return sort(before, rules) + [a] + sort(after, rules)
    else:
        return alist
            

def parttwo(rules, lists):
    s = 0
    for ap in lists:
        sorted = sort(ap, rules)
        s += int(sorted[(len(sorted) - 1)//2])
    return s


a, b = fix(read_input('05/input.txt'))
s, incorrect = partone(a,b)
print(s)
print(parttwo(a, incorrect))