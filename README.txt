IspByCountry (iPython Notebook)
	ispByCountry 
		Inputs - ip2l filename, and an optional parameter to indicate whether to filter the data to only include ISPs available for Mobile (True), to filter those ISPs out (False), or to not filter the data (None) which is the default
		Output - A "2D" dictionary linking 2 digit ip2l country code to ISP to number of ip addresses registered
			(ex - result["US"]["ISP A"] reveals the 144 ip addresses assigned to ISP A in the US)

IspBySegment (iPython Notebook)
	group
		Inputs - A dictionary of group names to a list of group members (by 2 digit ip2l country code), and a 2D dictionary as the result of ispByCountry
		Outputs - A 2D dictionary linking segment name to ISP to number of ip addresses registered
			(ex - result["NORTH AMERICA"]["ISP A"] reveals the 256 ip addresses assigned to ISP A in North America (including the 144 from the US as shown above))
		
	ispBySegment
		Inputs - ip2l filename, and a 2D dictionary as returned from ispByCountry (pre-calculated)
		Outputs - A 2D dictionary linking segment name to ISP to number of ip addresses registered
			
analyticSummary (Python file)
	analyticSummary
		Inputs - A 2D dictionary in the format output by ispBySegment and ispByCountry
		Outputs - A dictionary linking group name (either Segment or Country Code) to its mean and standard deviation respectively
			
merge (Python file)
	merge_dicts
		Inputs - A list of 2D dictionaries to be merged into a single 2D dictionary
		Output - A 2D dictionary containing the aggregated data from the inputs
		
	agg
		Inputs - A country name and a list of 2D dictionaries to be merged
		Output - A dictionary of ISPs to number of ip addresses reserved for that country and ISP combo
			
split (Python file)
	split
		Inputs - A filename and maximum number of lines you want in each split file
		Output - None, though it saves each split file in Data/Split/data_x.csv (for x [1:n] as needed)
		Note - Used to allow parallelization of ispByCountry

Terminal (iPython Notebook)
	Used to actually run the above code (either in chunks or sequentially). 
	Divided into "Whole Dataset", "Mobile", and "No Mobile" each of which includes calls to ispByCountry and ispBySegment as well as analyicSummary in both cases
	
nbImport (Python file)
	Allows iPython notebooks to be imported as "normal" modules (ie - using import)