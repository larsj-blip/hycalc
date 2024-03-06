<template>
  <div class="Hello">
    <h1>{{ msg}}</h1>
  </div>
</template>



<script>
export default {
  name: 'hello',
  data() {
    return {
      msg: 'Hello!',
    };
  },
};
</script>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>