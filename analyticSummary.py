import statistics as stat
import pickle

def analyticSummary(data):
    result = {}
    for country in data:
        val = list(data[country].values())
        try:
            avg = stat.mean(val)
        except stat.StatisticsError:
            avg = 0
        try:
            std = stat.stdev(val)
        except stat.StatisticsError:
            std = 0
        except AssertionError:
            print(country)
            pickle.dump(val,open(country+".p","wb"))
            std = None
        result[country] = (avg,std)
    return result