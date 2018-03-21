'''
    Author: Kyle Ong
    Date: 03/17/2018

    heapify algorithms

    runtime: O(logn)
'''

def max_heapify(i, heap):
    '''
        Author: Kyle Ong
        Date: 03/17/2018

        max-heapify algorithm ~> enforces the max - heap property

        runtime: O(logn)

        type: i: int
        type: heap: arr[int]

    '''
    if i > capacity:return
    l = 2i+1
    r = 2i+2
    max = i if heap[i] > heap[r] else r
    max = max if heap[max] > heap[l] else l
    if max != i:
        max_heapify(max,heap)


def min_heapify(i,heap):
    '''
        Author: Kyle Ong
        Date:03/17/2018

        min-heapify algorithm ~> enforces the min-heap property

        runtime: O(logn)

        type: i: int
        type: heap: arr[int]
    '''
    if i > size: return
    l = 2i
    r = 2i + 1
    min = i if heap[i] < heap[l] else l
    min = min if heap[min] < heap[r] else r 
    if min != i:
        min_heapify(min,heap)