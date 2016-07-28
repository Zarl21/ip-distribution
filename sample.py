f_read = open("Data/DB24-IP-COUNTRY-REGION-CITY-LATITUDE-LONGITUDE-ZIPCODE-TIMEZONE-ISP-DOMAIN-NETSPEED-AREACODE-WEATHER-MOBILE-ELEVATION-USAGETYPE.CSV/IP-COUNTRY-REGION-CITY-LATITUDE-LONGITUDE-ZIPCODE-TIMEZONE-ISP-DOMAIN-NETSPEED-AREACODE-WEATHER-MOBILE-ELEVATION-USAGETYPE.CSV")

f_write = open("data_7.csv","w")
count = 0

for line in f_read:
    
	if count == 14000000:
		break
	elif count >= 12000000:    
		f_write.write(line)
        
	count = count + 1

f_read.close()
f_write.close()