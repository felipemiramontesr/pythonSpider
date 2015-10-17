'''
Script that extract IPs localizaed in México from IPV4 and calculate its time execution 
and prints it on screen.

Author: c. Mtro. Felipe de Jesús Miramontes Romero
date: October 17th, 2015. 
'''

#!usr/bin/python
import GeoIP 
import time

from sys import argv

# $tic, Tick time 1. 
tic = time.clock();

#Command to open the file (data_mx.txt) which is going to be manipulated.
file = open('data_mx.txt','w+')

# Four segment IP generator.
for ra in range(177,178):
	for rb in range(0,256):
		for rc in range(0,256):
			for rd in range(0,256):
				
				# -int- to -string- convertion.				
				a = str(ra)
				b = str(rb)
				c = str(rc)
				d = str(rd)
				
				#Command to assing a load database into memory, faster performance but uses more memory
				gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)
				
				# México code (MX) comparision to extract just "in México" geolocalizated IPs. 
				if gi.country_code_by_addr(a + '.' + b + '.' + c + '.' + d) == 'MX':

					#Command to writte the IP on the manipulated file (data_mx.txt).
					file.write(a + '.' + b + '.' + c + '.' + d + '\r\n')

# $toc, Tick time 2. 					
toc = time.clock();	

# $et, Execution time (Seconds).				
et = toc - tic;

# Command to print calculated execution time in minutes (et/60) and hours (et/60/60).
print ('Execution time: ' + et/60 + ' minutes,' + et/60/60 + ' hours.')

#Command to close the file which is manipulated.
file.close()