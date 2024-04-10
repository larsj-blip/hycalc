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

