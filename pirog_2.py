
def getCount():
    peopleCount = ''
    while not peopleCount:
        ret = input('Количество посетителей. (q-exit)\n')
        if(ret == 'q'):
            exit()
        try:
            peopleCount = int(ret)
        except ValueError as err:
            print(f'Вводить только цифры.')
        else:
            return peopleCount

cnt = getCount()
#print(f'ret:{cnt}')

if cnt % 2:
    print(cnt // 2 + 1)
else:
    print(int(cnt / 2))