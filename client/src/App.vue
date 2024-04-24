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

      <nav class="navbar">
        <ul class="nav navbar-right nav-pills">
          <li class="nav-item">
            <RouterLink to="/" class="nav-link">Home</RouterLink>
          </li>
          <li class="nav-item" v-if="is_visible">
            <RouterLink to="/results" class="nav-link">results</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink to="/sources" class="nav-link">sources</RouterLink>
          </li>
        </ul>
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
.nav-link{
  font-size: 3em;
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
    place-items: center;

  }

  .logo {
    margin: auto auto 2rem;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
  }

  nav {
    font-size: 1rem;
    padding: 1rem 10% 1rem;
  }
}

</style>
