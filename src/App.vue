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
    <v-content>
      <v-container>
        <EventList v-bind:events="information.events"/>
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
    return {information: events_and_trends}
  }
};
</script>
