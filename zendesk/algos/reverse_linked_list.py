'''
    new_node.next = prev
    prev = new_node
'''

def reverse_linked_list(head):
    '''
        Author: Kyle Ong
        Date: 03/24/2018

        reverses a singly linked list

        runtime: O(n)
        space: O(n)

    '''
    if not head: return
    
    res = None

    while head:
        insert = ListNode(head.val)
        insert.next = res
        res = insert
        head = head.next

    return res