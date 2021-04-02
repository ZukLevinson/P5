<template>
  <div class="slider" fill-width>
    <div class="graphic-container">
      <box v-for="(box, index) in boxes" :title="box.text" :key="index" />
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import Box from "./Box.vue";

@Component({
  components: {
    Box,
  },
})
export default class SlidingBoxes extends Vue {
  private boxes: object[] = [
    { text: "Test 1" },
    { text: "Test 2" },
    { text: "Test 3" },
    { text: "Test 4" },
    { text: "Test 5" },
    { text: "Test 6" },
    { text: "Test 7" },
    { text: "Test 8" },
    { text: "Test 9" },
    { text: "Test 10" },
  ];
}
</script>

<style lang="scss">
.slider {
  width: 100%;
  overflow: hidden;

  & .graphic-container {
    width: 2130px;
  }
}
.box:first-child {
  animation: bannermove 10s linear infinite;
}

@keyframes bannermove {
  0% {
    margin-left: 0px;
  }
  100% {
    margin-left: -2130px;
  }
}
</style>