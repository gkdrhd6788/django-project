<template>
    <div v-for="movie in movies">
        <movieCard :movie="movie"/>
    </div>
</template>

<script setup>
  import { ref,onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  import axios from 'axios'
  import movieCard from '@/components/MovieCard.vue'

  const token = import.meta.env.VITE_TMDB_TOKEN
  const movies = ref([])

  const searchVideo = function(){
      const url = 'https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1'
      const options = {
        url,
        method: 'GET',
        headers: {
            accept: 'application/json',
            Authorization: `Bearer ${token}`
        }
        };

      //TMDB 요청
    axios(options)
        .then(res=>{
            movies.value = res.data.results
            console.log(movies)
        })
        .catch(err=> console.log(err))
  }

  onMounted(()=>{
    searchVideo()
  })
  const router = useRouter()
  const goDetail = function(movie){
    router.push(`/${movie.id}`)
  }
</script>

<style scoped>

</style>