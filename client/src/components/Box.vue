<template>
  <div class="box" text-center>
    <p>{{ title }}</p>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";

@Component
export default class Box extends Vue {
  @Prop() readonly title!: string;
}
</script>

<style lang="scss">
.box {
  margin: 2em;
  background: rgb(73, 44, 71);
  border-radius: 0.3em;
  box-shadow: 25px #000;
  float: left;
  width: 5%;
  height: 6vh;
}

p {
  margin: 1em;
}
</style>