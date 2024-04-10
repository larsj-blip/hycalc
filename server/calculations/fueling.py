import numpy as np
import json
import os
from dataclasses import dataclass
import typing

"""
    DATA
    _sourceX indicates the source in order per type of truck in the "data_data_data" google sheet
"""

#densities of hydrogen [kg/m3] NOT NECESSARY RN
density_CH2_350bar = 24.0 
density_CH2_700bar = 40.2
density_LH2 = 70.9

#volumes [L] NOT NECESSARY RN
volume_tank_350bar = 140 
volume_tank_400bar = 134 
n_tanks_350bar = 8
n_tanks_700bar = 6

#COMPRESSED HYDROGEN 
#350bar 
#range (full tank) [km]
r_350bar_source2 = 450
r_350bar_source3 = 1200
r_350bar_source4 = 800
r_350bar_list = [r_350bar_source2, r_350bar_source3, r_350bar_source4]
r_350bar_avg = np.average(r_350bar_list)

#range (full tank) [km]
rt_350bar_source4 = 18
rt_350bar_list = [rt_350bar_source4]
rt_350bar_avg = np.average(rt_350bar_list)

#weight of hydrogen per truck [kg] NOT NECESSARY RN
m_source1 = 26 
m_source2 = 33
m_source3 = 50
m_source4 = 55  
mH2_350bar_list = [m_source1, m_source2, m_source3, m_source4]
mH2_350bar_avg = np.average(mH2_350bar_list)

#fuel consumption [km/kgH2] NOT NECESSARY RN
fcon_source2 = 13.5
fcon_source3 = 12
fcon_source4 = 14
fcon_350bar_list = [fcon_source2, fcon_source3, fcon_source4]
fcon_350bar_avg = np.average(fcon_350bar_list)

#700bar
#range (full tank) [km]
r_700bar_source2 = 805
r_700bar_source3 = 1100
r_700bar_list = [r_350bar_source2, r_700bar_source3]
r_700bar_avg = np.average(r_700bar_list)

#refueling time [min]
rt_700bar_source2 = 20
rt_700bar_source3 = 18
rt_700bar_list = [rt_700bar_source2, rt_700bar_source3]
rt_700bar_avg = np.average(rt_700bar_list)

#weight of hydrogen per truck [kg] NOT NECESSARY RN
m_source1 = 30
m_source2 = 70
m_source3 = 85
mH2_700bar_list = [m_source1, m_source2, m_source3]
mH2_700bar_avg = np.average(mH2_700bar_list)

#fuel consumption [km/kgH2] NOT NECESSARY RN
fcon_source2 = 12
fcon_source3 = 13
fcon_700bar_list = [fcon_source2, fcon_source3]
fcon_700bar_avg = np.average(fcon_700bar_list)
    
#LIQUID HYDROGEN
#range (full tank) [km]
r_L_source2 = 1047 
r_L_source3 = 870
r_L_list = [r_L_source2, r_L_source3]
r_L_avg = np.average(r_L_list)

#refueling time [min]
rt_L_source1 = 12.5
rt_L_list = [rt_L_source1]
rt_L_avg = np.average(rt_L_list)

#weight of hydrogen per truck [kg] NOT NECESSARY RN
m_source2 = 88
m_source3 = 50
mH2_L_list = [m_source1, m_source2, m_source3]
mH2_L_avg = np.average(mH2_L_list)

#fuel consumption [km/kgH2]
fcon_source2 = r_L_source2 / m_source2
fcon_source3 = r_L_source3 / m_source3
fcon_L_list = [fcon_source2, fcon_source3]
fcon_L_avg = np.average(fcon_L_list)

#BATTERY
#range (full charge) [km]
r_bat_source2 = 531.1
r_bat_source3 = 241.4
r_bat_list = [r_bat_source2, r_bat_source3]
r_bat_avg = np.average(r_bat_list)

