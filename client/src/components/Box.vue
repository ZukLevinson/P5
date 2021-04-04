<template>
  <div class="box" text-center :id="location">
    <p>{{ title }}</p>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";

@Component
export default class Box extends Vue {
  @Prop() readonly title!: string;
  @Prop() readonly location!: number;
}
</script>

<style lang="scss">
.box {
  margin: 0em 1em;
  background: rgb(73, 44, 71);
  border-radius: 0.3em;
  box-shadow: 25px #000;
  float: left;
  width: 50px;
  height: 100%;
  user-select: none;
}

p {
  margin: 1em;
}
</style>