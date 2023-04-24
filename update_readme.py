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

def write_readme():
    problems = [ x[1] for x in os.walk("./solutions") ]
    with open("README.md", "w") as f:
        f.write("# Kattis\n")
        f.write("| Problem | Solutions | Difficulty |\n")
        f.write("| ------- | --------- | ---------- |\n")
        for problem in problems:
            f.write("| " + problem_url(problem) + " | ")
            f.write(" - | 0.0 |\n")

def main():
    write_readme()


if __name__ == '__main__':
    write_readme()