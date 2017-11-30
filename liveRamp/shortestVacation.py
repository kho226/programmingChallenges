'''
Author: Kyle Ong
Date: 11/05/2017

problem: given an array of integers, determine the shortest continuous sub-array that contains all values in the array

time: O(n)
space: O(n)

type: nums : arrayList[int]
rtype: trip: int

constraints:
- 0 < len(nums) < 100001
- 0 < nums[i] < len(nums) - 1

'''
try:
	import sys
except ImportError:
	raise ImportError("could not import sys")

def getLengthContinuousSubArray(nums):
	'''
		Author: Kyle Ong
		Date: 11/05/2017

		time: O(n)
		space: O(n)

		type: nums : arrayList[nums]
		rtype: trip: int

	'''
	array = stringToArray(nums)
	if not isValidInput(array): raise ValueError("Invalid Input")
	l1 = []
	l2 = []
	for i in xrange(len(array)):
		if array[i] not in l1:
			l1.append(array[i])
		elif l1.index(array[i]) == 0:
			l1.remove(array[i])
			l1.append(array[i])
		else:
			l1.append(array[i])
	for i in xrange(len(l1) - 1, -1, -1):
		if l1[i] not in l2:
			l2.append(l1[i])
		elif l2.index(l1[i]) == 0:
			l2.remove(l1[i])
			l2.append(l1[i])
		else:
			l2.append(l1[i])
	return len(l2)

def isValidInput(nums):
	'''
		Author: Kyle Ong
		Date: 11/05/2017

		type: nums: arrayList[int]
		rtype: Bool 

		time: O(n)
		space: O(1)

		verifies input based off of problem parameters
	'''
	if not (0 < len(nums) and len(nums) < 100001 ) or not nums: return False
	for i in xrange(len(nums)):
		if nums[i] > len(nums) - 1 or nums[i] < 0: return False
	return True

def stringToArray(s):
	'''
		converts a given string s to an arrayList[int]

		type: s : string
		rtype: ret : arrayList[int]

		time: O(n)
		space O(n)

		will return [] if s is empty
	'''
	ret = []
	tmp = s.split(',')
	for i in xrange(len(tmp)):
		ret.append(int(tmp[i]))
	return ret


'''command line tool'''

userInput = ""
try:
	userInput = sys.argv[1]
	getLengthContinuousSubArray(userInput)
except:
	print "Invalid usage %s; comman-separated string. Each value has to be in the range of [0,..N-1]" %sys.argv[0]










