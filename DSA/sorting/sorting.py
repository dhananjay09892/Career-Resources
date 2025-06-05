# Bubble Sort
# performance analysis and implementation
def performance_analysis(func):
    """
    Decorator to analyze the performance of a sorting function.
    It measures the time taken to sort an array and returns the sorted array.
    """
    import time

    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken to sort: {end_time - start_time:.6f} seconds")
        return res

    return wrapper

@performance_analysis
def bubble_sort(arr):
    """
    Sorts an array using the bubble sort algorithm.
    This algorithm repeatedly steps through the list, compares adjacent elements,
    and swaps them if they are in the wrong order. The pass through the list is repeated
    until the list is sorted.
    Time Complexity: O(n^2) in the worst case.
    Space Complexity: O(1) as it sorts in place.
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

@performance_analysis
def selection_sort(arr):
    """
    Sorts an array using the selection sort algorithm.
    This algorithm divides the input list into two parts: a sorted and an unsorted part.
    It repeatedly selects the smallest (or largest) element from the unsorted part and moves it to the sorted part.
    Time Complexity: O(n^2) in the worst case.
    Space Complexity: O(1) as it sorts in place.
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

@performance_analysis
def insertion_sort(arr):
    """
    Sorts an array using the insertion sort algorithm.
    This algorithm builds a sorted array one element at a time by repeatedly taking the next element
    and inserting it into the correct position in the already sorted part of the array.
    Time Complexity: O(n^2) in the worst case.
    Space Complexity: O(1) as it sorts in place.
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i -1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j] 
            j-=1
        arr[j+1] = key
    return arr


@performance_analysis
def merge_sort(arr):
    """
    Sorts an array using the merge sort algorithm.
    This algorithm divides the array into halves, sorts each half, and then merges them back together.
    Time Complexity: O(n log n) in all cases.
    Space Complexity: O(n) due to the temporary arrays used for merging.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

@performance_analysis
def quick_sort(arr):
    """
    Sorts an array using the quick sort algorithm.
    This algorithm selects a 'pivot' element and partitions the array into two halves:
    elements less than the pivot and elements greater than the pivot, then recursively sorts the halves.
    Time Complexity: O(n log n) on average, O(n^2) in the worst case.
    Space Complexity: O(log n) due to recursive stack space.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sorted_arrays(left, right):
    """
    Merges two sorted arrays into one sorted array.
    This function is used in the merge sort algorithm.
    Time Complexity: O(n) where n is the total number of elements in both arrays.
    Space Complexity: O(n) due to the temporary array used for merging.
    """
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

@performance_analysis
def merge(arr):
    """
    Merges two sorted arrays into one sorted array.
    This function is used in the merge sort algorithm.
    Time Complexity: O(n) where n is the total number of elements in both arrays.
    Space Complexity: O(n) due to the temporary array used for merging.
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge(arr[:mid])
    right = merge(arr[mid:])
    
    return merge_sorted_arrays(left, right)

arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array using Bubble Sort:", bubble_sort(arr.copy()))
print("Sorted array using Selection Sort:", selection_sort(arr.copy()))
print("Sorted array using Insertion Sort:", insertion_sort(arr.copy()))
print("Sorted array using Merge Sort:", merge_sort(arr.copy()))
print("Sorted array using Quick Sort:", quick_sort(arr.copy()))
print("Sorted array using Merge:", merge(arr.copy()))

