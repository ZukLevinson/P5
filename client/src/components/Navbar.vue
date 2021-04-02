<template>
  <div fill-width flex-row class="navbar main">
    <div class="logos" lg2 pd2>
      <img src="logos/logo.svg" mr3 />
      <h2>MusicApp</h2>
    </div>
    <div class="center-piece" lg8 flex-row>Extra Data</div>
    <div class="links" lg2>
      <div class="link-box" v-for="(link, index) in links" :key="index">
        <router-link :to="link.url">{{ link.name }}</router-link>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component
export default class Navbar extends Vue {
  private links: Array<object> = [
    { url: "/", name: "Taste" },
    { url: "/recommendations", name: "Recommendations" },
  ];
}
</script>

<style lang="scss" scoped>
.center-piece {
  justify-content: center;
  align-items: center;
}

.logos {
  display: flex;
}

.links {
  display: inline-grid;
  grid-column-gap: 30px;
  grid-template-columns: auto auto;
}

.link-box {
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: "Open Sans Condensed", sans-serif;
  font-size: 1em;
  text-transform: uppercase;

  &:hover {
    color: gray;
    transition: 0.15s ease-in-out;
  }
}

.navbar {
  color: white;

  &.main {
    height: 6vh !important;
    min-height: 50px;
    flex: 0 1 auto !important;
  }
}

.router-link-exact-active {
  font-weight: bold;
}
</style>
