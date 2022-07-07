from collections import deque
from multiprocessing.dummy import current_process
from turtle import distance
R = 5
C = 3

class chamb:

	def __init__(self,m: int, n: int):
		self.m = m
		self.n = n

class queuex:
	def __init__(self,pt: chamb, distance: int):
		self.pt = pt
		self.distance = distance


def checkValid(row: int, col: int):
	return ((row >= 0) and (row < R) and (col >= 0) and (col < C))


rowNum = [1, 0, -1, 1]
colNum = [0, 1, 0, 1]


def Lee(matrix, source: chamb, destination: chamb):
	
	if matrix[source.m][source.n]!=1 or matrix[destination.m][destination.n]!=1:
		return -1
	
	visit = [[False for i in range(C)] for j in range(R)]
	 
	visit[source.m][source.n] = True
	
	q = deque()
	
	s = queuex(source,0)
	q.append(s)
	 
	while q:

		curr = q.popleft()
		
		pt = curr.pt
		if pt.m == destination.m and pt.n == destination.n:
			return curr.distance
		
		for i in range(4):
			row = pt.m + rowNum[i]
			col = pt.n + colNum[i]
			

			if (checkValid(row,col) and
			matrix[row][col] == 1 and
				not visit[row][col]):
				visit[row][col] = True
				Adjcell = queuex(chamb(row,col),curr.distance+1)
				q.append(Adjcell)
	 
	return -1

matrix = [
    [ 1, 0, 1, 0, 1, 0 ],
	[ 1, 0, 1, 0, 1, 0 ], 
	[ 1, 1, 0, 0, 1, 1 ], 
	[ 0, 0, 0, 0, 1, 1 ],
    ]

source = chamb(0,0)
destination = chamb(1,2)
	
distance = Lee(matrix,source,destination)
	
if distance!=-1:
		print("Length of the Shortest Path is",distance)
else:
		print("Shortest Path doesn't exist")
