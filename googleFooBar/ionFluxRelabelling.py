'''
Author: Kyle Ong
Date: 11/11/2017

Problem: Given an arrayList[Int] representing a post-order traversal of a perfect binary tree return the parent associated with each TreeNode
 
type: q: arrayList[Int]
type: h: int 



time : O(n)
space : O(n)

'''

import math, sys

def answer(h,q):
	'''
		Author: Kyle Ong
		Date: 11/11/2017

		time: O(n)
		space O(n)

		type: h: int
		type: q: arrayList[int]

		rtype: ret: arrayList[int]

		will return [] if input is invalid
	'''
	ret = []
	head = int(math.pow(2,h)) - 1
	for i in xrange(len(q)):

		if (q[i] < head and q[i] >= 1):
			print q[i]
			parent = findParent(head,q[i],head-1)
			
			ret.append(parent)
			print ret
		else: 

			ret.append(-1)
			print ret
	print ret
	return ret

def findParent(head,target,step):
	'''
		Author: Kyle Ong
		Date: 11/14/2017

		type: head: int
		type: target: int
		type: step: int

		runtime: O(logn)
		space: O(1)
	'''
	step = step / 2 #the difference at each level is euqual to 2^(h-1) - 1
	lChild = head - 1 - step
	rChild = head - 1
	step -=1
	if lChild == target or rChild == target: return head
	elif target <= rChild:
		return findParent(rChild,target,step)
	else:
		return findParent(lChild,target,step)	


def arrayToIntArray(l):
	'''

		Author: Kyle Ong
		Date: 11/14/2017


		type: l: arrayList[string]
		type: ret: arrayList[int]

		runtime: O(n)
		space: O(n))

	'''
	ret = []
	if not l: return ret
	for i in xrange(len(l)):
		try:
			ret.append(int(l[i]))
		except ValueError:
			print("Invalid string representation. %s" %l[i])
	return ret


try:
	userInput = sys.argv[1]
	tmp = userInput.split(',')
	q = arrayToIntArray(tmp[1:])
	h = int(tmp[0])
	answer(h,q)
except:
	print("Invalid useage %s. Comma separated string. 3,0,1,2,3. " %sys.argv[0])

