<template>
   <v-col sm="4">
       <EventCard
       v-for="event in events"
       v-bind:event="event"
       v-bind:key="event.name"
       />
    </v-col>
</template>

<script>
import EventCard from "./EventCard.vue";
import information from "../assets/information.json"

export default {
    components: {EventCard},
    data() {
        return {
            events: information.events
        }
    },
    methods: {

    }
}
</script>