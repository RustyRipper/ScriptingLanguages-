import subprocess
import sys
from pathlib import Path

if len(sys.argv) > 1:
    n = sys.argv[1]
    output = subprocess.check_output('java Paths -R -s | java Process --project=1,3', shell=True,universal_newlines=True)
    array = output.split('\n')

    dict_1 = {}
    f = open('f1.txt', 'w')
    for line in array:
        new_line = line.replace('-', '').split(" ")
        if 1 < len(new_line):
            try:
                e = int(new_line[1])
                dict_1[new_line[0]] = e
            except:
                dict_1[new_line[0]] = 0

    sorted_dict = sorted(dict_1.items(), key=lambda item: int(item[1]), reverse=True)

    for elem in sorted_dict:
        f.write('%s %s\n' % (elem[0], elem[1]))

    f = open("f1.txt", "r")
    txt = Path('f1.txt').read_text()
    output = subprocess.run(f'java Head --lines={n}', text=True, input=txt)