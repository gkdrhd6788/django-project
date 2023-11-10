<template>
    <Navigation />
  <div class="container">
      <RouterView />
  </div>
</template>

<script setup>
    import { RouterLink, RouterView } from 'vue-router'
    import Navigation from '@/components/Navigation.vue'
</script>


<style scoped>

</style>
