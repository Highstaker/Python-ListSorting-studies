#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-
import sys
from time import time

def recursion_limit(limit):
	def wrapper(f):
		#Stuff here is run when declaring a decorated function
		def func(*args):
			#And this is run when the function is run
			initial_limit = sys.getrecursionlimit()
			sys.setrecursionlimit(limit)
			f(*args)
			sys.setrecursionlimit(initial_limit)
		return func
	return wrapper

def print_time(f):
	def wrapper(*args):
		start_time = time()
		result = f(*args)
		time_taken = time() - start_time
		print("Time taken for {0} : {1} seconds".format(f.__name__, time_taken))
		return result
	return wrapper