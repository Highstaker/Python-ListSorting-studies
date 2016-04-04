#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-
import sys

from decorators import print_time, Profile

class HeapSort(object):
	"""docstring for HeapSort"""

	instance = None

	def __new__(cls, L=None):
		if cls.instance is None:
			cls.instance = super(HeapSort, cls).__new__(cls)
		return cls.instance

	def __init__(self, L=None):
		super(HeapSort, self).__init__()
		if L:
			self(L)

	def __call__(self, L):
		l = L.copy()
		return self.heapSort(l)

	def _minHeap(self, lst, length):
		start_node = length//2 - 1
		swapped = True # Just a placeholder to enter the loop

		while swapped:
			swapped = False

			for node in range(start_node, -1, -1):
				child1 = node * 2 + 1
				child2 = child1 + 1
				if lst[node] > lst[child1]:
					lst[node], lst[child1] = lst[child1], lst[node]
					swapped = True
				if child2 < length and lst[node] > lst[child2]:
					lst[node], lst[child2] = lst[child2], lst[node]
					swapped = True

	@Profile
	@print_time
	def heapSort(self, l):
		result = []
		length = len(l)

		while length > 1:
			self._minHeap(l, length)

			result.append(l.pop(0))
			l.insert(0, l.pop())
			length -= 1

		result.append(l.pop())
		return result



if __name__ == '__main__':
	L1 = [2,7,3,1,9,8,5,6,4]
	print(HeapSort()(L1))