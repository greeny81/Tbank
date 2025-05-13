from random import randint

kolNumbers = randint(1, 10)
kolOpers = 3

singleNums = []
doubleNums = []
tripleNums = []
quadsNums = []


nums = [ randint(1, 10000) for _ in range(kolNumbers) ]
print(nums)
sNums = sorted(nums)
for num in sorted(nums):
    if len(str(num)) == 1:
        singleNums.append(num)
    if len(str(num)) == 2:
        doubleNums.append(num)
    if len(str(num)) == 3:
        tripleNums.append(num)
    if len(str(num)) == 4:
        quadsNums.append(num)

print(singleNums, doubleNums, tripleNums, quadsNums)