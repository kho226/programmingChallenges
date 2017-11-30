'''
Author: Kyle Ong
Date: 11/05/2017

Problem: Given an array of integers, which represent the heights of buildings. determine how many horizontal strokes needed to paint the skyline!

type: nums: arrayList[int]
rtype: strokes: int

time: O(n)
space: O(1)

constraints:
 - 0 <= len(nums) <= 1000000000
 - 0 <= nums[i] <= 1000000000
 - 0 <= strokes <= 10000000000

 Algorithm:
 We observe that the number of strokes only increases when the current height is more than the previous
 We do not need to update the number of strokes when the current height is less than the previous

 - Verify input based off of problem constraints
 - iterate through input
 - handle two cases
 	- 1. if current height is more than previous
 	- 2. if current height is les than previous
 - handle edge cases
 - return strokes

'''

try:
	import sys
except ImportError:
	raise ImportError("cannot import sys")

def getHorizontalStrokes(nums):
	'''
		gets the number of horizontal strokes required to paint the skyline represented as an arrayList[int] (nums)

		type: nums : arrayList[int]
		rtype: strokes : int

		time: O(n)
		space: O(1)

		will return -1 if nums does not comply with the constraints of the problem
	'''

	array = stringToArray(nums)
	if not isValidInput(array):
		raise ValueError("Invalid Input")

	strokes = 0
	constraint = 0
	for i in xrange(len(array)):
		current = array[i]
		if strokes > 1000000000:
			raise ValueError("Invalid input")
		if current > constraint: 
			strokes += current - constraint
			constraint = current
		elif current < constraint:
			constraint = current
	print strokes
	return strokes		

def isValidInput(nums):
	'''
		type: nums: arrayList[Int]
		rtype: Boolean

		time: O(n)
		space: O(1)
	'''

	if not nums:
		return False
	if not (len(nums) >= 1 and len(nums) <= 1000000000): 
		raise ValueError("Invalid Input")
	for i in xrange(len(nums)):
		if nums[i] > 1000000000:
			return False
	return True



def stringToArray(s):
	'''
		converts string s to arrayList[int]

		type: s : string
		rtype: ret : arrayList[int]

		time: O(n)
		space: O(n)

		will return an empty arrayList if not s

	'''
	ret = []
	tmp = s.split(',')
	for i in xrange(len(tmp)):
		ret.append(int(tmp[i]))
	return ret

userInput = ""
try:
	userInput = sys.argv[1]
	getHorizontalStrokes(userInput)
except:
	print ("Usage: %s comma-separated string" %sys.argv[0])


