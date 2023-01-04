from collections import deque
from math import log2, ceil, pow

class Interleaver1D(object):
	"""
	List interleaver for progressive rendering of 1D data.
	An iterator that interleaves values from `start` to `end`, inclusive,
	ensuring `start` and `end` values are returned first.
	No restrictions at all on `start` or `end` values, other than being integers.
	This is useful for "progressive rendering" by picking coarse-grained values first,
	and finer resolutions last.
	
	Example:
		list(Interleaver1D(0, 10)) -> [0, 10, 5, 2, 7, 1, 3, 6, 8, 4, 9]
	"""
	def __init__(self, start: int, end: int) -> None:
		if not isinstance(start, int) or not isinstance(end, int):
			raise TypeError("Interleaver1D requires integer arguments.")
		start, end = min(start, end), max(start, end)
		self.secs = deque()
		self.secs.appendleft([start, start])
		if end-start >= 1:
			self.secs.appendleft([end, end])
		if end-start >= 2:
			self.secs.appendleft([start+1, end-1])
	
	def __iter__(self):
		return self
	
	def __next__(self):
		if not self.secs:
			raise StopIteration
		a, b = self.secs.pop()
		if a == b:
			return a
		c = (a + b)//2
		if a <= c-1:
			self.secs.appendleft([a, c-1])
		if c+1 <= b:
			self.secs.appendleft([c+1, b])
		return c

class Interleaver2D(object):
	"""
	Array interleaver for progressive rendering of 2D data | Lucas V. B.
	An iterator returning pairs of ints as coordinates (x,y) filling the (width,height) rectangle
	progressively. Values range from (0, 0) to (width-1, height-1).
	Width and height must be positive and non-zero, but any number is fine.
	Powers of two are ideal, as less values are skipped in the while loop.
	
	Useful for "progressive rendering", by picking values at finer and finer resolutions last.
	Example:
	    Interleaver2D(4,5) -> [(0,0), (0,4), (2,2), (2,0), (2,4), (0,2), (1,1),
	    (3,3), (3,1), (1,3), (1,0), (1,4),(3,2),(3,0),(3,4),(1,2),(0,1),(2,3),(2,1),(0,3)
	]
	
	"""
	def __init__(self, width: int, height: int) -> None:
		if not isinstance(width, int) or not isinstance(height, int) or width <= 0 or height <= 0:
			raise TypeError("Interleaver2D requires positive non-zero integer arguments.")
		self.width, self.height = width, height
		self.remaining = width*height
		self.count = 0
		self.levels = ceil(max(log2(width), log2(height))) # Recursion level
	
	def __iter__(self):
		return self
	
	def __next__(self):
		while self.remaining:
			k = self.count
			x, y = 0, 0
			for i in range(self.levels):
				d = k // int(pow(4, self.levels - i - 1))
				k -= int(pow(4, self.levels - i - 1)) * d
				x += (1 if (d == 1 or d == 2) else 0) * (1 << i)
				y += (d % 2) * (1 << i)
			self.count += 1
			if x < self.width and y < self.height:
				self.remaining -= 1
				return (x,y)
		raise StopIteration

