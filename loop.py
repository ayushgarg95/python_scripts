#!/usr/bin/env python

import random

ans=random.randint(1, 100)
num=0

while num != ans:
	num=int(raw_input('Guess the number :'))
	
	if num<ans:
		print 'Guess higher'
	elif num>ans:
		print 'Guess Lower'

print 'Correct!'
