#!/usr/bin/env python3

import os

problems = [ x[0] for x in os.walk("./solutions") ]

with open("README.md", "w") as f:
    f.write("# Kattis\n")
    f.write("| Problem | Solutions | Difficulty |\n")
    f.write("|   ---   |    ---    |     ---    |\n")
    for problem in problems:
        f.write("| ")
        problem_title = problem.split("/")[-1];
        f.write(problem_title + " | ")
        f.write(" - | 0.0 |\n")

    
