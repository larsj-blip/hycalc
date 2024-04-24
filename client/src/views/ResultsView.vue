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
  price: 'Fuel costs (EUR)'
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
  <div class="heading">
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
    <template v-for="data_object in refueling_data" :key="data_object.type">
      <tbody>
      <tr data-test="result_row">
        <td>{{ fuel_type_headers[data_object.type] }}</td>
        <td v-for='(_, datapoint_name) in travel_data_headers' >
          {{ parseFloat(data_object[datapoint_name]).toFixed(0)}}
        </td>
      </tr>
      </tbody>
    </template>

  </table>

  <button @click="fetch_data_from_api">Reload</button>
</template>

<style scoped>
.heading {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 10vh;
}

table {
  margin: auto auto;
  width: 80%;
  border-collapse: collapse;
}

th {
  background-color: #f2f2f2;
  color: #333;
  padding: 8px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

tbody tr:nth-child(even) {
  background-color: #f9f9f9;
}

td {
  padding: 8px;
  border-bottom: 1px solid #ddd;
}

tbody tr:hover {
  background-color: #e9e9e9;
}

button {
  display: block;
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px 10px;
  cursor: pointer;
  border-radius: 5px;
  width: 10%;
  margin-left: auto;
  margin-right: auto;
}

button:hover {
  background-color: #0056b3;
}

</style>
