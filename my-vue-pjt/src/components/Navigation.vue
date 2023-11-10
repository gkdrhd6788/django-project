<template>
    <div>
        <ul class="nav bg-dark justify-content-center">
            <li class="nav-item">
                <RouterLink :to="{name:'home'}" class="nav-link text-white">Home</RouterLink>
            </li>
            <li class="nav-item">
                <RouterLink :to="{name:'movieList'}" class="nav-link">영화조회</RouterLink>
            </li>
            <li class="nav-item">
                <RouterLink :to="{name:'reviewSearch'}" class="nav-link">리뷰검색</RouterLink>
            </li>
            <li class="nav-item">
                <RouterLink :to="{name:'recommended'}" class="nav-link">영화추천</RouterLink>
            </li>
        </ul>
    </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
</script>

<style scoped>

</style>