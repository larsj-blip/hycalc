<script setup>
import { onUpdated, ref, } from 'vue'
import { useFormStore } from '../stores/form_store.js'

const form_store = useFormStore()
const distance_traveled = ref(0);
const payload_weight = ref(0);



onUpdated(() =>{console.log(distance_traveled.value)
update_values_in_store()
})

function update_values_in_store() {
  form_store.update_form_store(distance_traveled.value, payload_weight.value)
}
</script>

<template>

  <form>
    <label for="distance_traveled">Distance traveled</label>
    <input type="number" id="distance_traveled"v-model="distance_traveled" placeholder="100"/>
    <label for="payload_weight">Payload weight</label>
    <input type="number" id="payload_weight" v-model="payload_weight" placeholder="400"/>
  </form>


</template>

<style scoped>


</style>