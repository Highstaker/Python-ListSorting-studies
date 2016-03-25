#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-
import sys
from decorators import print_time

class QuickSort(object):
	"""docstring for QuickSort"""
	def __init__(self):
		super(QuickSort, self).__init__()

	def __call__(self,L):
		l = L.copy()
		return self.quickSort(l)

	@print_time
	def quickSort(self,l):
		l_len = len(l)

		#Have to set a big recursion limit, or the program crashes.
		initial_limit = sys.getrecursionlimit()
		temp_limit = l_len*10
		if temp_limit > initial_limit:
			sys.setrecursionlimit(temp_limit)

		result = self._quickSort(l,0,l_len-1)

		sys.setrecursionlimit(initial_limit)

		return result
	
	def _quickSort(self, l, start, end):
		# No need to try to sort a one-item or empty list
		if end <= start:
			return l

		pivot = start
		left_caret = start+1
		right_caret = end

		while True:
			#Move left caret until it jumps OVER the right one or until its value is greater than that of pivot
			while left_caret <= right_caret and l[left_caret] <= l[pivot]:
				left_caret += 1

			#Move right caret until it jumps OVER the lefy one or until its value is less than that of pivot
			while left_caret <= right_caret and l[right_caret] >= l[pivot]:
				right_caret -= 1

			#If one caret jumped over another
			if left_caret > right_caret:
				# Jump out of the loop
				break
			else:
				#No, they did not. Switch values of left and right carets and continue moving them.
				l[left_caret], l[right_caret] = l[right_caret], l[left_caret]

		# A jump-over happened. Switch values of pivot and what used to be right caret
		l[pivot], l[right_caret] = l[right_caret], l[pivot]

		#The right caret becomes a divisor
		divisor = right_caret

		# perform the same routine with lists to the left and to the right of the divisor
		l = self._quickSort(l,start,divisor-1)
		l = self._quickSort(l,divisor+1,end)

		return l

if __name__ == '__main__':
	L1 = [2,7,3,1,8,5,6,4]
	print(QuickSort()(L1))