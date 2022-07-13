from tabnanny import filename_only


# def tail(filename, n=10):
#     with open(filename, "r") as f:
#         lines = f.readlines()
#     for line in lines[-1:-n-1:-1]:
#         print(line)

file = "/home/miki/Desktop/Deployment/currency-denomination/ttt.txt"

# tail(file)

# def parse1():
#     for line in open(file, "r"):
#         print(" ".join(line.split("[" or "]")[3:5]))

# parse1()

# def parse1():
#     for line in open(file, "rw"):
#         print(" ".join(line.split()[3:5]).strip("[]"))
# parse1()
# import re
# def parse1():
#     for line in open(file):
#         print(re.split("\[|\]", line)[1])
# parse1()

ls = [-1, 2, 3, -3, 4]

# def sqsum1(ls):
#     return sum(x**2 if x > 0 for x in ls)
# def sqsum1(ls):
#     return sum(x**2 for x in ls if x > 0)
# sqsum1(ls)
# def sqsum1(ls):
#     return sum(for x in ls if x > 0 then x^2)
# sqsum1(ls)
# def sqsum1(ls):
#     return sum(x^2 if x > 0 for x in ls )
# sqsum1(ls)

class FunEvent:
    def __init__(self, tags, year):
        self.tags = tags
        self.year = year
    def __str__(self):
        return f"FunEvent(tags = {self.tags}, year = {self.year})"
tags = ["google", "ml"]
year = 2022
bootcamp = FunEvent(tags, year)
tags.append("bootcamp")
year = 2023
print(bootcamp)