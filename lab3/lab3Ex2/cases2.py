import subprocess
import sys
from pathlib import Path

path = ""
continent = ""
year = ""
month = ""

for param in sys.argv:
    new_param = param.split('=')
    if new_param[0].__eq__('-path'):
        path = new_param[1]
    if new_param[0].__eq__('-continent'):
        continent = new_param[1]
    elif new_param[0].__eq__('-year'):
        year = new_param[1]
    elif new_param[0].__eq__('-month'):
        month = new_param[1]

txt = ''
try:
    txt = Path(path).read_text()
except FileNotFoundError as e:
    print('bad file')

param = f'"{month} {year} {continent}"'
sum_of_cases = 0
try:
    sum_of_cases = subprocess.check_output(
        f'java Process --project=3,4,11,5 | java Process --select={param}| java Process --project=4 | java Aggregate -sum ',
        text=True, input=txt, shell=True, universal_newlines=True)
except subprocess.CalledProcessError as e:
    if e.returncode == 2:
        print('bad input :c')
    if e.returncode == 1:
        print('bad params :/')

print(sum_of_cases)
