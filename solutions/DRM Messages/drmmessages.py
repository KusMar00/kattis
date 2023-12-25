#! /usr/bin/python3
import sys
 
def char_to_num(c):
    return ord(c) - 65

def rotate_char(c, n):
    new_n = (char_to_num(c) + n) % 26
    return chr(new_n+65)

def rotate(line):
    sum = 0
    for char in line:
        if(char == '\n'):
            break
        sum += char_to_num(char)
    new_line = ""
    for char in line:
        if(char == '\n'):
            break
        new_line += rotate_char(char, sum)
    return new_line

def combine(line1, line2):
    new_line = ""
    for i in range(len(line1)):
        new_line += rotate_char(line1[i], char_to_num(line2[i]))
    return new_line


for line in sys.stdin:
    line1  = line[:len(line)//2]
    line2 = line[len(line)//2:]
    new_line1 = rotate(line1)
    new_line2 = rotate(line2)
    print(combine(new_line1, new_line2))