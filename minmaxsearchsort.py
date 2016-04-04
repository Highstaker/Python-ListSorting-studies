#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-
import sys

from decorators import print_time, Profile

class MinMaxSearchSort(object):
	"""docstring for MinMaxSearchSort"""

	instance = None

	def __new__(cls, L=None):
		if cls.instance is None:
			cls.instance = super(MinMaxSearchSort, cls).__new__(cls)
		return cls.instance

	def __init__(self, L=None):
		super(MinMaxSearchSort, self).__init__()
		if L:
			self(L)

	def __call__(self, L):
		l = L.copy()
		return self.minMaxSearchSort(l)

	@staticmethod
	def _iextend(lst, index, value):
		lst[index:index] = value

	@staticmethod
	def _poptwo(lst, i1, i2):
		if i1 > i2:
			r1 = lst.pop(i1)
			r2 = lst.pop(i2)
		else:
			r2 = lst.pop(i2)
			r1 = lst.pop(i1)

		return [r1,r2,]

	@Profile
	@print_time
	def minMaxSearchSort(self, l):

		result = []
		result_len = 0

		while len(l) > 1:
			mn = 0
			mx = 0

			for n, i in enumerate(l):
				if i < l[mn]:
					mn = n 
				if i > l[mx]:
					mx = n

			self._iextend(result, result_len//2, self._poptwo(l, mn, mx))
			result_len += 2

		if l:
			self._iextend(result, result_len//2, [l[0]])

		return result


if __name__ == '__main__':
	L1 = [2,7,3,9,1,8,5,6,4]
	print(MinMaxSearchSort()(L1))