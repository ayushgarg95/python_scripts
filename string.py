#!/usr/bin/env python

# String Manipulation

st= 'i am, a, google  ,   aspirant   ,  i want to, get     , into  ,  google '
arr=st.split(',')

for i in arr:
	trim = i.strip()
	trimR=i.rstrip()
	trimL=i.lstrip()

	firstInitial = trim[:1]
	lastInitial = trim[1:2]
	lastName = trim[1:]
	
	print 'User : \'' + i + '\''
    	print 'LTrim: \'' + trimL + '\''
	print 'RTrim: \'' + trimR + '\''
	print ' Trim: \'' + trim + '\''
	print 'First Initial:', firstInitial.upper()
	print 'Last Initial: ', lastInitial.upper()
	print 'Last Name:', lastName

	print ''
