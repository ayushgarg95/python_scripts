#!/usr/bin/env python
import urllib2

properties = {}

properties['protocol'] = 'http'
properties['host'] = 'www.google.com'
properties['port'] = '80'
properties['path'] = '/trends/'

#the properties in this map represent the URL:
#http://www.google.com:80/trends/

url = properties['protocol'] + '://' + \
      properties['host'] + ':' + \
      properties['port'] + \
      properties['path']
      
print 'Reading URL', url


# ERROR IN THIS LINE !!!!!
response = urllib2.open(url)

print response.read()
