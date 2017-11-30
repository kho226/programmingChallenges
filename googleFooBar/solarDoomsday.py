'''

Solar Doomsday

Author: Kyle Ong
Date: 11/05/2017

Problem: Write a function answer(area) that represents the total area of solar panels and returns an arrayList[Int] of ints representing the maximum squares
Constraints:
- 0 < area < 1000000

type: area: Int
rtype : ret: arrayList[Int]

time: O(n)
space O(n)

example:
area = 12
ret = [9,1,1,1]


'''

try:
	import math
	import sys
except ImportError:
	raise ValueError("Could not import Math")

def answer(area):
	'''

		Author: Kyle Ong
		Date: 11/05/2017

		type: area: Int
		rtype: ret: arrayList[Int]

		type: area: int
		rtype: ret: arrayList[int]

		time: O(n)
		space O(n)

	'''
	ret = []
	if not isValidInput(area):
		raise ValueError("Invalid Input")
	maxArea = 0
	while area > 0:
		tmp = int(math.sqrt(area))
		maxArea = tmp * tmp
		area = area - maxArea
		ret.append(maxArea)
	print ret
	return ret

def isValidInput(area):
	'''
		Author: Kyle Ong
		Date: 11/05/2017

		Validates the input

		type: area: int
		rtype: Bool

		time: O(1)
		space: O(1)
	'''
	if not (0 < area and area < 1000000) or not area: return False
	return True

try:
	userInput = sys.argv[1]
	answer(int(userInput))
except:
	print "Invalid Usage %s. integer!!" %sys.argv[0]




