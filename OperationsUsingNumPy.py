import numpy as np
def replaceOdds(arr,arr_size):
    for i in range(0,arr_size):
     if arr[i] % 2 != 0:
        arr[i] == -1
    print(arr)
def arrSlicing(arr,arr_size):
    np.split(arr,arr_size,2,5)
    print(arr)
def sumOfArr(arr,arr_size):
    for i in range(0,arr_size):
        sum_ = sum(arr[i])
    print(sum_)
arr = [0,1,2,3,4,5,6,7,8,9]
arr_size = len(arr)
print(replaceOdds(arr,arr_size))
print(arrSlicing(arr))
print(sumOfArr(arr,arr_size)) 