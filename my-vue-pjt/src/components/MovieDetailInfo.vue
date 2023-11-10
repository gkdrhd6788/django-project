<template>
    <div>
    <img :src="`https://image.tmdb.org/t/p/w500${movieDetail.poster_path}`" class="card-img-top" alt="...">
    <h1>{{ movieDetail.title }}</h1>
    <p>개봉일:{{ movieDetail.release_date }}</p>
    <p>러닝타임:{{ movieDetail.runtime }}</p>
    <p>TMDB 평점:{{ movieDetail.vote_average }}</p>
    <h3>장르</h3>
    <div v-for="genre in movieDetail.genres">
        {{ genre.name }}
    </div>
    <h3>줄거리</h3>
    <p>{{ movieDetail.overview }}</p>
    <h3>공식 예고편</h3>

        <!-- Button trigger modal -->
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#YoutubeTrailerModal">
        유튜브 트레일러
    </button>
    <YoutubeTrailerModal :movie-id="movieDetail.id"/>


    </div>
</template>

<script setup>
import YoutubeTrailerModal from './YoutubeTrailerModal.vue';
const props = defineProps({
    movieDetail: Object
})


</script>

<style scoped>

</style>