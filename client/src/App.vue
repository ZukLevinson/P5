<template>
  <div id="app">
    <navbar />

    <router-view />
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import Navbar from "./components/Navbar.vue";

@Component({
  components: {
    Navbar,
  },
})
export default class App extends Vue {}
</script>

<style lang="scss">
html,
body {
  margin: 0;
}

#app {
  display: flex;
  flex-direction: column;
  width: 100vw;
  height: 100vh;
  color: white;
  font-family: "Open Sans", sans-serif;

  background: rgb(43, 28, 42);
  background: radial-gradient(
    circle,
    rgba(43, 28, 42, 1) 0%,
    rgba(2, 0, 36, 1) 100%
  );

  & > * {
    flex: 1 1 auto;
  }
}

a {
  text-decoration: none !important;
  color: inherit;
}

[fill-width] {
  width: 100%;
}

[fill-height] {
  height: 100%;
}

[flex-row] {
  display: flex;
  flex-direction: row;

  & > * {
    flex: 1 1 auto;
  }
}

[flex-column] {
  display: flex;
  flex-direction: column;

  & > * {
    flex: 1 1 auto;
  }
}

[no-stretch] {
  flex: 0 !important;
}

[fill-height] {
  height: 100%;
}

[lg1] {
  flex: 1 !important;
}

[lg12] {
  flex: 12 !important;
}

[lg3] {
  flex: 3 !important;
}

[lg6] {
  flex: 6 !important;
}

[lg8] {
  width: 66.667%;
  flex: 8 !important;
}

[lg2] {
  width: 16.667%;
  flex: 2 !important;
}

[mg3] {
  margin: 2em;
}

[pd3] {
  padding: 1em;
}

[pd2] {
  padding: 0.6em;
}

[pd1] {
  padding: 0.3em;
}

[mg3] {
  margin-right: 1em;
}

[text-center] {
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
}

h1 {
  margin: 3px;
  line-height: 0.8em;
  font-size: 2em;
}

h2 {
  margin: 3px;
  line-height: 1.3em;
  font-size: 1.5em;
}

@import url("https://fonts.googleapis.com/css2?family=Open+Sans+Condensed:ital,wght@0,300;0,700;1,300&family=Open+Sans:ital,wght@0,300;0,400;0,600;0,700;0,800;1,300;1,400;1,600;1,700;1,800&display=swap");
</style>
