'''
	Author: Kyle Ong
	Date: 11/29/2017

	problem: 
	- Given an array of integers determine how many 'permutations' it has
	- a 'permutation' is defined as an index P such that the summation of A[0] through A[P] is equal to the summation of 1 through P + 1

	runtime: 0(n)
	space: 0(1)

'''

def solution(A):
	'''
		Author: Kyle Ong
		Date: 11/29/2017

		type: A: arrayList[int]
		rtype: int

	'''
	p = 0
	perm = 0
	permCount = 0
	for i in xrange(len(A)):
		p += i + 1
		perm += A[i]
		if perm == p: permCount += 1
	return permCount