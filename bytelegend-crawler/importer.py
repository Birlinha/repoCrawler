import csv
import sys
import os

if __name__ == "__main__":
    with open("data/bytelegend.csv") as f:
        r = f.read()
        f.close()
    
    bytelegendcsv = r.split(",")

    os.chdir("./repos")
    for repo in bytelegendcsv:
        path  = "./repos/{}".format(repo)
        clone = "git clone https://github.com/ByteLegendQuest/{}".format(repo) 
        os.system(clone) # Cloning