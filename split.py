f_read = open("Data/DB24-IP-COUNTRY-REGION-CITY-LATITUDE-LONGITUDE-ZIPCODE-TIMEZONE-ISP-DOMAIN-NETSPEED-AREACODE-WEATHER-MOBILE-ELEVATION-USAGETYPE.CSV/IP-COUNTRY-REGION-CITY-LATITUDE-LONGITUDE-ZIPCODE-TIMEZONE-ISP-DOMAIN-NETSPEED-AREACODE-WEATHER-MOBILE-ELEVATION-USAGETYPE.CSV")

f_write = open("Data/Split/data_1.csv","w")
count = 0
ind = 1
for line in f_read:  
	if count < 1900000:
		f_write.write(line)
	elif count == 1900000:
		ind = ind + 1
		f_write.close()
		f_write = open("Data/Split/data_"+str(ind)+".csv","w")
		f_write.write(line)
		count = -1
	count = count + 1

f_read.close()
f_write.close() 