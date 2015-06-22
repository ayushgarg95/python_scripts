#!/usr/bin/env python

x=raw_input('Enter a list of numbers separated by space: ')

# nums is an array which has each element of input
nums=x.split()

for i in nums:
	if not i.isdigit():
		print ' Not a number :',i
	else:
		print 'Numer :',i

