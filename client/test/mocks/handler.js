import {HttpResponse, http } from 'msw'

export const data = [
{type: "CH2_350bar", number_of_refuels: 1, percent_left_in_tank: 77, minutes_spent_refueling: 18.0},
{type: "CH2_700bar", number_of_refuels: 1, percent_left_in_tank: 70, minutes_spent_refueling: 19.0},
{type: "LH2", number_of_refuels: 1, percent_left_in_tank: 95, minutes_spent_refueling: 12.5},
{type: "Battery", number_of_refuels: 2, percent_left_in_tank: 41, minutes_spent_refueling: 50.0},
{type: "Diesel", number_of_refuels: 0, percent_left_in_tank: 53, minutes_spent_refueling: 0.0},
]


export const handler = http.post('https://obscure-wildwood-11280-c9cda1944639.herokuapp.com/api/calculate/truck',
    () => {
    return HttpResponse.json(data, {status: 200})
    })