<template>
  <v-app id="inspire">
    <v-navigation-drawer v-model="drawer">
      <v-list-item title="My Application" subtitle="Vuetify"></v-list-item>
      <v-divider></v-divider>
      <v-list-item router to="/" title="Dashboard"></v-list-item>
      <v-list-item router to="/users" title="Users"></v-list-item>
    </v-navigation-drawer>

    <v-app-bar>
      <v-app-bar-nav-icon @click="something()"></v-app-bar-nav-icon>

      <v-app-bar-title>ntfy-commander</v-app-bar-title>
    </v-app-bar>

    <v-main>
      <router-view />

    </v-main>

  </v-app>
</template>

<script setup>
  import { ref } from 'vue'

  const drawer = ref(null)
</script>

<script>
  export default {
    data: () => ({ drawer: null }),
  }

  function something() {
    this.drawer = !this.drawer;
    console.log('sidebar opened')
  }
</script>
