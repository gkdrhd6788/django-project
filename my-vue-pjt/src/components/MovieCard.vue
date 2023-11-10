<template>
    <div @click="goDetail(movie)" class="card" style="width: 18rem;">
        <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" class="card-img-top" alt="...">
        <div class="card-body">
            <h1 class="card-text">{{ movie.title }}</h1>
            <p class="card-text">{{ movie.overview }}</p>
        </div>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
const props = defineProps({
    movie: Object
})
const goDetail = function (movie) {
    router.push(`/${movie.id}`)
}
</script>

<style scoped>

</style>