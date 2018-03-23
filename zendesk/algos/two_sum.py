'''

    Author: Kyle Ong
    Date: 03/23/2018
'''


def two_sum(arr,target):
    ''' 
        Author: Kyle Ong
        Date: 03/22/2018

        runtime: O(n)
        space: O(n)

    '''
    ret = []
    if not arr: return ret
    dict = {}
    for i in range(0,len(arr),1):
        cmp = target - arr[i]
        if cmp in dict.keys():
            ret.append(dict[cmp])
            ret.append(i)
            break
        dict[arr[i]] = i

    return ret;