'''
Author: Kyle Ong
Date: 11/05/2017

Problem: Given a arrayList[String] sort based off of major.minor.revision

type: arrayList[String]
rtype: arrayList[String]

example:
 input - ["1.1.2", "1.1.3", "1.1.0", "0.1.1"]
 output - ["0.1.1", "1.1.0", "1.1.2", "1.1.3"]

constraints:
	- every element is gauranteed a major
	- every element is gauranteed a revision if it has a minor
	- every element is [1...100]

'''

import sys

def sort(l):
	'''
		Author: Kyle Ong
		Date: 11/05/2017

		sorts l based off of major.minor.revision

		type: l : arrayList[String]
		rtype: ret: arrayList[String]

		will return [] if l is invalid

		time: O(n^2)
		space: O(n)
	'''
	ret = []
	array = stringToArray(l)
	if not isValidInput(array): return ret
	print array
	ints = stringArraytoIntArray(array)
	ints = sorted(ints)
	
	ret = intArrayToStringArray(ints)

	print ret

	return sorted(ret)

def intArrayToStringArray(l):
	'''
		Author: Kyle Ong
		Date: 11/05/2017

		converts arrayList[Int] to arrayList[String]

		time: O(n)
		space: O(n)

		type: l : arraylist[Int]
		rtype: ret: arrayList[String]

		will return [] if input is invalid

		example:
		l : [1.0, 1.1.2]
		ret : ["1.0", "1.1.2"]

	'''
	ret = []
	if not l: return ret
	for i in xrange(len(l)):
		string = ""
		for j in xrange(len(l[i])):
			if j == len(l[i]) - 1:
				string += str(l[i][j])
			else:
				string += str(l[i][j])
				string += "."
		ret.append(string)
	return ret

def stringArraytoIntArray(l):
	'''
		Author: Kyle Ong
		Date: 11/05/2017

		converts arrayList[String] to arrayList[int]

		type: l : arrayList[string]
		rtype: arrayList[int]

		will return [] if the input is not valid
	'''
	ret = []
	for i in xrange(len(l)):
		tmp = []
		split = l[i].split('.')
		for j in xrange(len(split)):
			tmp.append(int(split[j]))
		ret.append(tmp)
	return ret


def stringToArray(s):
	'''
		converts a given string s to an arrayList[String]

		type: s : string
		rtype: ret : arrayList[int]

		time: O(n)
		space O(n)

		will return [] if s is empty
	'''
	ret = []
	tmp = s.split(',')
	for i in xrange(len(tmp)):
		ret.append((tmp[i]))
	return ret

def isValidInput(l):
	'''
		Author: Kyle Ong
		Date: 11/05/2017

		validates the input

		time: O(n)
		space: O(1)

		type: l: arrayList[string]
		rtype: Bool

	'''
	if not l: return False
	
	for i in xrange(len(l)):
		tmp = l[i].split(".")
		for j in xrange(len(tmp)):
			if not int(tmp[j]) > 0 and not int(tmp[j]) <= 100: 
				return False

	return True



try:
	userInput = sys.argv[1]
	sort(userInput)
except:
	print "Invalid Usage %s. Comma-separated String; 1.2.3,1.4.5,2.4.5 " %sys.argv[0]






