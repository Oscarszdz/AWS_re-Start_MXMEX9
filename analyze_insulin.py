
import re

with open('preproinsulin-seq.txt') as f:
    lines = f.readlines()
    for line in lines:
        # line.replace("ORIGIN", "")
        print(line)