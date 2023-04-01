#!/usr/bin/env python3

import os

problems = [ x[0] for x in os.walk("./solutions") ]

def problem_url(problem):
    url = "[{title}](https://open.kattis.c½om/problems)"
    return url.format(title = problem)

with open("README.md", "w") as f:
    f.write("# Kattis\n")
    f.write("| Problem | Solutions | Difficulty |\n")
    f.write("| ------- | --------- | ---------- |\n")
    for problem in problems:
        split = problem.split("/");
        if len(split) < 3 :
            continue
        f.write("| " + problem_url(split[-1]) + " | ")
        f.write(" - | 0.0 |\n")


