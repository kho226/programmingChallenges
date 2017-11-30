'''
Author: Kyle Ong
Date: 11/16/2017

Floyd-Warshall Algorithm

runtime: O(n^3)

finds the all pairs of shortest paths

- sets all shortest paths with k = 0 intermediate nodes equal to infinity
- for every edge the shortest path with k = 0 intermediate edges is equal to l(u,v)
- for [1..k] we compute the shortest distance between nodes with k = [1...k] intermediate vertices

essentially dijkstra's except with keep track of the intermediate vertices

def l(u,v):
	- finds the length of the edge between nodes u and v
	- edge is directed

def dist(i,j,k):
	- finds the shortest distance between the ith node and the jth node given k intermediate vertices

dist(i,j,k) = min(dist(i,k,k-1), dist(i,j,k-1), dist(k,j,k-1))
 	- find the minimum value of all your sub-problems

'''