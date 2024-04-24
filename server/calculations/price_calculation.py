#Calculating the specific price of pure hydrogen
import requests
import time


def fetch_electricity_price():
    url = "https://api.energy-charts.info/price?bzn=DE-LU&start=2023-01-01T00%3A00%2B01%3A00&end=2023-01-01T23%3A45%2B01%3A00"
    response = requests.get(url)

    # Assuming the API response contains the price under the 'price' key
    data_json = response.json()
    return data_json

data = fetch_electricity_price()
#Price_electricity = data['price'][20] #Euro/MWh
Electricity_needed = 0.055 #MWh needed to produce 1 kg of hydrogen
Price_electricity = 190 #Euro/MWh



def cost_of_producing_1_kg_hydrogen():
    return (Price_electricity * Electricity_needed)

#Next we need to know how much it will cost to pressurize hydrogen to 350 (41 kg) or 700 (61.66)bar

#Compressing hydrogen from 20 bar to 350 bar requires 1.05 kWh/kg H2

#Liquid requires 10-13 KWh/kg LH2


# User_input_distance = 0 #Kilometer input i integer



Cost_per_kg_treehundred = cost_of_producing_1_kg_hydrogen()+0.00105*Price_electricity


Cost_per_kg_seveno = cost_of_producing_1_kg_hydrogen()+0.00135*Price_electricity


Cost_per_kg_liquid = cost_of_producing_1_kg_hydrogen()+0.01*Price_electricity  #MWh/kg * Euro/MWh




    #350: 13.166 km/kg H2
    #700: 12.5 km/kg
    #Liquid: 14.65 km/kg

#Price electricity = Euro/MWh
#INPUT USER DISTANCE





#All data in euros

def dictionary_fuction(User_input_distance):
    Total_cost_treefifty = User_input_distance * Cost_per_kg_treehundred / 13.166  # kg hydrogen som trengs per kilometer kjørt

    Total_cost_seveno = User_input_distance * Cost_per_kg_seveno / 12.5  # kg hydrogen som trengs per kilometer kjørt

    Total_cost_liquid = User_input_distance * Cost_per_kg_liquid / 14.65  # kg hydrogen som trengs per kilometer kjørt

    Total_cost_gas = User_input_distance * 0.10 * 2.172

    Total_cost_electric = User_input_distance * Price_electricity * 0.0011 #MWh/km

    Cost_dictionary = {
        "treefifty": Total_cost_treefifty,
        "sevenhundred": Total_cost_seveno,
        "liquid": Total_cost_liquid,
        "Gas": Total_cost_gas,
        "Electric": Total_cost_electric

    }

    return Cost_dictionary












