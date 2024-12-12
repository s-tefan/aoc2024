"""
AoC 2024 Day 12
"""


class GardenMap(dict):
    def __init__(self, lines=None):
        if lines:
            self.unchecked = []
            for r, line in enumerate(lines):
                for c, plant in enumerate(line):
                    self[(r, c)] = plant
                    self.unchecked.append((r,c))
            #self.unchecked = set(self) # more effective if taken line by line
            self.regions = []
            while self.unchecked:
                newplot = self.unchecked.pop()
                # om bara en granne med samma plant addera till den regionen
                # om flera, lägg samman dess om de är i olika regioner
                r, c = newplot
                plant = self[newplot]
                regs = []
                for reg in self.regions:
                    if reg.plant == plant and any(
                        nb in reg 
                        for nb in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
                    ):
                        regs.append(reg)
                if len(regs) == 0:
                    self.regions.append(GardenRegion(newplot, plant))
                elif len(regs) == 1:
                    regs[0].add(newplot)
                else:
                    joined = GardenRegion.join(newplot, plant, regs)
                    for reg in regs:
                        self.regions.remove(reg)
                    self.regions.append(joined)

class GardenRegion(set):
    def __init__(self, plot=None, plant=None):
        if plot:
            self.add(plot)
        if plant:
            self.plant = plant
        # self.perimeter = {plot} if plot in map else set{}
        # self.open = self.perimeter.copy()

    @staticmethod
    def join(plot, plant, reglist):
        gl = GardenRegion(plot, plant)
        for r in reglist:
            gl.update(r)
        return gl


"""
    def add_if_nb(self, p):
        r, c = p
        if any(x in self.perimeter for x in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]):
            self.perimeter.add(p)
            self.update_perimeter()

    def add(self, p):

    def update_perimeter(self):
        for p in self.perimeter:
            r, c = p
            if all(x in set for x in[(r-1,c),(r+1,c),(r,c-1),(r,c+1)] ):
                self.perimeter.remove(p)
            if not any(x in self.map.unchecked) for x in[(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
                self.open.remove(p)
"""


def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]


def fix(lines):
    return lines


def partone(data):
    gm = GardenMap(data)
    s = 0
    for reg in gm.regions:
        perimeter = 0
        for plot in reg:
            r, c = plot
            for p in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if p not in gm or gm[p] != reg.plant:
                    perimeter += 1
        #print(reg.plant, len(reg), perimeter)
        s += len(reg) * perimeter
    return s

    return None


def parttwo(data):
    return None


data = fix(read_input("12/input.txt"))
print(partone(data))
print(parttwo(data))
