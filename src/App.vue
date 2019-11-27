<template>
  <v-app>
    <v-content class="back">
      <v-container
        style="max-width: calc(100vw - 30px) !important; padding: 0px !important; padding-left: 15px;"
      >
        <v-row>
          <TrendList v-bind:trends="information.trends" />
          <v-spacer></v-spacer>
          <EventList v-bind:events="information.events" />
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import EventList from "./components/EventList.vue";
import TrendList from "./components/TrendList.vue";
import events_and_trends from "./assets/information.json";
import "./Map.js";

export default {
  name: "App",

  components: {
    EventList,
    TrendList
  },

  data() {
    return { information: events_and_trends };
  }
};

</script>

<style scoped>
.back {
  z-index: 1;
}

*::-webkit-scrollbar {
  display: none !important;
}

canvas {
  position: absolute;
  top: 0;
  left: 0;
  margin: 0;
  padding: 0;
}
</style>