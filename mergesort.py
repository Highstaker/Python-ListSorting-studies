#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-
import sys

from decorators import print_time, Profile


class MergeSort(object):
	"""docstring for MergeSort"""

	instance = None

	def __new__(cls, L=None):
		if cls.instance is None:
			cls.instance = super(MergeSort, cls).__new__(cls)
		return cls.instance

	def __init__(self, L=None):
		super(MergeSort, self).__init__()
		if L:
			self(L)

	def __call__(self, L):
		l = L.copy()
		return self.mergeSort(l)

	@Profile
	@print_time
	def mergeSort(self, l):
		l_len = len(l)

		# Have to set a big recursion limit, or the program crashes.
		initial_limit = sys.getrecursionlimit()
		temp_limit = l_len*10
		if temp_limit > initial_limit:
			sys.setrecursionlimit(temp_limit)

		# Start splitting
		result = self._splitList(l)

		# Set the limit back
		sys.setrecursionlimit(initial_limit)

		return result


	def _splitList(self, l):
		"""
		Splits the list and calls the merging function that sorts the Splits
		"""

		# Once the splitter reaches a 1-element list, there is nothing to split. Simply return it.
		if len(l) <= 1:
			return l

		# Find the index of list's middle
		middle = len(l)//2

		# Get the left half of the list and repeat the splitting routine with it
		left = self._splitList(l[:middle])
		# Do the same with right part
		right = self._splitList(l[middle:])

		# Run the merging routine
		return self._merger(left, right)

	def _merger(self, l, r):
		"""
		Compares first elements of two lists 
		and reruns itself with a list and a slice of a list that had the smallest first element.
		If one of the lists is empty, simply returns the non-empty one.
		"""

		# If a list is empty, return another one
		if not l:
			return r
		if not r:
			return l


		# Compare first elements of lists
		if l[0] < r[0]:
			# If the first element of the left list is smaller than that of the right one,
			# take the left first element, rerun the routine with right list and slice of the left list
			# and append the result to the first element
			return [l[0]] + self._merger(l[1:], r)
		else:
			return [r[0]] + self._merger(l, r[1:])