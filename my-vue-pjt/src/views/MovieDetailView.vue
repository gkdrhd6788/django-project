<template>
    <div>
        <MovieDetailInfo :movie-detail="movie"/>
    </div>
</template>

<script setup>
     import { ref,onMounted } from 'vue';
  import { useRouter, useRoute } from 'vue-router';
  import axios from 'axios'
  import MovieDetailInfo from '../components/MovieDetailInfo.vue';
  const route = useRoute()
  const token = import.meta.env.VITE_TMDB_TOKEN
  const movie = ref([])

  const movieDetail = function(){
      const movieId = route.params.movieId
      const url = `https://api.themoviedb.org/3/movie/${movieId}?language=en-US`
      
      const options = {
            url,
            method: 'GET',
            headers: {
                accept: 'application/json',
                Authorization: `Bearer ${token}`}
        };

      //TMDB 요청
    axios(options)
        .then(res=>{
            console.log(res.data)
            movie.value = res.data
            console.log(movie)
        })
        .catch(err=> console.log(err))
  }

  onMounted(()=>{
    movieDetail()
  })

</script>

<style scoped>

</style>