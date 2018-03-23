'''

    dp[i] = min(cost[i] + dp[i-1],cost[i] + dp[i-2])
'''

'''

    dp[i] = min(cost[i] + dp[i-1], cost[i] + dp[i-2])

~> example 1:
    cost = [0,1,2]
    dp = [0,1,2]

    ret = min(2,1) = 1
~> example 2:
    cost = [3,4,6,7]
    dp = [3,4,9,11]
    
    ret = min(9,11) = 9

'''

def min_cost_climbing_stairs(arr):
    '''
        Author: Kyle Ong
        Date: 03/22/2018

        runtime: O(n)
        space: O(n)

    '''
    if not arr: return 
    dp = [0] * len(arr)
    dp[0] = arr[0]
    dp[1] = arr[1]

    for i in range(2,len(arr),1):
        dp[i] = min(dp[i-1]+arr[i],dp[-2]+arr[i])

    return min(dp[-1],dp[-2]);