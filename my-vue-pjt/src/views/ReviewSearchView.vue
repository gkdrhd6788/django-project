<template>
    <div>
        ReviewSearch
        <searchForm 
        @input-keyword="searchVideo"/>
        <div class="video-list">
            <VideoCard v-for="video in videos" :key="video.etag"
            :video="video"
            />
        </div>
    </div>
</template>

<script setup>
  import {ref,onMounted} from 'vue'
  import searchForm from '@/components/SearchForm.vue'
  import VideoCard from '@/components/VideoCard.vue'
  
  import axios from 'axios'
  const key = import.meta.env.VITE_YOUTUBE_KEY
  const videos = ref([])

  const saveData =  function(data){
    const jsonData = JSON.stringify(data)
    localStorage.setItem('youtube-videos',jsonData)
  }
  const loadData = function(){
    const jsonData = localStorage.getItem('youtube-videos')
    return JSON.parse(jsonData) || [] 
  }
  onMounted(()=>{
    videos.value=loadData()

    console.log(videos.value)
  })
  const searchVideo = function(keyword){
      const url = 'https://www.googleapis.com/youtube/v3/search'
      const params = {
        key: key,
        part: 'snippet',
        q: keyword,
        type: 'video',
      }

      //youtube 요청
    axios({
        method:'get',
        url,
        params,
    })
        .then(res=>{
            console.log(res.data)
            videos.value = res.data.items
            saveData( videos.value)
        })
        .catch(err=> console.log(err))
  }
</script>

<style scoped>
.video-list{
    display:flex;
    flex-wrap: wrap;
}
</style>