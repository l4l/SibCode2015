from random import random as rand
from math import *
import re

parseable = ['sqrt', 'sin', 'cos', 'abs', 'min',
             'max', 'avg', 'if', 'concat', 'equals',
             'indexof', 'substr', 'replace', 'rand',
             'dev', 'degToRad', 'radToDeg', 'floor',
             'ceil', 'round']

parseablec = [('sin', 'sing'), ('cos', 'cosg'), ('if', 'ifv')]  # Conflicted


def sing(ang):
    return sin(degToRad(ang))


def cosg(ang):
    return cos(degToRad(ang))


def avg(*argv):
    return sum(argv) / len(argv)


def ifv(cond, f, s):
    if cond:
        return f
    return s


def concat(a, b):
    return a + b


def equals(a, b):
    return a == b


def replace(str, fr, to):
    return str.replace(fr, to)


def indexof(sub, str):
    return str.find(sub)


def substr(str, beg, len):
    return str[beg:beg + len]


def dev(*arg):
    aver = avg(arg)
    s = 0
    for a in arg:
        s += (a - aver) ** 2

    return sqrt(s / len(arg))


def degToRad(ang):
    return ang * pi / 180


def radToDeg(ang):
    return ang * 180 / pi


def lower_case(s):
    for p in parseable:
        pattern = re.compile(p, re.IGNORECASE)
        s = pattern.sub(p, s)
    for p in parseablec:
        s = s.replace(p[0], p[1])
    return s


def insert_actual_values(s, f):
    matched = re.split(r'([A-Z]+[0-9]+)', s)
    sub = ""
    for i, m in enumerate(matched):
        if i % 2 == 0:
            sub += m
            continue
        p = re.search('[0-9]+', m).start()
        sub += str(f(m[:p], m[p:]))
    return sub


def evaluate(str, f):
    val = eval(insert_actual_values(lower_case(str), f))
    val -= 1e-9  # I am really sorry about that
    val = round(val, 8)
    if floor(val) == ceil(val):
        val = int(val)
    return val
