o = open("Data/Split/data_8.csv","w")
for n in range(2,8):
	f = open("Data/Split/data_"+str(n)+".csv","r")
	s = f.readline()
	o.write(s)
	f.close()
o.close()