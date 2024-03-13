import { defineStore } from 'pinia'
import {ref} from 'vue'

export const useFormStore = defineStore('form_store', ()=> {
  const distance_traveled = ref(0)
  const payload_weight = ref(0)
  function update_form_store(updated_distance, updated_payload) {
      distance_traveled.value = updated_distance
      payload_weight.value = updated_payload
      console.log(payload_weight.value)
    }
  return {distance_traveled, payload_weight, update_form_store}
})
  //   TODO: set data in store from form
      // what we have:  volume, hydrogen prices,
      // input = distance,  cargo weight
    // output = for each hydrogen type(300, 700bar + liquid), diesel, elektrisk:
  //            antall refuels;