#recharging time [min]
rt_bat_source1 = 20
rt_bat_source2 = 30
rt_bat_list = [rt_bat_source1, rt_bat_source2]
rt_bat_avg = np.average(rt_bat_list)

#power consumption [km/kWh] NOT NECESSARY RN
p_con_source1 = 0.3195
    
#DIESEL
#range (full tank) [km]
r_dies_source1 = 2172.6
r_dies_list = [r_dies_source1]
r_dies_avg = np.average(r_dies_list)

#refueling time [min]
rt_dies_source1 = 10
rt_dies_list = [rt_dies_source1]
rt_dies_avg = np.average(rt_dies_list)

#fuel consumption [km/L] NOT NECESSARY RN
fcon_dsl_source1 = 2.976

#average refueling/charging times list
rt_avg_list = [rt_350bar_avg, rt_700bar_avg, rt_L_avg, rt_bat_avg, rt_dies_avg]

#names
data_to_send = ["number_of_refuels", "percent_left_in_tank", "minutes_spent_refueling"]
types_of_trucks = ["CH2_350bar", "CH2_700bar", "LH2", "Battery", "Diesel"]

def calc_refueling(user_range):
    """
    Description:
        takes the input "user_range" to calculate 
        the number of refuels, time spent refueling 
        and procent left in tank
            
    Args:
        user_range: the input from the user with their desired trucking range (int, float)
    
    Returns:
        refueling (dict)
    """

    n_refuels_350 = user_range / r_350bar_avg
    n_refuels_700 = user_range / r_700bar_avg
    n_refuels_L = user_range / r_L_avg
    n_refuels_bat = user_range / r_bat_avg
    n_refuels_dies = user_range / r_dies_avg
    
    n_refuels_floats = [n_refuels_350, n_refuels_700, n_refuels_L, n_refuels_bat, n_refuels_dies]
    fuel_charge_left_list = []
    n_refuels_ints = []
    time_spent_refueling_ints = []
    all_data_list = [n_refuels_ints, fuel_charge_left_list, time_spent_refueling_ints]
    
    for i in range(len(n_refuels_floats)):
        n_refuels = n_refuels_floats[i]
        n_refuels_rounded = round(n_refuels, 2)
        fuel_charge_left = (1 - (n_refuels - int(n_refuels_rounded))) * 100
        n_refuels_ints.append(int(n_refuels))
        fuel_charge_left_list.append(int(fuel_charge_left))
        time_spent_refueling_ints.append(int(n_refuels) * rt_avg_list[i])
    
    all_data_dict = {}
    for i in range(len(data_to_send)):
        idict = {}
        for j in range(len(types_of_trucks)):
            idict[types_of_trucks[j]] = all_data_list[i][j]
        all_data_dict[data_to_send[i]] = idict
        
    return all_data_dict

@dataclass
class RealWorldData:
    object_type: str
    id: str
    value: int
    unit: str
    
    @staticmethod
    def get_real_worl_data(input_json):
                    
        object_type = input_json["object_type"]
        irl_id = input_json["id"]
        value = input_json["value"]
        unit = input_json["unit"]

        return RealWorldData(object_type, irl_id, value, unit)

@dataclass
class TruckData:
    id: str
    type_powertrain: str
    source: str
    data: list[RealWorldData]
    
    @staticmethod
    def from_json(input_json):

        id = input_json["id"]
        type_powertrain = input_json["type_powertrain"]
        source = input_json["source"]
        irl_data = []
        
        for el in input_json["data"]:
            json_rwd = input_json["data"][el]            
            irl_data.append(RealWorldData.get_real_worl_data(json_rwd))
        
        data_obj = TruckData(id, type_powertrain, source, irl_data)
        
        return data_obj


if __name__ == '__main__':

    f = open("server/data/truck_data.json")

    data = json.load(f)
    truck_data = TruckData.from_json(data)
    print(truck_data)