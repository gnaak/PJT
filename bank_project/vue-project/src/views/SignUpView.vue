<template>
  <div class="bank-recommendation">
  <div class="login-container">
    <h1>환영합니다!</h1>
    <p>금융 상품 추천 사이트에 가입하세요.</p>
    <form @submit.prevent="signUp" class="signup-form">
      <div class="form-group">
        <label for="username">아이디</label>
        <input type="text" id="username" v-model.trim="username" placeholder="아이디를 입력하세요">
      </div>
      <div class="form-group">
        <label for="password1">비밀번호</label>
        <input type="password" id="password1" v-model.trim="password1" placeholder="비밀번호를 입력하세요">
      </div>
      <div class="form-group">
        <label for="password2">비밀번호 확인</label>
        <input type="password" id="password2" v-model.trim="password2" placeholder="비밀번호를 다시 입력하세요">
      </div>
      <div class="form-group">
        <label for="nickname">닉네임</label>
        <input type="text" id="nickname" v-model.trim="nickname" placeholder="닉네임을 입력하세요">
      </div>
      <div class="form-group">
        <label for="birthdate">생년월일</label>
        <div class="date-inputs">
          <select id="year" v-model.trim="selectedYear">
            <option value="" disabled selected>년도</option>
            <option v-for="year in years" :key="year" :value="year">{{ year }}년</option>
          </select>
          <select id="month" v-model.trim="selectedMonth">
            <option value="" disabled selected>월</option>
            <option v-for="month in months" :key="month" :value="month">{{ month }}월</option>
          </select>
          <select id="day" v-model.trim="selectedDay">
            <option value="" disabled selected>일</option>
            <option v-for="day in days" :key="day" :value="day">{{ day }}일</option>
          </select>
        </div> 
      </div>
      <div class="form-group">
        <label for="phoneNo">휴대폰 번호</label>
        <input type="text" id="phoneNo" v-model.trim="phoneNo" placeholder="하이픈(-) 없이 휴대폰 번호만 입력하세요">
      </div>
      <div class="form-group">
        <label for="email">이메일 주소</label>
        <input type="text" id="email" v-model.trim="email" placeholder="example@ssafy.com">
      </div>
      <div class="form-group">
        <label>연봉</label>
        <div class="radio-group">
          <label>
            <input type="radio" v-model.trim="money" value="1"> 1억 미만
          </label>
          <label>
            <input type="radio" v-model.trim="money" value="2"> 1억 - 5억
          </label>
          <label>
            <input type="radio" v-model.trim="money" value="3"> 5억 - 10억
          </label>
        </div>
      </div>
      <div class="form-group">
        <label>총 자산</label>
        <div class="radio-group">
          <label>
            <input type="radio" v-model.trim="salary" value="1"> 10억 미만
          </label>
          <label>
            <input type="radio" v-model.trim="salary" value="2"> 10억 - 50억
          </label>
          <label>
            <input type="radio" v-model.trim="salary" value="3"> 50억 이상
          </label>
        </div>
      </div>
      <button type="submit">가입하기</button>
    </form>
  </div>
</div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore();
const username = ref(null);
const password1 = ref(null);
const password2 = ref(null);
const nickname = ref(null);
let age = ref(null);
const selectedYear = ref(null);
const selectedMonth = ref(null);
const selectedDay = ref(null);
const phoneNo = ref(null);
const money = ref(null);
const salary = ref(null);
const email = ref(null);
const money_choices = ref([
  10000000, 50000000, 100000000
])
const salary_choices = ref([
  100000000, 500000000, 1000000000
])
const signUp = function () {
  age.value = Number(2023 - selectedYear.value)
  // console.log('어느게', money)
  console.log('진짜 값인가?',money.value)
  console.log('얘는 안나와?',money_choices.value)
  money.value = Number(money_choices.value[money.value-1])
  salary.value = Number(salary_choices.value[salary.value-1])
  console.log('지랄말고 나와라?',money.value)
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    nickname: nickname.value,
    age: age.value,
    phoneNo: phoneNo.value,
    money: money.value,
    salary: salary.value,
    email: email.value,
  };
  console.log('Payload:', payload);
  // console.log('age:', age);
  // console.log("나이계산2", age)
  store.signUp(payload);
};

const years = Array.from({ length: 2023 - 1930 + 1 }, (_, i) => 2023 - i);
const months = Array.from({ length: 12 }, (_, i) => i + 1);
const days = Array.from({ length: 31 }, (_, i) => i + 1);
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

.form-group {
  text-align: left;
}

label {
  display: block;
  margin-bottom: 4px;
  font-size: 14px; /* Adjusted font size */
}

.input-group {
  display: flex;
  gap: 8px;
}

.date-inputs {
  display: flex;
  gap: 8px;
}

.radio-group {
  display: flex;
  gap: 16px;
}

input {
  width: 100%;
  padding: 8px;
  font-size: 14px;
}

button {
  background-color: #4caf50;
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
