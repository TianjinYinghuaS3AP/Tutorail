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

def checkIfExist(arr):
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



'''--------------------第四题--------------------'''

'''
把每个arr中的元素都替换成那个元素右边元素中的值最大的元素，如果右边没有元素，则将那个元素替换为-1
'''

def replaceElements(arr):
    """
    replaceElements返回修改后的arr
    """
    final=[]
    #for any arr with small length than 1
    if len(arr)<1:
        return [-1]
    else:
        for i in range(len(arr)):
            final.append(max(arr[i:]))
        #rightmost indexed element won't have any higher value
        final.append(-1)
        #when you are selecting max it will consider from first index but in our case we are only looking at greatest element on right side 
        return(final[1:])

def replaceElements_2(self, arr):
        """
        第二种解法
        """
        max_right = arr[len(arr)-1]
        arr[len(arr)-1] = -1
        for i in range(len(arr)-2,-1,-1):
            temp = arr[i]
            arr[i]=max_right
            if max_right<temp:
                max_right=temp
                
        return arr