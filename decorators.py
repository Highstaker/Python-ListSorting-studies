#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-
from time import time
from memory_profiler import profile

USE_MEMORY_PROFILER = False  # if True, writes the profile of memory usage


def dummy(f):
	def wrapper(*args):
		result = f(*args)
		return result

	return wrapper


Profile = profile if USE_MEMORY_PROFILER else dummy


def print_time(f):
	def wrapper(*args):
		start_time = time()
		result = f(*args)
		time_taken = time() - start_time
		print("Time taken for {0} : {1} seconds".format(f.__name__, time_taken))
		return result

	return wrapper
