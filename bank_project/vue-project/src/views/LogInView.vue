<template>
  <div class="bank-recommendation">
  <div class="login-container">
    <h1>로그인</h1>
    <form @submit.prevent="logIn" class="login-form">
      <div class="form-group">
        <label for="username">아이디</label>
        <input type="text" id="username" v-model.trim="username" placeholder="아이디를 입력하세요">
      </div>
      <div class="form-group">
        <label for="password">비밀번호</label>
        <input type="password" id="password" v-model.trim="password" placeholder="비밀번호를 입력하세요">
      </div>
      <button type="submit">로그인</button>
    </form>
  </div>
</div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const username = ref(null)
const password = ref(null)

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
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
</style>
