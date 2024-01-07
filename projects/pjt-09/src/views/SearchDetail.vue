<template>
  <div class="container">
    <div v-if="video">
      <h2>{{ video.snippet.title }}</h2>
      업로드 날짜 : {{ video.snippet.publishedAt.slice(0,10) }}
      <iframe
      width="560"
      height="315"
      :src="getVideoEmbedUrl(video.id)"
      frameborder="0"
      allowfullscreen
      >
      </iframe>
      <p v-html="video.snippet.description"></p>

      <button class="btn btn-primary" @click="saveVideo(video)">동영상 저장</button>
      <button class="btn btn-warning" @click="saveChannel(video)">채널 저장</button>

    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRoute } from 'vue-router';

const route = useRoute();
const videoId = route.params.videoId;
const video = ref(null);

const fetchVideoDetails = async () => {
  try {
    const response = await axios.get('https://www.googleapis.com/youtube/v3/videos', {
      params: {
        id: videoId,
        key: '',
        part: 'snippet',
      },
    });
    // Assuming there is only one video with the given ID
    video.value = response.data.items[0];
  } catch (error) {
    console.error(error);
  }
};

const getVideoEmbedUrl = (videoId) => {
  return `https://www.youtube.com/embed/${videoId}`;
};

onMounted(() => {
  fetchVideoDetails();
});

const saveVideo = (video) => {
  const existingVideo = JSON.parse(localStorage.getItem('video')) || []
  const isDuplicate = existingVideo.length > 0 && existingVideo.find((item) => item.id === videoId)
  if (!isDuplicate) {
        alert('동영상을 저장합니다')
        existingVideo.push(video)
    } else {
        alert('동영상 저장을 취소합니다')
        const updatedVideoList = existingVideo.filter((item) => item.id !== videoId);
        existingVideo.length = 0; // 기존 배열을 비워줌
        existingVideo.push(...updatedVideoList); // 새로운 배열을 기존 배열에 추가
    }

    // 수정된 카트 데이터를 localStorage에 저장
    localStorage.setItem('video', JSON.stringify(existingVideo))

}
const saveChannel = (video) => {
  const existingVideo = JSON.parse(localStorage.getItem('channel')) || []
  const isDuplicate = existingVideo.length > 0 && existingVideo.find((item) => item.id === videoId)
  if (!isDuplicate) {
        alert('채널을 저장합니다')
        existingVideo.push(video)
    } else {
        alert('채널 저장을 취소합니다')
        const updatedVideoList = existingVideo.filter((item) => item.id !== videoId);
        existingVideo.length = 0; // 기존 배열을 비워줌
        existingVideo.push(...updatedVideoList); // 새로운 배열을 기존 배열에 추가
    }

    // 수정된 카트 데이터를 localStorage에 저장
    localStorage.setItem('channel', JSON.stringify(existingVideo))

}


</script>

<style scoped>
.container {
  width: 80%;
  margin: 20px auto;
}

img {
  width: 100%;
  height: auto;
}
button{
  margin: 5px;
}
</style>
