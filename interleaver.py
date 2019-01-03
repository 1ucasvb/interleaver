from collections import deque
from math import log2, ceil, pow

# List interleaver for progressive rendering of 1D data | Lucas V. B.
# Returns a vector from (start) to (end), inclusive.
# No restrictions at all on start or end values, other than being integers.
# Useful for "progressive rendering", by picking values at finer and finer resolutions last
# Example:
#     Interleaver1D(0,10)
# {0, 10, 5, 2, 7, 1, 3, 6, 8, 4, 9}
def Interleaver1D(start, end):
	start, end = min(start, end), max(start, end)
	sec =  [0,0]
	order = []
	secs = deque()
	
	# Size of interval
	w = end - start
	
	# If negative, invalid, return empty list
	if w < 0: return order
	
	# First and last items go first
	order.append(start)
	if w == 0: return order
	order.append(end)
	
	# If anything else, we interleave recursively
	if w > 1:
		# Create a subinterval
		secs.appendleft(start+1)
		secs.appendleft(end-1)
		while len(secs):
			sec[0] = secs.pop()
			sec[1] = secs.pop()
			w = sec[1] - sec[0]
			if w == 0:
				order.append(sec[0])
				continue
			if w == 1:
				order.append(sec[0])
				secs.appendleft(sec[1])
				secs.appendleft(sec[1])
				continue
			c = (sec[0] + sec[1]) // 2
			order.append(c)
			secs.appendleft(sec[0])
			secs.appendleft(c-1)
			secs.appendleft(c+1)
			secs.appendleft(sec[1])
	
	return order


# Array interleaver for progressive rendering of 2D data | Lucas V. B.
# Returns a vector with vector pairs of ints coordinates (x,y) filling the (width,height) rectangle
# progressively.
# width and height must be positive and non-zero, but any number is fine.
# Useful for "progressive rendering", by picking values at finer and finer resolutions last.
# Example:
#     Interleaver2D(4,5)
# [ [0,0], [0,4], [2,2], [2,0], [2,4], [0,2], [1,1], [3,3], [3,1], [1,3], [1,0],
#  [1,4],[3,2],[3,0],[3,4],[1,2],[0,1],[2,3],[2,1],[0,3] ]

def Interleaver2D(width, height):
	order = []
	levels = ceil(max( log2(width), log2(height) ))
	t = width*height
	n = 0
	while len(order) < t:
		k = n
		x, y = 0, 0
		for i in range(levels):
			d = k // int(pow(4, levels - i - 1))
			k -= int(pow(4, levels - i - 1)) * d
			x += (1 if (d == 1 or d == 2) else 0) * (1 << i)
			y += (d % 2) * (1 << i)
		if x < width and y < height:
			order.append((x,y))
		n += 1
	return order
