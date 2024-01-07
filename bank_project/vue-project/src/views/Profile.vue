<template>
  <div class="bank-recommendation">
  <div class="login-container">
    
    <h1>{{ account.username }}님, 환영합니다!</h1>
    <form class="login-form" @click="navigateToCart">
      <div class="form-group">
      </div>
      <div class="form-group">
        <strong>아이디:</strong> {{ account.username }}
      </div>
      <div class="form-group">
        <strong>이메일:</strong> {{ account.email }}
      </div>
      <div class="form-group">
        <strong>나이:</strong> {{ account.age }}
      </div>
      <div class="form-group">
        <strong>연봉:</strong> {{ account.money }}
      </div>
      <div class="form-group">
        <strong>자산:</strong> {{ account.salary }}
      </div>
      <div class="form-group">
        <strong>핸드폰 번호:</strong>
            0{{ phoneN[0] }}{{ phoneN[1] }}-
            {{ phoneN[2] }}{{ phoneN[3] }}{{ phoneN[4] }}{{ phoneN[5] }}-
            {{ phoneN[6] }}{{ phoneN[7] }}{{ phoneN[8] }}{{ phoneN[9] }}
      </div>
      <button type="submit">상품 보러가기</button>
    </form>
  </div>
</div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const article = ref(null)

const account = store.accounts
const phoneN = `${account.phoneNo}`
onMounted(() => {
  store.getUserInfo();
})

const navigateToCart = () => {
      router.push({ name: 'cart' });
    };
</script>

<style scoped>

strong {
  color: #1a0dab; /* Google blue color */
}

.login-container {
  max-width: 400px;
  margin: auto;
  margin-top: 100px;
  text-align: center;
}
.bank-recommendation {
  background-color: #f4f4f4;
  padding: 20px;
  height: 850px;
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
