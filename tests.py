#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-
import unittest
from random import randint
from bubblesort import BubbleSort
from quicksort import QuickSort

RANDOM_LIST_LENGTH = 10000

L1 = [2,7,3,1,8,5,6,4]
L1s = sorted(L1)
L2 = [randint(1,10000000) for i in range(RANDOM_LIST_LENGTH)]
L2s = sorted(L2)

class TestBubblesort(unittest.TestCase):

	def test_bubblesort(self):
		# self.assertEqual(BubbleSort()(L1),L1s)

		# print(L2)			
		self.assertEqual(BubbleSort()(L2),L2s)
		# print(L2)			


class TestQuicksort(unittest.TestCase):
	def test_quicksort(self):
		# self.assertEqual(QuickSort()(L1),L1s)

		for i in range(1):
			# print(L2)
			self.assertEqual(QuickSort()(L2),L2s)
		# print(L2)



if __name__ == '__main__':
	unittest.main()