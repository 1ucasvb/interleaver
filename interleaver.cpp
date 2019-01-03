#include <vector>
#include <queue>
#include <cmath>

// List interleaver for progressive rendering of 1D data | Lucas V. B.
// Returns a vector from (start) to (end), inclusive.
// No restrictions at all on start or end values, other than being integers.
// Useful for "progressive rendering", by picking values at finer and finer resolutions last
// Example:
//     Interleaver1D(0,10)
// {0, 10, 5, 2, 7, 1, 3, 6, 8, 4, 9}
std::vector<int> Interleaver1D(int start, int end) {
	std::vector<int> sec(2,0), order;
	std::queue<int> secs;
	int w, c;
	
	// Size of interval
	w = end - start;
	
	// If negative, invalid, return empty list
	if (w < 0) return order;
	
	// First and last items go first
	order.push_back(start);
	if (w == 0) return order;
	order.push_back(end);
	
	// If anything else, we interleave
	if (w > 1) {
		// Create a subinterval
		secs.push(start+1);
		secs.push(end-1);
		while (secs.size()) {
			sec[0] = secs.front(); secs.pop();
			sec[1] = secs.front(); secs.pop();
			w = sec[1] - sec[0];
			if (w == 0) {
				order.push_back(sec[0]);
				continue;
			}
			if (w == 1) {
				order.push_back(sec[0]);
				secs.push(sec[1]);
				secs.push(sec[1]);
				continue;
			}
			c = (sec[0]+sec[1]) / 2;
			order.push_back(c);
			secs.push(sec[0]); secs.push(c-1);
			secs.push(c+1); secs.push(sec[1]);
		}
	}
	
	return order;
}

// Array interleaver for progressive rendering of 2D data | Lucas V. B.
// Returns a vector with vector pairs of ints coordinates (x,y) filling the (width,height) rectangle
// progressively.
// width and height must be positive and non-zero, but any number is fine.
// Useful for "progressive rendering", by picking values at finer and finer resolutions last.
// Example:
//     Interleaver2D(4,5)
// { {0,0}, {0,4}, {2,2}, {2,0}, {2,4}, {0,2}, {1,1}, {3,3}, {3,1}, {1,3}, {1,0},
//  {1,4},{3,2},{3,0},{3,4},{1,2},{0,1},{2,3},{2,1},{0,3} }
std::vector< std::vector<int> > Interleaver2D(int width, int height) {
	std::vector< std::vector<int> > order;
	int levels = std::ceil(std::max( std::log2(width), std::log2(height) ));
	int t = width*height;
	int d, k, i, x, y, n = 0;
	while (order.size() < t) {
		k = n;
		x = 0; y = 0;
		for(i = 0; i < levels; i++) {
			d = k / (int)pow(4, levels-i-1);
			k -= (int)pow(4, levels-i-1)*d;
			x += (d == 1 || d == 2 ? 1 : 0) * (1 << i);
			y += (d % 2) * (1 << i);
		}
		if (x < width && y < height) {
			order.push_back( std::vector<int>(2,0) );
			order.back()[0] = x;
			order.back()[1] = y;
		}
		n++;
	}
	return order;
}

