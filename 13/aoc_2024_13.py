"""
AoC 2024 Day 13
"""


def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]


def fix(lines):
    k = 0
    e = []
    d = dict()
    for line in lines:
        if line[:6] == "Button":
            a, b = line.find("+"), line.find(",")
            c = line.find("+", b)
            dx, dy = int(line[a + 1 : b]), int(line[c + 1 :])
            d[line[7]] = (dx, dy)
        elif line[:5] == "Prize":
            a, b = line.find("="), line.find(",")
            c = line.find("=", b)
            dx, dy = int(line[a + 1 : b]), int(line[c + 1 :])
            d["P"] = (dx, dy)
            e.append(d.copy())
    return e


def partone(data):
    cost = 0
    for mupp in data:
        det = mupp["A"][0] * mupp["B"][1] - mupp["A"][1] * mupp["B"][0]
        aa = mupp["B"][1] * mupp["P"][0] - mupp["B"][0] * mupp["P"][1]
        bb = mupp["A"][0] * mupp["P"][1] - mupp["A"][1] * mupp["P"][0]
        if not (aa % det) and not (bb % det):
            cost += (3 * aa + bb) // det
    return cost


def parttwo(data):
    cost = 0
    for mupp in data:
        p, q = mupp["P"]
        p += 10000000000000
        q += 10000000000000
        det = mupp["A"][0] * mupp["B"][1] - mupp["A"][1] * mupp["B"][0]
        aa = mupp["B"][1] * p - mupp["B"][0] * q
        bb = mupp["A"][0] * q - mupp["A"][1] * p
        if not (aa % det) and not (bb % det):
            cost += (3 * aa + bb) // det
    return cost


data = fix(read_input("13/input.txt"))

print(partone(data))
print(parttwo(data))
