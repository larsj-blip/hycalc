# Calculating the specific price of pure hydrogen
import requests


def fetch_electricity_price():
    url = "https://api.energy-charts.info/price?bzn=DE-LU&start=2023-01-01T00%3A00%2B01%3A00&end=2023-01-01T23%3A45%2B01%3A00"
    response = requests.get(url)

    # Assuming the API response contains the price under the 'price' key
    data_json = response.json()

    return data_json


# Next we need to know how much it will cost to pressurize hydrogen to 350 (41 kg) or 700 (61.66)bar

# Compressing hydrogen from 20 bar to 350 bar requires 1.05 kWh/kg H2

# Liquid requires 10-13 KWh/kg LH2


# User_input_distance = 0 #Kilometer input i integer


# 350: 13.166 km/kg H2
# 700: 12.5 km/kg
# Liquid: 14.65 km/kg


# INPUT USER DISTANCE


#
# Total_cost_treefifty = User_input_distance* Cost_per_kg_treehundred  / 13.166 # kg hydrogen som trengs per kilometer kjørt
#
#
# Total_cost_seveno = User_input_distance* Cost_per_kg_seveno / 12.5  # kg hydrogen som trengs per kilometer kjørt
#
#
# Total_cost_liquid = User_input_distance*Cost_per_kg_liquid / 14.65 # kg hydrogen som trengs per kilometer kjørt
#
# #Calculating gas
#
# Total_cost_gas = User_input_distance* 0.10 *21.72
#
# Total_cost_electric = User_input_distance*Price_electricity*0.20

def cost_of_producing_1_kg_hydrogen(price_electricity, electricity_needed):
    return price_electricity * electricity_needed


def dictionary_function(user_input_distance):
    data = fetch_electricity_price()
    # price_electricity = data['price'][20]
    price_electricity = 190 #average price from 2023
    electricity_needed = 0.05  # MWh needed to produce 1 kg of hydrogen

    cost_per_kg_treehundred = cost_of_producing_1_kg_hydrogen(price_electricity,
                                                              electricity_needed) + 0.00105 * price_electricity

    cost_per_kg_seveno = cost_of_producing_1_kg_hydrogen(price_electricity,
                                                         electricity_needed) + 0.00135 * price_electricity

    cost_per_kg_liquid = cost_of_producing_1_kg_hydrogen(price_electricity,
                                                         electricity_needed) + 0.01 * price_electricity

    total_cost_treefifty = (
                user_input_distance * cost_per_kg_treehundred / 12.65)  # kg hydrogen som trengs per kilometer kjørt

    total_cost_seveno = (
            user_input_distance * cost_per_kg_seveno / 12)  # kg hydrogen som trengs per kilometer kjørt
    total_cost_liquid = (
            user_input_distance * cost_per_kg_liquid / 11.9)  # kg hydrogen som trengs per kilometer kjørt
    total_cost_gas = user_input_distance * 0.10 * 2.172
    total_cost_electric = user_input_distance * price_electricity * 0.0011

    cost_dictionary = {
        "CH2_350bar": total_cost_treefifty,
        "CH2_700bar": total_cost_seveno,
        "LH2": total_cost_liquid,
        "Battery": total_cost_electric,
        "Diesel": total_cost_gas,
    }

    return cost_dictionary
# km * (eur / kg) / (kg / km)
