<template>
    <div>
      <br>
      <h2>저장된 채널</h2>
      <div v-if="videos" class="smallcontainer">
        <div v-for="video in videos" :key="video.id" class="videocontainer">
            <!-- <img :src="video.snippet.thumbnails.default.url" alt="썸네일"> -->
            <img :src="channelProfileImage" alt="채널 프로필 사진">
            <div class="strong">
              <strong>{{ video.snippet.channelTitle }}</strong>
            </div>
            <div class="button">
                <button  class="btn btn-primary" @click="removeCart(video)">삭제</button>
            </div>
        </div>
      </div>
      <div v-else>
        <strong>등록된 비디오 없음</strong>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  
  const router = useRouter()
  
  const videos = ref(null)
  
  videos.value = JSON.parse(localStorage.getItem('video'))
  
  const goDetail = (video) => {
    router.push(`/${video.id.videoId}`)
  }
  
  const removeCart = (video) => {
  // 1. 삭제할 아이템 index 검색
  const itemIdx = videos.value.findIndex((item) => item.id === video.id);

  // 2. 데이터 삭제

  videos.value.splice(itemIdx, 1);

    // 3. 삭제된 데이터를 기준으로 데이터를 반영
    localStorage.setItem('video', JSON.stringify(videos.value));

    console.error('해당 동영상을 찾을 수 없습니다.');

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
.strong{
    margin-left: 4px;
    top: 230px;
    position: absolute;
}
.button{
    margin-left: 4px;
    bottom: 2px;
    position: absolute;
}

  </style>