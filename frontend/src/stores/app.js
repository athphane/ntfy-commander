// Utilities
import { defineStore } from 'pinia'

export const useDashboardStats = defineStore('dashboard_stats', {
  state: () => ({
    usersCount: null,
    topicsCount: null,
    tokensCount: null,
  }),

  actions: {
    // Call all functions below to set all the values
    async fetchAllData() {
      await Promise.all([
        this.fetchTotalUsers(),
        this.fetchTotalTopics(),
        this.fetchTotalTokens()
      ]);
    },

    // Get total users count
    async fetchTotalUsers() {
      try {
        const response = await axios.get('http://localhost:35000/users/total');
        this.usersCount = response.data;
      } catch (error) {
        console.error(error);
      }
    },

    // Get total topics count
    async fetchTotalTopics() {
      try {
        const response = await axios.get('http://localhost:35000/topics/total');
        this.topicsCount = response.data;
      } catch (error) {
        console.error(error);
      }
    },

    // Get total tokens count
    async fetchTotalTokens() {
      try {
        const response = await axios.get('http://localhost:35000/tokens/total');
        this.tokensCount = response.data;
      } catch (error) {
        console.error(error);
      }
    },


  }
});