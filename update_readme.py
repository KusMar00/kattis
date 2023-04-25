#!/usr/bin/env python3

import os
import requests
from bs4 import BeautifulSoup

# Gives a link to the problem description from Kattis
def get_problem_url(problem):
    url = f"https://open.kattis.com/problems/{problem}"
    return url

def get_solution_url(title, solution, extension):
    title = title.replace(' ', '%20')
    url = f"[{extension}](https://github.com/KusMar00/kattis/tree/main/solutions/{title}/{solution})"
    return url

# Scrapes problem info from Kattis
def scrape_problem(problem_url):
    try:
        page = requests.get(problem_url+'?tab=metadata')
        soup = BeautifulSoup(page.content ,'html.parser')
        number = str(soup.find_all("span", {"class": "difficulty_number"})[0].text)
        return number
    except:
        return ""



# Gives a dictionary with metadata on a given problem
def get_problem_info(problem):
    problem_dict = {"title": problem, "solutions": [], "origin": ""}
    solutions = [ x[2] for x in os.walk(f"./solutions/{problem}") ]
    # Find valid solutions
    for solution in solutions[0]:
        split = solution.split(".")
        if problem_dict["origin"] == "":
            problem_dict["origin"] = split[0]
        ext = split[-1]
        if ext == "c":
            url = get_solution_url(problem, solution, "C")
            problem_dict["solutions"].append(url)
        elif ext == "cpp":
            url = get_solution_url(problem, solution, "C++")
            problem_dict["solutions"].append(url)
        elif ext == "py":
            url = get_solution_url(problem, solution, "Python")
            problem_dict["solutions"].append(url)
        elif ext == "java":
            url = get_solution_url(problem, solution, "Java")
            problem_dict["solutions"].append(url)
        elif ext == "go":
            url = get_solution_url(problem, solution, "Go")
            problem_dict["solutions"].append(url)
        elif ext == "fs" or ext == "fsx" or ext == "fsi":
            url = get_solution_url(problem, solution, "F#")
            problem_dict["solutions"].append(url)
        elif ext == "cs":
            url = get_solution_url(problem, solution, "C#")
            problem_dict["solutions"].append(url)
    
    problem_dict["url"] = get_problem_url(problem_dict["origin"])
    problem_dict["difficulty"] = scrape_problem(problem_dict["url"])

    return problem_dict

def write_readme():
    problems = [ x[1] for x in os.walk("./solutions/") ]
    with open("README.md", "w") as f:
        f.write("[![Update README](https://github.com/KusMar00/kattis/actions/workflows/deploy.yml/badge.svg)](https://github.com/KusMar00/kattis/actions/workflows/deploy.yml)\n")
        f.write("# Kattis 🐱\n")
        f.write("These are my solutions to kattis problems\n")
        f.write("## [Open Kattis](https://open.kattis.com/)\n")
        f.write("| Problem | Solutions | Difficulty |\n")
        f.write("| ------- | --------- | ---------- |\n")
        for problem in problems[0]:
            problem_dict = get_problem_info(problem)
            url = problem_dict["url"]

            # Write problem title
            title = problem_dict["title"]
            url = problem_dict["url"]
            f.write(f"| [{title}]({url}) | ")

            # Write solutions
            solutions = problem_dict["solutions"]
            for solution in solutions:
                if solution == solutions[-1]:
                    f.write(solution)
                else:
                    f.write(solution + ", ")
            f.write(" |")

            # Write difficulty rating
            diff = problem_dict["difficulty"]
            f.write(f" {diff} |\n")
        f.write("## LilleKat\n")
        f.write("## DPOP\n")
        f.write("## Notes\n")
        f.write("The `update_readme.py` script requires a relatively strict file structure and naming convention in order to work: Problems are found in the `/solutions/` dir. The title of a problem is determined by the subdirs here. Each subdir has a list of solution files. The name of these files must correspond to the name in the kattis problem url. For instance a solution to the *Knight Packing* problem, must be called `knightpacking.cpp`.\n")
        f.write("\n*Credits must be given to [this repo](https://github.com/robertusbagaskara/kattis-solutions/tree/master), for inspiration on the script.*")
if __name__ == '__main__':
    write_readme()
