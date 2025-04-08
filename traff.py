#[int(input('')) for x in range(3)]
def inputData(elem=0,rData=''):
    anot = ['Tarif cost (q-quit)\n','Traf in tarif (q-quit)\n','cost 1mb (q-quit)\n','traf next month (q-quit)\n']
    if(elem):
        rnds = 4 - elem
        count = elem
        retData = rData
    else:
        count = 0
        retData = {}
        rnds = 4

    for x in range(rnds):
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
                print(f'ret:{retData}')
                return retData

#print(x)
a,b,c,d = inputData().values()
print(f'done {a} {b}')
