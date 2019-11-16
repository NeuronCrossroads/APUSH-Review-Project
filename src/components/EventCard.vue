<template>
  <v-card max-width="450">
    <v-list-item three-line>
      <v-list-item-content>
        <div class="overline mb-4" style="margin-bottom: 0px !important;">
          <v-row no-gutters>
            <v-col sm="4">Time</v-col>
            <v-col sm="4">AMSCO</v-col>
            <v-col sm="4">Curr Framework</v-col>
          </v-row>
        </div>
        <v-list-item-title class="headline mb-1">Event Name</v-list-item-title>
        <v-card-subtitle style="padding: 0px !important; padding-bottom: 5px !important;">
            <v-chip outlined class="mr-1" text-color="red" color="red">theme</v-chip>
            <v-chip outlined class="mr-1" text-color="green" color="green">theme</v-chip>
            <v-chip outlined class="mr-1" text-color="blue" color="blue">theme</v-chip>
        </v-card-subtitle>
        <v-divider></v-divider>
        <v-card-text style="padding: 0px !important;">
          <div class="text-primary" style="color: #333333 !important; margin-top: 4px !important;">
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nemo ipsam illo doloremque aliquid a pariatur aliquam quae nihil doloribus officia! Sit iusto impedit porro nisi necessitatibus expedita ipsa, reprehenderit aperiam.
          </div>
          <div class="text--primary" style="color: #333333 !important;">
            <v-row>
              <v-col sm="6">Causes: la la la la la, la la la la la, la la la la</v-col>
              <v-col sm="6">Effects: la la la la la, la la la la la, la la la la</v-col>
            </v-row>
          </div>
        </v-card-text>
      </v-list-item-content>
    </v-list-item>
  </v-card>
</template>

<script>
export default {};
</script>