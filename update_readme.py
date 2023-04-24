#!/usr/bin/env python3

import os
import requests
from bs4 import BeautifulSoup

# Gives a link to the problem description from Kattis
def get_problem_url(problem):
    url = "[{title}](https://open.kattis.com/problems)"
    return url.format(title = problem)

# Scrapes problem info from Kattis
def scrape_problem(problem_url):
    page = requests.get(problem_url+'?tab=metadata')
    soup = BeautifulSoup(page.content ,'html.parser')
    spans = soup.find_all("span", {"class": "difficulty_number"})
    number = spans[0].text
    print(number)
    return

# Gives a list of my solutions to the given problem
def list_solutions(problem):
    return

def write_readme(problems):
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

def main():
    problems = [ x[0] for x in os.walk("./solutions") ]
    write_readme(problem)


if __name__ == '__main__':
    scrape_problem("https://open.kattis.com/problems/sequences")
    #sys.exit(main(sys.argv[1:]))