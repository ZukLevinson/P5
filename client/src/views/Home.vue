<template>
  <div class="page">
    <sliding-boxes />
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
