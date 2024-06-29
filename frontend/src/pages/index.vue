<template>
  <v-container fluid>
    <v-row>
      <v-col md="4" cols="12">
        <v-card title="Total Users" text="..."></v-card>
      </v-col>

      <v-col md="4" cols="12">
        <v-card title="Total Topics" text="..."></v-card>
      </v-col>
      
      <v-col md="4" cols="12">
        <v-card title="Total Tokens" text="..."></v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
export default {

}

function get_total_users() {
  fetch('')
}

</script>
