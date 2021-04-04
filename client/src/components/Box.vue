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
  background: rgb(51, 30, 50);
  border-radius: 0.3em;
  box-shadow: 0 0 10px rgba(73, 44, 71, 0.5);
  float: left;
  width: 50px;
  height: 100%;
  user-select: none;
  color: rgb(104, 104, 105);
  font-weight: bold;

  &:hover {
    transition: all 0.3s ease-out;
    color: white;
    background: rgb(90, 66, 89);
    cursor: pointer;
    box-shadow: 0 0 20px rgb(90, 66, 70);
  }
}

p {
  margin: 1em;
}
</style>