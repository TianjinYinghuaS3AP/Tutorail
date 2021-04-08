# -*- coding: UTF-8 -*-

'''--------------------第一题--------------------'''

def doubleTheZero(arr):
    """
    doubleTheZero不返回任何值, 而是原地修改函数输入的数组arr
    """
    n = len(arr)
    i=0
    while(i<n):
        if arr[i] == 0:
            for j in range(n-1, i, -1):
                arr[j] = arr[j-1]
            i=i+1
        i+=1

'''--------------------第二题--------------------'''

def removeElement(arr, val):
    """
    removeElement不返回任何值, 而是原地修改函数输入的数组arr
    """
    while val in arr:
        arr.remove(val)

'''--------------------第三题--------------------'''

def checkIfExist(self, arr):
    """
    函数返回布尔值
    """
    set_mult = set()
    zero_occ = 0
    for i in arr:
        if i == 0:
            zero_occ += 1
        set_mult.add(i * 2)
        
        # second pass
    for i in arr:
        if i in set_mult:
            if i == 0:
                if zero_occ < 2: # edge case where there are two or more zeros
                    continue
                else:
                    return True
            return True
    return False