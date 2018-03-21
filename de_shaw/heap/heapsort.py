'''
    Author: Kyle Ong
    Date: 03/20/2018

    heapsort 

    runtime:O(nlogn)
    space: O(1)
'''

def max_heapify(arr,s,i):
    '''
        Author: Kyle Ong
        Date: 03/20/2018

        runtime: O(logn)
        space: O(1)

        type: arr: array[int]
        type: s: int
        type: i: int
    '''
    if i > s : return
    l = 2*i + 1
    r = 2*i + 2
    max = 0
    max = i if arr[i] > arr[l] else l
    max = max if arr[max] > arr[r] else r
    if max != i:
        tmp = arr[max]
        arr[max] = arr[i]
        arr[i] = arr[max]
        max_heapify(arr,s,i)

def heap_sort(arr,s):
    '''
        Author: Kyle Ong
        Date: 03/20/2018

        runtime:O(nlogn)
        space:O(1)

        type: arr: array[int]
        type: s: int

    '''
    for i in range(s/2-1,-1,1):
        max_heapify(arr,s,i)
    for i in range(s-1,-1,1):
        tmp = arr[i]
        arr[i] = arr[0]
        arr[0] = tmp
        max_heapify(arr,s,0)