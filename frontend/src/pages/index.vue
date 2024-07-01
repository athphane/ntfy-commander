<template>
  <v-container fluid>
    <v-row>
      <v-col md="4" cols="12">
        <v-card title="Total Users" :text="dashboardStats.usersCount"></v-card>
        <v-progress-linear v-if="dashboardStats.usersCount == null" indeterminate></v-progress-linear>
      </v-col>

      <v-col md="4" cols="12">
        <v-card title="Total Topics" :text="dashboardStats.topicsCount"></v-card>
        <v-progress-linear v-if="dashboardStats.topicsCount == null" indeterminate></v-progress-linear>
      </v-col>
      
      <v-col md="4" cols="12">
        <v-card title="Total Tokens" :text="dashboardStats.tokensCount">
          <v-progress-linear v-if="dashboardStats.tokensCount == null" indeterminate></v-progress-linear>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>

import { useDashboardStats } from '@/stores/app';

const dashboardStats = useDashboardStats();

onMounted(() => {
  dashboardStats.fetchAllData();
});
</script>
