import numpy as np

#python listの場合代入しただけでコピーされて別物になる
aL = [x for x in range(10)]
print(aL)

alc = aL[:]
alc[0] = 100
print(aL, alc)
#numpy の場合スライスを代入しても参照渡しで新しい変数で値を変えると元の変数も変化してしまう
nmlist = np.arange(10)
nmlists = nmlist[:]
nmlists[0] = 100
print(nmlist, nmlists)
nmcopy = nmlist[:].copy()
nmcopy[0] = 200
print(nmlist, nmcopy)

bls = np.array([2, 4, 6, 7])
print(bls[np.array([True,True,True,False])])
print(bls[bls % 3 == 1])

testabs = np.array([4,-9,16,-4,20])
testabs = np.abs(testabs)
print(testabs, np.exp(testabs), np.sqrt(testabs))

arr1=[2,4,5,6,7,9,2,4]
arr2=[1,3,4,5,6,7,9]
arrue = np.unique(arr1)
print(arrue)


