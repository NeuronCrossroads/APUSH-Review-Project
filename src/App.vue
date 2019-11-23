<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />

        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"
          width="100"
        />
      </div>

      <v-spacer></v-spacer>
    </v-app-bar>
    <v-content class="back">
      <v-container style="max-width: calc(100vw - 15px) !important; padding: 0px !important;">
        <v-row>
          <v-spacer></v-spacer>
          <EventList v-bind:events="information.events" />
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import EventList from "./components/EventList.vue";
import events_and_trends from "./assets/information.json";

export default {
  name: "App",

  components: {
    EventList
  },

  data() {
    return { information: events_and_trends };
  }
};
</script>

<style scoped>
.back {
  background-image: url("https://geology.com/world/usa-physical.jpg");
  background-attachment: fixed;
  background-size: cover;
}
</style>