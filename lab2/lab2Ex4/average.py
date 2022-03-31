import subprocess
import sys
from pathlib import Path
if len(sys.argv) > 1:
    extension = sys.argv[1]

    output = subprocess.check_output(f'java Paths -R -s | java Process --project=1,3 | java Process --select={str(extension)}', shell=True, universal_newlines=True)

    array = output.split('\n')
    dict = {}
    for line in array:
        new_line = line.split(" ")
        if len(new_line) > 1:
            try:
                e = int(new_line[1])
                dict[new_line[0]] = e
            except:
                dict[new_line[0]] = 0
    sum_of_dict = 0
    for val in dict.values():
        sum_of_dict += val

    print("The average : " + str(sum_of_dict / len(dict)))
