<template>
  <div class="slider" fill-width pd3>
    <div
      class="graphic-container"
      fill-height
      flex-row
      :id="`scroller-${location}`"
      :style="{ animation: animation }"
    >
      <box
        v-for="(box, index) in boxes"
        :title="box.text"
        :key="index"
        :location="index"
      />
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Prop } from "vue-property-decorator";
import Box from "./Box.vue";

@Component({
  components: {
    Box,
  },
})
export default class SlidingBoxes extends Vue {
  @Prop() readonly location!: number;
  @Prop() readonly forward!: boolean;

  private animation: string =
    (this.forward ? "bannermove-right" : "bannermove-left") +
    " 3s linear infinite";

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

  moveItems() {}

  created() {
    const length = 3000;

    if (this.forward) {
      setInterval(() => {
        const scroller = document.getElementById(`scroller-${this.location}`);
        let last = scroller.lastChild;
        scroller.prepend(last);
      }, length);
    } else {
      console.log(123);
      setInterval(() => {
        const scroller = document.getElementById(`scroller-${this.location}`);
        let first = scroller.firstChild;
        scroller.append(first);
      }, length);
    }
  }
}
</script>

<style lang="scss">
.slider {
  width: 100%;
  overflow: hidden;
  // max-height: 50px;

  & .graphic-container {
    width: 2130px;
  }
}

@keyframes bannermove-left {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(-10%);
  }
}

@keyframes bannermove-right {
  0% {
    transform: translateX(-10%);
  }
  100% {
    transform: translateX(0);
  }
}
</style>