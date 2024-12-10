"""
AoC 2024 Day 9
"""
import time


def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]


def fix(lines):
    data = []
    pos = 0
    for k, c in enumerate(lines[0]):
        blocks = int(c)
        data.append({"pos": pos, "blocks": blocks, "id": None if k % 2 else k // 2})
        pos += int(c)
    return data


def fix2(lines):
    files = []
    empties = []
    pos = 0
    for k, c in enumerate(lines[0]):
        blocks = int(c)
        if k % 2:
            empties.append({"pos": pos, "blocks": blocks})
        else:
            files.append({"pos": pos, "blocks": blocks})
        pos += int(c)
    return (files, empties)


def partone(data):
    first_empty = 1
    while first_empty < len(data):
        # print(data)
        bepa = data.pop()
        a = data[first_empty]["blocks"]
        b = bepa["blocks"]
        if b < a:
            bepa["pos"] = data[first_empty]["pos"]
            data[first_empty]["id"] = bepa["id"]
            data[first_empty]["blocks"] = b
            data.insert(
                first_empty + 1,
                {"pos": data[first_empty]["pos"] + b, "blocks": a - b, "id": None},
            )
        elif b == a:
            data[first_empty]["id"] = bepa["id"]
        elif b > a:
            data[first_empty]["id"] = bepa["id"]
            data.append({"pos": bepa["pos"], "blocks": b - a, "id": bepa["id"]})
        else:
            pass  # händer inte
        while data[-1]["id"] == None:
            data.pop()
        while first_empty < len(data) and data[first_empty]["id"] != None:
            first_empty += 1
    return sum(
        (2 * ap["pos"] + ap["blocks"] - 1) * ap["blocks"] // 2 * ap["id"] for ap in data
    )


def parttwo(data):
    files, empties = data
    filesreordered = sorted(files, key=lambda x: x["pos"])
    for file in reversed(files):
        empties = [
            {
                "pos": filesreordered[k]["pos"] + filesreordered[k]["blocks"],
                "blocks": filesreordered[k + 1]["pos"]
                - filesreordered[k]["pos"]
                - filesreordered[k]["blocks"],
            }
            for k in range(len(filesreordered) - 1)
        ]
        for emptyspace in empties:
            if emptyspace["pos"] > file["pos"]:
                break
            if file["blocks"] <= emptyspace["blocks"]:
                file["pos"] = emptyspace["pos"]
                break
        filesreordered.sort(key=lambda x: x["pos"])

    return sum(
        (2 * file["pos"] + file["blocks"] - 1) * file["blocks"] // 2 * k
        for k, file in enumerate(files)
    )


t = [time.perf_counter()]
tt = [time.process_time()]
data = fix(read_input("09/input.txt"))
print(partone(data))
t.append(time.perf_counter())
tt.append(time.process_time())
data = fix2(read_input("09/input.txt"))
print(parttwo(data))
t.append(time.perf_counter())
tt.append(time.process_time())
print([t[k+1]-t[k] for k in range(len(t)-1)])
print([tt[k+1]-tt[k] for k in range(len(tt)-1)])