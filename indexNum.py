import numpy as np

#python listの場合代入しただけでコピーされて別物になる
aL = [x for x in range(10)]
#print(aL)
alc = aL[:]
alc[0] = 100
#print(aL, alc)

#numpy の場合スライスを代入しても参照渡しで新しい変数で値を変えると元の変数も変化してしまう
nmlist = np.arange(10)
nmlists = nmlist[:]
nmlists[0] = 100
#print(nmlist, nmlists)
nmcopy = nmlist[:].copy()
nmcopy[0] = 200
#print(nmlist, nmcopy)

bls = np.array([2, 4, 6, 7])
#print(bls[np.array([True,True,True,False])])
#print(bls[bls % 3 == 1])

testabs = np.array([4,-9,16,-4,20])
testabs = np.abs(testabs)
#print(testabs, np.exp(testabs), np.sqrt(testabs))

arr1=[2,4,5,6,7,9,2,4]
arr2=[1,3,4,5,6,7,9]
# uniqueは重複したものをなくす
arrue = np.unique(arr1)
#print(arrue)
# union1dは和集合
#print(np.union1d(arrue, arr2))
# intersect1dは積集合
#print(np.intersect1d(arrue, arr2))
#  setdiff1dは差集合
#print(np.setdiff1d(arrue, arr2))

from numpy.random import randint

a = randint(0,11, (2,3))
#print(a)

arr = np.array([[1,2,3,4],[5,6,7,8]])
#print(arr.shape)

#print(arr.reshape(4,2))

# axis 0は縦で1は横
#print(arr.sum(axis=0), arr.sum(axis=1))

#ファインシーインデックス参照
arr = np.arange(25).reshape(5,5)
#print(arr[[1,3,0]])

# 転置行列
arr = np.arange(10).reshape(2,5)
#print(arr.T)

#sort
arr = np.array([15,30,5])
#print(arr, arr.argsort()) # sortとインデックス番号を返す 5,15,30 -> 

# 行列計算
arr = np.arange(9).reshape(3,3)
print(arr)
print(np.dot(arr,arr))
vec = arr.reshape(9)
print(np.linalg.norm(vec))

arr = np.arange(4).reshape(2,2)
print(arr)
vec = arr.reshape(4)
print(np.linalg.norm(vec))