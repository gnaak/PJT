<template>
    <div class="container">
        <br>
        <h2>비디오 검색</h2>
        <form @submit.prevent="searchVideos">
            <input v-model="searchQuery" type="text" placeholder="검색어를 입력하세요">
            <button type="submit">찾기</button>
        </form>
        <br>
        <h4>검색 결과</h4>
        <div v-if="videos.length" class="smallcontainer">
            <div v-for="video in videos" :key="video.id" class="videocontainer" @click="goDetail(video)">
                <img :src="video.snippet.thumbnails.default.url" alt="썸네일">
                <p v-html="video.snippet.title"></p>
            </div>
        </div>
    </div>
</template>

<script setup>
import {ref, computed} from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router';

const searchQuery = ref('');
const videos = ref([])
const youtubeAPIKey = ''
const youtubeURL = 'https://www.googleapis.com/youtube/v3/search'

const searchVideos = async () => {
  try {
    const response = await axios.get(youtubeURL, {
      params: {
        q: searchQuery.value,
        key: youtubeAPIKey,
        part: 'snippet',
        type: 'video'
      },
    });
    videos.value = response.data.items;
  } catch (error) {
    console.error(error);
  }
};

const router = useRouter()

const goDetail = (video) => {
  router.push(`${video.id.videoId}`)
}

</script>

<style scoped>

.smallcontainer{
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    
}
.videocontainer{
    border: 1px solid black;
    width: 30%;
    height: 350px;
    position: relative;
    
}
img{
    width: 100%;
    height: 220px;
    object-fit: fill;
}

input{
    width: 90%;
}

</style>