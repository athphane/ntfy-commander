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
import axios from 'axios';


function get_total_users() {
  axios.get('http://localhost:35000/users/total').then(function(response) {
    console.log(response.data);
  })
}

get_total_users()

</script>
