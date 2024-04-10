<script setup>
import {onMounted, shallowRef} from "vue";
import axios from "axios";
import {useFormStore} from "@/stores/form_store.js";

const fuel_type_headers = {
  CH2_350bar: "Compressed H2 (350 bar)",
  CH2_700bar: "Compressed H2 (700 bar)",
  LH2: "Liquid H2",
  Battery: "Battery",
  Diesel: "Diesel"
}

const travel_data_headers = {
  minutes_spent_refueling: 'Minutes spent refueling',
  number_of_refuels: 'Number of refuels during the trip',
  percent_left_in_tank: 'Percent of fuel left in the tank after the trip',
}
const refueling_data = shallowRef(null)
const store = useFormStore()
axios.defaults.baseURL = import.meta.env.VITE_DOMAIN

function set_table_data(response_data) {
  refueling_data.value = response_data
}

function fetch_data_from_api() {
  axios.post('/api/calculate/truck',
      store.get_store_as_json(), {
        headers: {
          'Content-Type': 'application/json'
        }
      }
  ).then(async function (response) {
    set_table_data(response.data);
  })

}

onMounted(() => {
  fetch_data_from_api();
})


</script>

<template>
  <div class="about">
    <h1>Results</h1>
  </div>

  <table v-if="refueling_data" class="table table-striped table-bordered">
    <thead>
    <tr>
      <th scope="col">fuel type</th>
      <th scope="col" v-for="datapoint_header in travel_data_headers">
        {{ datapoint_header }}
      </th>
    </tr>
    </thead>
    <tbody>
    <tr v-for="fuel_data in refueling_data" :key="fuel_data.type">
      <td></td>
      <template v-for='(datapoint) in fuel_data'>
        <td>
          {{ datapoint }}
        </td>

      </template>
    </tr>
    </tbody>
  </table>

  <button @click="fetch_data_from_api">reload</button>
</template>

<style scoped>

body {
  background-color: #f0f8ff; /* Light blue color */
}
.about {
  display: flex;
  flex-direction: column;
  align-items: center; /* Center horizontally */
  justify-content: center; /* Center vertically */
  height: 100vh; /* Set height to viewport height to center vertically */
}
table {
  width: 80%;
  border-collapse: collapse; /* Collapse table borders */
}

th {
  background-color: #f2f2f2; /* Light gray background */
  color: #333; /* Dark gray text color */
  padding: 8px; /* Add padding */
  text-align: left; /* Align text to the left */
  border-bottom: 1px solid #ddd; /* Add bottom border */
}

tbody tr:nth-child(even) {
  background-color: #f9f9f9; /* Alternate background color */
}

td {
  padding: 8px; /* Add padding */
  border-bottom: 1px solid #ddd; /* Add bottom border */
}

tbody tr:hover {
  background-color: #e9e9e9; /* Light gray background on hover */
}

button {
  background-color: #007bff; /* Blue background */
  color: #fff; /* White text color */
  border: none; /* Remove border */
  padding: 10px 20px; /* Add padding */
  cursor: pointer; /* Change cursor to pointer on hover */
  border-radius: 5px; /* Add border radius */
  margin-top: 10px; /* Add top margin */
}

button:hover {
  background-color: #0056b3; /* Darker blue background on hover */
}

</style>