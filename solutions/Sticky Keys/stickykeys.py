import sys

for line in sys.stdin:
    prev = ''
    res = ''
    for char in line:
        if char == prev:
            continue
        prev = char
        res += char
    print(res)