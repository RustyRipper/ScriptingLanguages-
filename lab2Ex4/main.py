import subprocess
import sys
from pathlib import Path

if len(sys.argv) > 1:
    n = sys.argv[1]
    output = subprocess.check_output("java Paths -R -s | java Process --project=1,3", shell=True,
                                     universal_newlines=True)

    array = output.split('\n')

    dict_1 = {}
    f = open('f1.txt', 'w')
    for a in array:
        new_a = a.replace('-', '').split(" ")
        if 1 < len(new_a):
            try:
                e = int(new_a[1])
                dict_1[new_a[0]] = e
            except:
                dict_1[new_a[0]] = 0

    sorted_dict = sorted(dict_1.items(), key=lambda item: int(item[1]), reverse=True)

    for i in sorted_dict:
        f.write('%s %s\n' % (i[0], i[1]))

    f = open("f1.txt", "r")
    txt = Path('f1.txt').read_text()
    output = subprocess.run(f"java Head --lines={n}", text=True, input=txt)
# ---------------------------------------------------------------------
if len(sys.argv) > 2:
    extension = sys.argv[2]
    output = subprocess.check_output(f"java Process --select={str(extension)}", shell=True, universal_newlines=True,
                                     text=True, input=txt)

    array = output.split('\n')
    dict_2 = {}
    for a in array:
        new_a = a.split(" ")
        if 1 < len(new_a):
            try:
                e = int(new_a[1])
                dict_2[new_a[0]] = e
            except:
                dict_2[new_a[0]] = 0
    sum = 0
    for val in dict_2.values():
        sum += val

    print("The average : " + str(sum / len(dict_2)))
