<script setup>

const calculations = {
  headers: ["hello", "yoo"],
  data: [
    {
      type: "car",
      hello: "hi",
      yoo: "y"
    },
    {
      type: "truck",
      hello: "boo",
      yoo: "ba"
    }
  ]
}
</script>

<template>
  <div class="about">
    <h1>Results</h1>
  </div>

  <table class="table table-striped table-bordered">
    <thead>
    <tr>
      <th scope="col" >type</th>
      <th scope="col" v-for="header in calculations.headers">{{ header }}</th>
    </tr>
    </thead>
    <tbody>
    <tr v-for="row in calculations.data">
      <th scope="row">{{row.type}}</th>
      <td v-for="column in calculations.headers">{{ row[column] }}</td>
    </tr>
    </tbody>
  </table>

</template>

