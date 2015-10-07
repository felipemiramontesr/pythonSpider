#!usr/bin/python
import GeoIP 
for ra in range(1,256):
	for rb in range(0,256):
		for rc in range(0,256):
			for rd in range(0,256):
				gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)
				a=str(ra)
				b=str(rb)
				c=str(rc)
				d=str(rd)
				print('IP-> '+a+'.'+b+'.'+c+'.'+d+' was localized in:-> '
					+gi.country_name_by_addr(a+'.'+b+'.'+c+'.'+d))