<template>
  <div class="page" flex-column>
    <sliding-boxes
      v-for="index in 10"
      :key="index"
      :location="index"
      :forward="index % 2 == 0"
    />
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import SlidingBoxes from "../components/SlidingBoxes.vue";

@Component({
  components: {
    SlidingBoxes,
  },
})
export default class Home extends Vue {}
</script>

<style lang="scss" scoped>
.page {
  overflow-x: hidden;
  overflow-y: hidden;
}
</style>
