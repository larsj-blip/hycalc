import numpy as np

"""
    DATA
    _sourceX indicates the source in order per type of truck in the "data_data_data" google sheet
"""

#average CO2 emissions per km from different types of trucks from source1
em_4UD = 814.1
em_4RD = 627.0
em_4LH = 786.4
em_5RD = 861.7
em_5LH = 783.5
em_9RD = 696.9
em_9LH = 873.3
em_10RD = 854.1
em_10LH = 806.5

emissions_list = [814.1, 627.0, 786.4, 861.7, 783.5, 696.9, 873.3, 854.1, 806.5]
emissions_avg_per_km = np.average(emissions_list)

def calc_emissions(user_range):
    total_emissions = user_range * emissions_avg_per_km
    return total_emissions