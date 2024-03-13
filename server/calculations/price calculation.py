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
Price_electricity = data['price'][20]
Electricity_needed = 0.05 #MWh needed to produce 1 kg of hydrogen


def cost_of_producing_1_kg_hydrogen():
    return (Price_electricity * Electricity_needed)

#Next we need to know how much it will cost to pressurize hydrogen to 350 (41 kg) or 700 (61.66)bar

#Compressing hydrogen from 20 bar to 350 bar requires 1.05 kWh/kg H2

#Liquid requires 10-13 KWh/kg LH2
Check_engine_variable = ""
Cost_per_kg = 0
User_input_distance = 0

def cost_of_your_engine_per_kg():
    if (Check_engine_variable == "treefifty"):
        Cost_per_kg = cost_of_producing_1_kg_hydrogen()+1.05*41*Price_electricity
        return Cost_per_kg
    elif (Check_engine_variable == "seveno"):
        Cost_per_kg = cost_of_producing_1_kg_hydrogen()+1.05*61.66*Price_electricity
        return Cost_per_kg

    elif (Check_engine_variable == "Liquid"):
        Cost_per_kg = cost_of_producing_1_kg_hydrogen()+10*56*Price_electricity
        return Cost_per_kg


def total_cost_of_driving_your_vehicle():
    #350: 13.166 km/kg H2
    #700: 12.5 km/kg
    #Liquid: 14.65 km/kg
    if (Check_engine_variable == "treefifty"):
        Total_cost = Cost_per_kg * User_input_distance/13.166 # kg hydrogen som trengs per kilometer kjørt
        return Total_cost
    elif (Check_engine_variable == "seveno"):
        Total_cost = Cost_per_kg * User_input_distance / 12.5  # kg hydrogen som trengs per kilometer kjørt
        return Total_cost

    elif (Check_engine_variable == "Liquid"):
        Total_cost = Cost_per_kg * User_input_distance / 14.65  # kg hydrogen som trengs per kilometer kjørt
        return Total_cost


if __name__ == "__main__":


    print(total_cost_of_driving_your_vehicle()) # Price is in euro








