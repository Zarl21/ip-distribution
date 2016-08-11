def merge_dicts(dicts): #input: List of Dicts
	countries = []
	for dic in dicts: #Get all keys 
		countries = countries + list(dic.keys())
	countries = list(set(countries)) #remove duplicates
	
	final = {}
	for country in countries:
		final[country] = agg(country,dicts)
	return final
		
def agg(country,dicts): #Returns a dict of isp:# ips
	ret = {}
	isps = []
	for dic in dicts:
		temp = dic.get(country) #Is this country in this dict
		if temp is None:
			temp = []
		else:
			temp = list(temp.keys())
		isps = isps + temp
	isps = list(set(isps)) #Remove Duplicates
	
	for isp in isps: 
		ret[isp] = 0
		for dic in dicts:
			country_check = dic.get(country) #Is this country in this dict
			isp_check = 0
			if country_check is not None: #Country is in this dict
				isp_check = country_check.get(isp)
				if isp_check is None: #isp is not in this dict
					isp_check = 0
			ret[isp] = ret[isp] + isp_check
    
	return ret