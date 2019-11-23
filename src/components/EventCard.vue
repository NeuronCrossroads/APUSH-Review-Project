<template>
  <div>
  <v-card max-width="500" class="frosted">
    <v-list-item three-line>
      <v-list-item-content>
        <div class="overline mb-4" style="margin-bottom: 10px !important;">
          <v-row no-gutters>
            <v-col sm="4" class="text-left">Date: {{ event.time }}</v-col>
            <v-col sm="4" class="text-center">AMSCO: {{ event.amsco }}</v-col>
            <v-col sm="4" class="text-right">{{ event.cfw }}</v-col>
          </v-row>
        </div>
        <v-list-item-title class="mb-1" style="font-size: 1.25rem !important;">{{ event.name }}</v-list-item-title>
        <v-card-subtitle style="padding: 0px !important; padding-bottom: 0px !important;">
          <v-chip outlined class="mr-3 mb-1" 
            v-for="theme in event.themes"
            v-bind:key="theme"
            :text-color="colors[theme]"
            :color="colors[theme]">
            {{ theme }}
          </v-chip>
        </v-card-subtitle>
        <v-divider></v-divider>
        <v-card-text style="padding: 0px !important;">
          <div class="text-justify" style="color: #333333 !important; margin-top: 6px !important; font-size: 0.9rem !important;" v-html="event.overview">
          </div>
          <div class="text--primary" style="color: #333333 !important;">
            <v-row>
              <v-col sm="6">Causes:
                <ul>
                <li
                  v-for="cause in event.causes"
                  v-bind:key="cause">
                  {{ cause }}
                </li>
                </ul>
              </v-col>
              <v-col sm="6">Effects:
                <ol>
                <li
                  v-for="effect in event.effects"
                  v-bind:key="effect">
                  {{ effect }}
                </li>
                </ol>

              </v-col>

            </v-row>
          </div>
        </v-card-text>
      </v-list-item-content>
    </v-list-item>
  </v-card>
  <v-divider class="ma-1"></v-divider>
  </div>
</template>

<script>
export default {
  props: ["event"],
  data() {
    return {
      colors: {
        "political":"red",
        "economic":"green",
        "social":"blue",
        "ideological":"orange",
        "cultural":"purple"
      }
    }
  }
};
</script>

<style scoped>
.frosted {
  background-color: rgba(255, 255, 255, 0.75) !important;
  -webkit-backdrop-filter: blur(10px) !important;
  backdrop-filter: blur(10px) !important;
  border-radius: 20px !important;
}
</style>