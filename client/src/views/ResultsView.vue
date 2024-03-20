<script setup>
import {onMounted, ref} from "vue";

axios.defaults.baseURL = process.env.BASE_URL;



import axios from "axios";
import {useFormStore} from "@/stores/form_store.js";
import process from "@vueform/vueform/src/config/index.js";

const store = useFormStore()
const transport_types = ["Battery", "CH2_350bar", "CH2_700bar", "Diesel", "LH2"]
const calculations = ref({
  headers: ["minutes_spent_refueling", "number_of_refuels", "percent_left_in_tank"],
  data: {}
  // data:
  //   {
  //     "minutes_spent_refueling": {'Battery': 0.0, 'CH2_350bar': 0.0, 'CH2_700bar': 0.0, 'Diesel': 0.0, 'LH2': 0.0},
  //     "number_of_refuels": {'Battery': 0, 'CH2_350bar': 0, 'CH2_700bar': 0, 'Diesel': 0, 'LH2': 0},
  //     "percent_left_in_tank": {'Battery': 74, 'CH2_350bar': 87, 'CH2_700bar': 87, 'Diesel': 95, 'LH2': 89},
  //   }
})

onMounted(()=> {
  axios.post('/api/calculate/truck',
    store.get_store_as_json(), {
      headers: {
        'Content-Type': 'application/json'
      }
    }
).then(function (response) {
  calculations.data = response.data;
    console.log(response.data)
})

})

console.log(calculations.data)



</script>

<template>
  <div class="about">
    <h1>Results</h1>
  </div>

  <table class="table table-striped table-bordered">
    <thead>
    <tr>
      <th scope="col">type</th>
      <th scope="col" v-for="header in calculations.headers">{{ header }}</th>
    </tr>
    </thead>
    <tbody>
    <tr v-if="calculations.data" v-for="locomotion_type in transport_types">
      <th scope="row">{{ locomotion_type }}</th>
      <td v-for='datapoint in calculations.headers'>{{ calculations.data[datapoint][locomotion_type] }}</td>
    </tr>
    </tbody>
  </table>

</template>

