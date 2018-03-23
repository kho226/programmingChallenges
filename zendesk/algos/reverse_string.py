'''
    Author: Kyle Ong
    Date: 03/23/2018

    reverse string ~> leetcode

'''

def reverse_string(x):
    '''
        Author: Kyle Ong
        Date: 03/23/2018

        rutime: O(n)
        space: O(n)

    '''
    ret = []
    if not x: return ret
    for i in range(len(x)):
        ret.append(x[i])
    ret.reverse()
    return ''.join(ret)