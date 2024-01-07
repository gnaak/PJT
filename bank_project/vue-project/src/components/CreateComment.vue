<template>
    <h5 class="title-message">이 글에 댓글을 남겨보세요</h5>
      <form @submit.prevent="createComment">
          <!-- <label for="content">댓글:</label> -->
        <div class="create-container">
          <textarea class="create-box" v-model.trim="content" id="content" style="height: 50px;"></textarea>
        <input class="input-button" type="submit" value="작성하기">
        </div>
      </form>

  </template>
  
  <script setup>
  import { ref } from 'vue'
  import axios from 'axios'
  import { useCounterStore } from '@/stores/counter'
  import { useRouter } from 'vue-router'
  
  const content = ref('')
  const store = useCounterStore()
  const router = useRouter()
  
  const props = defineProps({
  article: {
    type: Object,
  },
});

  const createComment = function () {
    axios({
      method: 'post',
      url: `${store.API_URL}/api/v1/articles/${props.article.id}/comments/`,
      data: {
        content: content.value
      },
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then((res) => {
        // 새로고침 없이 추가한 댓글이 바로 출력되려면
        store.comments.push(res.data)
        content.value = ''
        router.push({ name: 'DetailView'})
        
      })
      .catch((err) => {
        console.log(err)
      })
  }


  </script>
  
  <style scoped>
  .title-message {
    font-weight: 600;
    font-size: large;
  }
  .create-container {
    display: flex;
    align-items: center;
    
  }
  .create-box {
    width: 400px;
    margin-right: 10px;
  }

  .input-button{
    width: 80px;
    height: 30px;
    background-color: #db9834 ;
    color: white;
    border: none;
    /* padding: 10px 20px; */
    text-align: center;
    text-decoration: none;
    /* display: inline-block; */
    font-size: 16px;
    cursor: pointer;
    border-radius: 4px;
    
  }
  </style>
  