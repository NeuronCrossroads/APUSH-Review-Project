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

export default {
    props: ["events"],
    components: {EventCard},
    methods: {

    }
}
</script>