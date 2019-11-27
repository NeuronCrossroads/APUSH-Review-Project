<template>
  <v-col sm="3" xl="2">
    <v-card
      id="events"
      class="pa-4 frosted mr-1"
      style="height: calc(100vh - 30px) !important; overflow: scroll !important;"
    >
      <EventCard v-for="event in events" v-bind:event="event" v-bind:key="event.name" />
    </v-card>
  </v-col>
</template>

<script>
import EventCard from "./EventCard.vue";

export default {
  props: ["events"],
  components: { EventCard },
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

*::-webkit-scrollbar {
  display: none !important;
}
</style>