'''

    Author: Kyle Ong
    Date: 03/23/2018

    container with the most water from leetcode
'''

def container_with_most_water(arr):
    '''
        Author: Kyle Ong
        Date: 03/23/2018

        type: arr: arr[int]

        runtime: O(n)
        space: O(1)
    '''

    if not arr: return
    
    ret = 0

    tail = 0
    head = len(arr) - 1

    while tail < head:
        tmp = 0
        length = head - tail
        if arr[tail] < arr[head]:
            tmp = arr[tail] * length 
            tail += 1
        else:
            tmp = arr[head] * length
            head -= 1
        ret = ret if ret > tmp else tmp
    
    return ret 
