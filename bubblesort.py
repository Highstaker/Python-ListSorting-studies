#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-

from decorators import print_time, Profile

class BubbleSort(object):
	"""docstring for BubbleSort"""

	instance = None

	def __new__(cls, L=None):
		if cls.instance is None:
			cls.instance = super(BubbleSort, cls).__new__(cls)
		return cls.instance

	def __init__(self, L=None):
		super(BubbleSort, self).__init__()
		if L:
			self(L)

	def __call__(self,L):
		l = L.copy()
		return self.bubbleSort(l)

	@classmethod
	# @Profile
	@print_time
	def bubbleSort(cls,l):
		while True:
			l, n = cls._bubbleRunThrough(l)
			if n == 0:
				break
		return l

	@staticmethod
	def _bubbleRunThrough(l):
		swaps_n = 0
		for caret in range(len(l)-1):
			if l[caret] > l[caret+1]:
				l[caret], l[caret+1] = l[caret+1], l[caret]
				swaps_n += 1
		return l, swaps_n

if __name__ == '__main__':
	L1 = [2,7,3,1,8,5,6,4]
	print(BubbleSort()(L1))
