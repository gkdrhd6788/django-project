<template>
    
    <!-- Modal -->
    <div class="modal fade" id="YoutubeTrailerModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-lg">
            <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="exampleModalLabel">Modal title</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                {{ movieId }}
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary">Save changes</button>
            </div>
        </div>
    </div>
</div>
</template>

<script setup>
import { ref,onMounted } from 'vue'
import axios from 'axios';
const props = defineProps({
  movieId: Number  //?
})
console.log(props, 'asdf')

// import {ref,onMounted} from 'vue'
// import axios from 'axios'

// const key = import.meta.env.VITE_YOUTUBE_KEY
// const videos = ref([])

//   const saveData =  function(data){
//     const jsonData = JSON.stringify(data)
//     localStorage.setItem('youtube-videos',jsonData)
//   }
//   const loadData = function(){
//     const jsonData = localStorage.getItem('youtube-videos')
//     return JSON.parse(jsonData) || [] 
//   }
//   onMounted(()=>{
//     videos.value=loadData()

//     console.log(videos.value)
//   })
//   const searchVideo = function(keyword){
//       const url = 'https://www.googleapis.com/youtube/v3/search'
//       const params = {
//         key: key,
//         part: 'snippet',
//         q: keyword,
//         type: 'video',
//       }

//       //youtube 요청
//     axios({
//         method:'get',
//         url,
//         params,
//     })
//         .then(res=>{
//             console.log(res.data)
//             videos.value = res.data.items
//             saveData( videos.value)
//         })
//         .catch(err=> console.log(err))
//   }
//tmdb
  const token = import.meta.env.VITE_TMDB_TOKEN
  const movie = ref([])

  const searchMovie = function(){
    console.log(props.movieId)
      const url = `https://api.themoviedb.org/3/movie/${props.movieId}/videos?language=en-US`
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
            movie.value = res.data
            console.log(movie)
        })
        .catch(err=> console.log(err))
  }

  onMounted(()=>{
    searchMovie()
  })
</script>

<style lang="scss" scoped>

</style>