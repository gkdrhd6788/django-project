<template>
    <div class="card-wrapper">
        <div class="card" >
        <img :src="thumbnailUrl" class="card-img-top" alt="..."
        @click="moveDatail">
        <div class="card-body">
            <h6 class="card-title">{{ VideoTitle }}</h6>
        </div>
    </div>
    </div>
</template>

<script setup>
import {computed} from 'vue'
import { useRouter } from 'vue-router';
const props = defineProps({
    video:Object,
})
const thumbnailUrl = computed(()=>props.video.snippet.thumbnails.medium.url)
const VideoTitle = computed(()=>props.video.snippet.title)
const VideoId = computed(()=>props.video.id.videoId)  //자동으로 ref됨

const router = useRouter()
const moveDatail = function(){
    console.log(VideoId.value)
    router.push({
        name:'detail',
        params: {id: VideoId.value}
    })
}
</script>

<style scoped>
.card-wrapper{
    width:300px;
    height: 300px;
    margin:1rem;
}
</style>