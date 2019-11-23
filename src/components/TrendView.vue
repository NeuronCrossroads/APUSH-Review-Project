<template>
   <v-col sm="4">
       <v-card outlined class="pa-4">
       <EventCard
       v-for="event in events"
       v-bind:event="event"
       v-bind:key="event.name"
       />
       </v-card>
    </v-col>
</template>

<script>
import TrendCard from "./TrendCard.vue";

export default {
    props: ["events"],
    components: {EventCard},
    methods: {

    }
}
</script>