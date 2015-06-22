#!/usr/bin/env python

#GCD calculator (recursive)

def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(b,a%b)

inp=raw_input('Enter numbers (space separated): ')
x=inp.split()

ans=int(x[0])

for i in x:
	ans = gcd(ans,int(i))
print 'GCD of input list is :',ans
