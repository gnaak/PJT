<template>
    <div class="bank-recommendation">
      <div class="login-container">
        <h4>여러분의 이야기를 공유해보세요!</h4>
        <form @submit.prevent="createArticle" class="login-form">
          <div class="form-group">
            <label class="title" for="title">제목: </label>
            <input type="text" v-model.trim="title" id="title" class="form-input">
          </div>
          <div class="form-group">
            <label for="content">내용:</label>
            <textarea v-model.trim="content" id="content" class="form-textarea"></textarea>
          </div>
          <button type="submit" class="submit-button">작성하기</button>
        </form>
      </div>
    </div>
      
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'
import { useRouter, RouterLink } from 'vue-router'

const title = ref(null)
const content = ref(null)
const store = useCounterStore()
const router = useRouter()

const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      router.push({ name: 'ArticleView' })
    })
    .catch((err) => {
      console.log(err)
    })
}
</script>

<style scoped>

.bank-recommendation {
  background-color: #f4f4f4;
  padding: 20px;
  height: 850px;
}
.login-container {
  max-width: 400px;
  margin: auto;
  margin-top: 100px;
  text-align: center;
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-top: 16px;
}

.form-group {
  text-align: left;
}

label {
  display: block;
  margin-bottom: 4px;
}

input {
  width: 100%;
  padding: 8px;
  font-size: 14px;
}

button {
  background-color: #3498db;
  color: white;
  border: none;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  cursor: pointer;
  border-radius: 4px;
}

.potato {
  text-align: left;
  align-items: left;
  margin-left: 10px;
  width: 60%;
  margin-top: 0;
}

.articlebox {
  display: flex;
  flex-direction: column;
  justify-content: center;
  background-color: white  ;
  align-items: center;
  height: 100vh;
}

.contentbox {
  width: 500px;
  height: auto;
  padding: 20px;
  border-radius: 8px;
  margin-bottom: 20px;
}

.create-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 15px;
}

.title,
label {
  font-size: 18px;
}

.form-input,
.form-textarea {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.submit-button {
  background-color: #3498db;
  color: white;
  border: none;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  cursor: pointer;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.submit-button:hover {
  background-color: #2c3e50;
}
</style>
