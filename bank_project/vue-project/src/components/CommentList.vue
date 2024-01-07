<template>
  <div>
    <div>
        <h5 class="comment-title">이 글에 작성된 댓글</h5>
    </div>
    <div></div>
    <ul v-if="comments">
      <li v-for="comment in comments" :key="comment.id" >
        <div v-if="article.id === comment.article">
          <div class="name"> 
            익명이 {{ comment.user }} 
          </div>
          <!-- {{ comment.id }} -->
          <!-- {{ comment.content }} -->
          <div class="button-box">
            <div class="content-box">
            {{ comment.content }}
          </div>
          <button class="button-style1" @click="deleteComment(comment)" v-if="comment.user === store.accounts.pk">삭제</button>
          <button class="button-style2" @click.prevent="showform(comment)" v-if="comment.user === store.accounts.pk">수정</button>
          </div>
          <div>
            <div v-if="comment.editing">
              <textarea class="comment-edit" v-model="comment.editedContent"> 
              </textarea>
              <button class="save-button" @click="updateComment(comment)">저장</button>
            </div>
            </div>
        </div>
      </li>
    </ul>
    <div v-else>아직 작성된 댓글이 없습니다. 댓글을 작성해보세요!</div>
    <hr>
  </div>
</template>

<script setup>

import { onMounted, watch, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import { storeToRefs } from 'pinia';
import axios from 'axios';

import { useRouter } from 'vue-router'
const router = useRouter()

  
const props = defineProps({
  article: {
    type: Object,
  },
});

const store = useCounterStore()

const { comments } = storeToRefs(store)

onMounted(() => {
  store.getComments() // 비동기 처리라서 뒤가 먼저 실행
  // console.log(store.comments) // undefined
})

// watch(comments, (newValue) => {
//   console.log('comments watch')
//   console.log(newValue)
// })
// path('comments/<int:comment_pk>/', views.comment_detail),

const deleteComment = (comment) => {
    axios({
      method: 'delete',
      url: `${store.API_URL}/api/v1/comments/${comment.id}/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then(() => {
        console.log('Article deleted successfully');
        router.push({ name: 'DetailView' })
        store.getComments()
      })
      .catch((err) => {
        console.error('Error deleting article:', err);
      });
  }

  // 수정하기 위해 필요한 함수 
  // 1.수정할 댓글 내용과 폼을 불러오는 함수
  // 2. 수정 후 저장하기
  // 수정버튼 - 누르면 수정 폼(기존의 댓글부분? 새로운 입력창에 v-model?) - 수정 - 제출 - 수정완료?
const updateComment = (comment) => {
  console.log('여기는 오나?')
  axios({
    method: 'put',
    url: `${store.API_URL}/api/v1/comments/${comment.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
    data: {
      content: comment.editedContent,
      id: comment.id
    }
  })
  .then(() => {
    console.log('Comment updated successfully')
    router.push({ name: 'DetailView' })
    store.getComments()
  })
  .catch((err) => {
    console.error('Error updating comment:', err)
    console.log(err.response.data);
    // console.log(err.response.status);
    // console.log(err.response.headers);
  });
  }

const showform = (comment) => {
  comment.editing = !comment.editing // 댓글 객체에 editing 속성을 추가하고 토글
  comment.editedContent = comment.content

};
</script>
<style scoped>
.comment-title {
  font-size: large;
  font-weight: 600;
}

.content-box {
  max-width: 360px;
}
.button-box {
  display: flex;
  /* justify-content: right; */
}
.button-style1 {
  width: 50px;
  height: 30px;
  background-color: #3498db;
  color: white;
  border: none;
  /* padding: 10px 5px; */
  text-align: center;
  text-decoration: none;
  /* display: inline-block; */
  font-size: 16px;
  cursor: pointer;
  border-radius: 4px;
  /* width: 500px; */
  margin-right: 5px;
  margin-left: 10px;
}

.button-style2{
  width: 50px;
  height: 30px;
  background-color: #2ecc71;
  color: white;
  border: none;
  /* padding: 10px 20px; */
  text-align: center;
  text-decoration: none;
  /* display: inline-block; */
  font-size: 16px;
  cursor: pointer;
  border-radius: 4px;
  /* width: 500px; */
}

.comment-edit {
  width: 400px;
  margin-right: 10px;
  margin-top: 10px;
}

.name{
  color: darkcyan;
  font-weight: 700;
}

.save-button {
    width: 50px;
    height: 30px;
    background-color: #db9834 ;
    color: white;
    border: none;
    text-align: center;
    text-decoration: none;
    font-size: 16px;
    cursor: pointer;
    border-radius: 4px;
}
</style>