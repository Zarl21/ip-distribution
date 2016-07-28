def merge_dicts(dicts): #input: List of Dicts
	countries = []
	for dic in dicts: #Get all keys 
		countries = countries + list(dic.keys())
	countries = list(set(countries)) #remove duplicates
	
	final = {}
	for country in countries:
		final[country] = agg(country,dicts)
	return final
		
def agg(key,dicts):
	ret = {}
	isps = []
	for dic in dicts:
		temp = dic.get(key)
		if temp is None:
			temp = []
		else:
			temp = list(temp.keys())
		isps = isps + temp
	isps = list(set(isps))
	
	for isp in isps:
		ret[isp] = 0
		for dic in dicts:
			temp1 = dic.get(key)
			temp2 = 0
			if temp1 != None:
				temp2 = temp1.get(isp)
				if temp2 is None:
					temp2 = 0
			ret[isp] = ret[isp] + temp2
    
	return ret