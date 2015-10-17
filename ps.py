#!usr/bin/python
import GeoIP 
import time

from sys import argv

file = open('data_mx.txt','w+')

for ra in range(177,178):
	for rb in range(0,256):
		for rc in range(0,256):
			for rd in range(0,256):
								
				a=str(ra)
				b=str(rb)
				c=str(rc)
				d=str(rd)
				
				gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)

				if gi.country_code_by_addr(a + '.' + b + '.' + c + '.' + d) == 'MX':
					file.write(a + '.' + b + '.' + c + '.' + d + '\r\n')
file.close()
