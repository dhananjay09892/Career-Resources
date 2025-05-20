# 1 pointer DSA Problems Structure 

def function(arr):
    h = {}
    for i in range(len(arr)):
        if arr[i] in h:
            h[arr[i]] += 1
        else:
            h[arr[i]] = 1
    return h
arr = [1,5,1,2,3,4,2,1,3,4,5,3,4,2,1,3,4,5]
print(function(arr))


#  2 Pointer DSA Problem 

def reverseArray(arr):
    i = 0
    j = len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr
print(reverseArray(arr))

def removeDuplicate(arr):
    if not arr:
        return []
    h = {}
    i = 1
    j = 0
    while i < len(arr):
        if arr[i] not in h:
            h[arr[i]] = 1
            j += 1
            arr[j] = arr[i]
        i += 1
    return arr[:j]
arr = [1,5,1,2,3,4,2,1,3,4,5,3,4,2,1,3,4,5]
print(removeDuplicate(arr))