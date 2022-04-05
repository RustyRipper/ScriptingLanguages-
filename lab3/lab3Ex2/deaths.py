import subprocess
import sys
from pathlib import Path

n = 0
path = ""
option = ""
country = ""
output = ""

for param in sys.argv:
    new_param = param.split('=')
    if new_param[0].__eq__('-country'):
        country = new_param[1]
    elif new_param[0].__eq__('-path'):
        path = new_param[1]
    elif new_param[0].__eq__('-option'):
        if new_param[1].__eq__('h') or new_param[1].__eq__('l'):
            option = new_param[1]
    elif new_param[0].__eq__('-n'):
        if new_param[1].isdigit():
            n = int(new_param[1])

txt = ''
try:
    txt = Path(path).read_text()
except FileNotFoundError as e:
    print('bad file')

try:
    output = subprocess.check_output(f' java Process --project=3,4,6,7 | java Process --select={country}',
                                     text=True, input=txt, shell=True, universal_newlines=True)
except subprocess.CalledProcessError as e:
    if e.returncode == 2:
        print('bad input :c')
    if e.returncode == 1:
        print('bad params :/')

array = output.split('\n')

f = open('f1.txt', 'w')

dict = {}
for line in array:
    splitted_array = line.split(' ')
    if len(splitted_array) > 1:
        month = splitted_array[0]
        year = splitted_array[1]
        key = f'{month} {year}'
        if not dict.get(key):
            dict[key] = 0, 0

        actual_deaths = (dict[key])[0]
        new_deaths = int(splitted_array[2])
        actual_count = (dict[key])[1]

        dict[key] = (actual_deaths + new_deaths, actual_count + 1)

# item[1][0] : deaths
# item[1][1] : count
sorted_dict = sorted(dict.items(), key=lambda item: item[1][0] / item[1][1], reverse=True)

for key, value in sorted_dict:
    avg = 0
    count = value[1]
    if count != 0:
        deaths = value[0]
        avg = deaths/count
    f.write('(month year)=%s\t(avg_deaths)=%.2f\t(deaths, amount_days)=%s\n' % (key, avg, value))

f = open("f1.txt", "r")
txt = Path('f1.txt').read_text()
if option.__eq__('h'):
    output = subprocess.run(f"java Head --lines={n} -e", text=True, input=txt)
elif option.__eq__('l'):
    output = subprocess.run(f"java Tail --lines={n} -e", text=True, input=txt)
