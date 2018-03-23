'''

    Author: Kyle Ong
    Date: 03/23/2018

    runtime: O(n)
    space: O(n)
'''

def reverse_integer(x):
    '''
        Author: Kyle Ong
        Date: 03/23/2018

        type: x: int

        rtype: int

        will return 0 if reversed integer overflows signed 32 bit

    '''
    ret = 0
    if not x: return ret

    tmp = x*-1 if x < 0 else x

    while tmp > 0:
        ret *= 10
        ret += tmp % 10
        tmp = int(tmp/10)
    
    ret = ret*-1 if x < 0 else ret
    if ret.bit_length() >= 32: ret = 0
    return ret

