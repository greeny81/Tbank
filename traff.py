#[int(input('')) for x in range(3)]

def inputData(count=0,rData=''):
    anot = ['Tarif cost (q-quit)\n','Traf in tarif (q-quit)\n','cost 1mb (q-quit)\n','traf next month (q-quit)\n']
    if(count):
        rnds = 3 - count
        retData = rData
    else:
        count = 0
        retData = {}
        rnds = 3
    print(f'NOW rnds {rnds}')
    for x in range(0, rnds):# 0 Должен вычислятся!!!!
        print(f'X:{x}')# ЮЗАТЬ Х как ключ
        try:
            ret = input(anot[count])
            if(ret == 'q'):
                exit()
            retData[count] = int(ret)
            print(f' cnt:{count} d:{retData}')
        except ValueError as err:
            print(f' {err} only num')
            inputData(count,retData)
        else:
            count += 1
            if(len(retData) == 4):
                print(f'ret:{retData} {len(retData)}')
                return retData
                exit()

#print(x)
a,b,c,d = inputData().values()
print(f'done {a} {b}')
