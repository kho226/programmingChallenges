'''
Author: Kyle Ong
Date: 03/17/2017

algorithm implements runner - trailer method to detect cycles in a linked list

runtime: O(n)
space: O(1)

'''

def detect_cycle(head):
    '''
        Author: Kyle Ong
        Date: 03/17/2018

        detects cycles in a linked list

        type: head: linked list node
        type: ret: Bool

    '''

    ret = False
    if not head: return ret

    runner = head
    trailer = head

    while runner.next:
        runner = runner.next
        if runner.val == trailer.val:ret = True
        if runner.next: runner = runner.next
        trailer = trailer.next

    return ret