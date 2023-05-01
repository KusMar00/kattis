import sys

lines = []

for i in sys.stdin:
    lines.append(i)

for line in lines[1:]:
    line = line.strip()
    split = line.split(" ")[1:-1]
    prev = 1
    total = 0
    for num in split:
        num = int(num)
        dif = num-prev*2
        if dif >= 0:
            total += dif
        prev = num
    print(total)