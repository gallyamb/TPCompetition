num = input()

if len(num) != 80:
    print('0' * 80)
else:
    if num[:4] == num[-4:] == '1111':
        print('0' * 80)
    elif num[-4:] == '1111':
        print(num[::-1])
    elif num[:4] == '1111':
        print(num)
    else:
        print('0' * 80)