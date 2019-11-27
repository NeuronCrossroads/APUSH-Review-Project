<template>
  <div>
  <v-card max-width="500" class="frosted">
    <v-list-item three-line>
      <v-list-item-content>
        <div class="overline mb-4" style="margin-bottom: 10px !important;">
          <v-row no-gutters>
            <v-col sm="12" class="text-center">Time Period: {{ trend.time }}</v-col>
          </v-row>
        </div>
        <v-list-item-title class="mb-1" style="font-size: 1.25rem !important;">{{ trend.name }}</v-list-item-title>
        <v-divider></v-divider>
        <v-card-text style="padding: 0px !important;">
          <div class="text-justify" style="color: #333333 !important; margin-top: 6px !important; font-size: 0.9rem !important;" v-html="trend.overview">
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
  props: ["trend"],
  data() {
    return {

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