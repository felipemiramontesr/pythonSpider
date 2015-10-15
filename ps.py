#!usr/bin/python
import GeoIP 
import time

from sys import argv

tic = time.clock()
#file = open('data.txt','w+')

for ra in range(177,178):
	for rb in range(0,256):
		for rc in range(0,256):
			for rd in range(0,256):
				a=str(ra)
				b=str(rb)
				c=str(rc)
				d=str(rd)
				gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)
				#print('IP-> '+a+'.'+b+'.'+c+'.'+d+' was localized in:-> '	
					#+gi.country_name_by_addr(a+'.'+b+'.'+c+'.'+d))	
#file.close()
toc = time.clock()

processTimeSeconds = toc - tic
processTimeMinutes = (processTimeSeconds / 60)
processTimeHours = (processTimeSeconds / 60) / 60

processTimeDays = ((processTimeSeconds / 60) / 60) / 24

processTimeString = str(processTimeSeconds)
processTimeStringMinutes = str(processTimeMinutes)
processTimeStringHours = str(processTimeHours)
processTimeStringDays = str(processTimeDays)

print('Process time: ' + processTimeString + ' Seconds, '
	  + processTimeStringMinutes + ' Minutes, ' 
	  + processTimeStringHours + ' Hours, '
	  + processTimeStringDays + ' Days.')