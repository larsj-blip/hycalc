<script setup>
import {RouterLink, RouterView, useRouter} from 'vue-router'
import {ref} from "vue";
const router = useRouter()
const is_visible = ref(false);

function showResults() {
  router.push('/results')
}

function setResultLinkVisibility() {
  is_visible.value = true;
}

function navigateToResults() {
  setResultLinkVisibility();
  showResults();
}

</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125"/>

    <div class="wrapper">

      <nav>
        <button type="button" class="btn btn-link">
          <RouterLink to="/">Home</RouterLink>
        </button>
        <button type="button" class="btn btn-link" v-if="is_visible">
          <RouterLink to="/results">results</RouterLink>
        </button>
        <button type="button" class="btn btn-link">
          <RouterLink to="/sources">sources</RouterLink>
        </button>
      </nav>
    </div>
  </header>

  <RouterView @showResults="navigateToResults"/>
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}


nav a {
  display: inline-block;
  padding: 0 1rem;

}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;

  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
