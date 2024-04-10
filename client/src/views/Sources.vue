<script setup>
import {onMounted, shallowRef} from "vue";
import axios from "axios";
import {useFormStore} from "@/stores/form_store.js";


<template>
    <div class="sources1">
      <h2>Sources for calculating hydrogen price</h2>
      <ul>
        <li>Werner Zittel; Reinhold Wurster (1996-07-08). "Chapter 3: Production of Hydrogen. Part 4: Production from electricity by means of electrolysis".</li>
        <li>Bjørnar Kruse; Sondre Grinna; Cato Buch (2002-02-13). "Hydrogen – Status and Possibilities". The Bellona Foundation</li>
        <li> realto.io: Connect to spot market price electricity across Europe <li>

      </ul>
    </div>
  </div>
</template>

<template>
    <div class="sources2">
      <h2>Sources for  calculating number of refuels</h2>
      <ul>
        <li> </li>
        <li></li>
        <!-- Add more sources as needed -->
      </ul>
    </div>
   </div>
</template>

<template>
    <div class="sources3">
      <h2>Sources for calculating minutes spent refueling</h2>
      <ul>
        <li> </li>
        <li></li>
      </ul>
    </div>
  </div>
</template>


<style>
.content {
  /* Your styling for the content section */
}

.sources1 {
  margin-top: 50px; /* Adjust margin as needed */
}

.sources1 h2 {
  font-size: 1.5em; /* Adjust font size as needed */
}

.sources ul {
  list-style-type: none;
  padding: 0;
}

.sources1 li {
  margin-bottom: 10px; /* Adjust margin as needed */
}

.sources1 a {
  text-decoration: none;
  color: #007bff; /* Link color */
}

.sources1 a:hover {
  text-decoration: underline;
}
</style>