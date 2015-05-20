import re

pass_len = int(input())
password = input()

if len(password) < pass_len:
    print('NO')
else:
    if re.search('[a-z]', password) and re.search('[A-Z]', password) and re.search('\d', password):
        if len(re.sub('[a-zA-Z0-9]', '', password)) > 0:
            print('NO')
        else:
            print('YES')
    else:
        print('NO')