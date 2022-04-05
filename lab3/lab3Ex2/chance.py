import subprocess
import sys
from pathlib import Path

path = ""
month = ""
year = ""
country = ""

for param in sys.argv:
    splitted_param = param.split('=')
    if splitted_param[0].__eq__('-country'):
        country = splitted_param[1]
    elif splitted_param[0].__eq__('-path'):
        path = splitted_param[1]
    elif splitted_param[0].__eq__('-year'):
        year = splitted_param[1]
    elif splitted_param[0].__eq__('-month'):
        month = splitted_param[1]

txt = ''
try:
    txt = Path(path).read_text()
except FileNotFoundError as e:
    print('bad file')

param = f'"{month} {year} {country}"'
median = 0
population = 0
count_of_lines = 0
try:
    median = subprocess.check_output(
        f'java Process --project=3,4,7,5 | java Process --select={param}| java Process --project=4 | java Aggregate -median',
        text=True, input=txt, shell=True, universal_newlines=True)
    count_of_lines = subprocess.check_output(
        f'java Process --project=3,4,7,5 | java Process --select={param}| java Process --project=4 | java Aggregate -count',
        text=True, input=txt, shell=True, universal_newlines=True)
    population = subprocess.check_output(
        f'java Process --project=7,10 | java Process --select={country}| java Process --project=2 | java Aggregate -avg',
        text=True, input=txt, shell=True, universal_newlines=True)
except subprocess.CalledProcessError as e:
    if e.returncode == 2:
        print('bad input :c')
    if e.returncode == 1:
        print('bad params :/')

if float(median) != 0 and float(count_of_lines) != 0 and float(population) != 0:
    print(float(median) * float(count_of_lines) / float(population))
else:
    print('cant read')
