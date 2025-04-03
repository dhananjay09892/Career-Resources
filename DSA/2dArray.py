Arr = [
    [1 ,2 ,3 ,4 ,5 ,6 ],
    [7 ,8 ,9 ,10,11,12],
    [13,14,15,16,17,18],
    [19,20,21,22,23,24]
]
# This code is a simple 2D array traversal using DFS and BFS algorithms.

def print2DArray(arr):
    for row in arr:
        print(" ".join(map(str, row)))
        

def traversalDfs(arr):
    rows = len(arr)
    cols = len(arr[0]) if rows > 0 else 0
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    result = []
    direction = [[-1,0],[0,1],[1,0],[0,-1]]

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c]:
            return
        visited[r][c] = True
        result.append(arr[r][c])
        for dr, dc in direction:
            nr, nc = r + dr, c + dc
            dfs(nr, nc)

    dfs(0, 0)
    return result

print("DFS Traversal:", traversalDfs(Arr))

def traversalBfs(arr):
    rows = len(arr)
    cols = len(arr[0]) if rows > 0 else 0
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    result = []
    queue = [(0, 0)]
    direction = [[-1,0],[0,1],[1,0],[0,-1]]

    while queue:
        r, c = queue.pop(0)
        if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c]:
            continue
        visited[r][c] = True
        result.append(arr[r][c])
        for dr, dc in direction:
            nr, nc = r + dr, c + dc
            queue.append((nr, nc))

    return result

print("BFS Traversal:", traversalBfs(Arr))

# General 2D Array Functions

# 1. Find the maximum element in a 2D array
def findMax(arr):
    max_val = float('-inf')
    for row in arr:
        for elem in row:
            if elem > max_val:
                max_val = elem
    return max_val
print("Maximum Element:", findMax(Arr))

# 2. Find the minimum element in a 2D array
def findMin(arr):
    min_val = float('inf')
    for row in arr:
        for elem in row:
            if elem < min_val:
                min_val = elem
    return min_val
print("Minimum Element:", findMin(Arr))

# 3. Calculate the sum of all elements in a 2D array
def sumArray(arr):
    total = 0
    for row in arr:
        for elem in row:
            total += elem
    return total
print("Sum of Elements:", sumArray(Arr))

# 4. Calculate the average of all elements in a 2D array
def averageArray(arr):
    total = sumArray(arr)
    count = len(arr) * len(arr[0]) if arr else 0
    return total / count if count > 0 else 0
print("Average of Elements:", averageArray(Arr))

# 5. Transpose a 2D array
def transposeArray(arr):
    if not arr:
        return []
    return [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]
print("Transposed Array:")
print2DArray(transposeArray(Arr))

# 6. Rotate a 2D array 90 degrees clockwise
def rotateArray(arr):
    if not arr:
        return []
    return [[arr[len(arr)-1-j][i] for j in range(len(arr))] for i in range(len(arr[0]))]
print("Rotated Array:")
print2DArray(rotateArray(Arr))

# 7. Rotate a 2D array 90 degrees counter-clockwise
def rotateArrayCounterClockwise(arr):
    if not arr:
        return []
    return [[arr[j][len(arr[0])-1-i] for j in range(len(arr))] for i in range(len(arr[0]))]
print("Rotated Array Counter-Clockwise:")
print2DArray(rotateArrayCounterClockwise(Arr))

# 8. Rotate a 2D array 180 degrees
def rotateArray180(arr):
    if not arr:
        return []
    return [[arr[len(arr)-1-i][len(arr[0])-1-j] for j in range(len(arr[0]))] for i in range(len(arr))]
print("Rotated Array 180 degrees:")
print2DArray(rotateArray180(Arr))

# 9. Check if a 2D array is symmetric
def isSymmetric(arr):
    if not arr:
        return True
    rows = len(arr)
    cols = len(arr[0])
    for i in range(rows):
        for j in range(cols):
            if arr[i][j] != arr[rows-1-i][cols-1-j]:
                return False
    return True
print("Is the array (Arr) symmetric?", isSymmetric(Arr))
Arr2 = [
    [1, 2, 3],
    [2, 1, 2],
    [3, 2, 1]
]
print("Is the array (Arr2) symmetric?", isSymmetric(Arr2)) 

# 10. Check if a 2D array is square
def isSquare(arr):
    return len(arr) == len(arr[0]) if arr else False
print("Is the array (Arr) square?", isSquare(Arr))
print("Is the array (Arr2) square?", isSquare(Arr2))

# 11. Flatten a 2D array into a 1D array
def flattenArray(arr):
    return [elem for row in arr for elem in row]
print("Flattened Array:", flattenArray(Arr))