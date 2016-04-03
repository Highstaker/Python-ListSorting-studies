#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-
import unittest
from random import randint
from bubblesort import BubbleSort
from quicksort import QuickSort
from mergesort import MergeSort

RANDOM_LIST_LENGTH = 5000

L1 = [2,7,3,1,8,5,6,4]
L1s = sorted(L1)
L2 = [randint(1, 10000000) for i in range(RANDOM_LIST_LENGTH)]
L2s = sorted(L2)

class TestBubblesort(unittest.TestCase):

	def test_bubblesort_class_singleton(self):
		a = BubbleSort()
		b = BubbleSort()
		self.assertEqual(id(a),id(b))

	def test_bubblesort(self):

		self.assertEqual(BubbleSort()(L1), L1s)

		self.assertEqual(BubbleSort()(L2), L2s)


class TestQuicksort(unittest.TestCase):

	def test_quicksort_class_singleton(self):
		a = QuickSort()
		b = QuickSort()
		self.assertEqual(id(a),id(b))

	def test_quicksort(self):
		self.assertEqual(QuickSort()(L1), L1s)

		for i in range(1):
			self.assertEqual(QuickSort()(L2), L2s)


class TestMergesort(unittest.TestCase):

	def test_mergesort_class_singleton(self):
		a = MergeSort()
		b = MergeSort()
		self.assertEqual(id(a),id(b))

	def test_mergesort(self):
		self.assertEqual(MergeSort()(L1), L1s)

		for i in range(1):
			self.assertEqual(MergeSort()(L2), L2s)

if __name__ == '__main__':
	unittest.main()