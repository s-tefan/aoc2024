def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]

def fix(lines):
    reports = list(list(map(int, line.split())) for line in lines)
    return reports

def check(report):
    diff = [report[k+1]-report[k] for k in range(len(report)-1)]
    return all([x >= 1 and x <=3 for x in diff]) or all([x <= -1 and x >= -3 for x in diff])

def check2(report):
    if check(report):
        return True
    for k in range(len(report)):
        dampened = report[:k] + report[k+1:]
        diff = [dampened[k+1] - dampened[k] for k in range(len(dampened)-1)]
        if all([x >= 1 and x <=3 for x in diff]) or all([x <= -1 and x >= -3 for x in diff]):
            return True
    return False




def partone(lists):
   return len(list(filter(check, lists)))

def parttwo(lists):
   return len(list(filter(check2, lists)))

lists = fix(read_input("02/input.txt"))
print(partone(lists))
print(parttwo(lists))
      