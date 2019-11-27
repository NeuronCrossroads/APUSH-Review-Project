<template>
  <v-col sm="3" xl="2">
    <v-card
      id="trends"
      class="frosted mr-1 blue-back"
      style="height: calc(60px) !important; margin-bottom: 150px !important;"
    >
      <v-card-title>APUSH Review</v-card-title>
    </v-card>
    <v-card
      class="pa-4 frosted mr-1"
      style="height: calc(100vh - 240px) !important; overflow: scroll !important;"
    >
      <TrendCard v-for="trend in trends" v-bind:trend="trend" v-bind:key="trend.name" />
    </v-card>
  </v-col>
</template>

<script>
import TrendCard from "./TrendCard.vue";

export default {
  props: ["trends"],
  components: { TrendCard },
  methods: {}
};
</script>

<style scoped>
.frosted {
  background-color: rgba(255, 255, 255, 0.1);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  border-radius: 20px !important;
}

.blue-back {
  color: white;
  background-color: rgba(68, 0, 255, 0.75);
}
*::-webkit-scrollbar {
  display: none !important;
}
</style>