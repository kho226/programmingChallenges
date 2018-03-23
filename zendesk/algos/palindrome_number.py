'''

    Author: Kyle Ong
    Date: 03/22/2018

    palindrome_number
'''

def palindrome_number(x):
    ''' 
        Author: Kyle Ong
        Date: 03/23/2018

        type: x: int
        rtype: ret: Bool

        runtime: O(n)
        space: O(n)

    '''
    ret = False
    if not x: return ret
    
    tmp = x
    p = 0

    while tmp > 0:
        p *= 10
        p += tmp % 10
        tmp = int(tmp/10)
    
    if p == x
        ret = True
    return ret
    
    