import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const router = useRouter()
  const articles = ref([])
  const accounts = ref([])
  const comments = ref([])
  const exchangeRate = ref([])
  const finlife = ref([])
  const finlife2 = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const surveyData=ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  // DRF에 article 조회 요청을 보내는 action
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) =>{
        // console.log(res)
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 회원가입 함수(인자를 받아서 axios로 요청 보내기)
  const signUp = function (payload) {
    const { username, password1, password2
    , nickname, email, age, money, salary, phoneNo, financial_products  
  } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2, 
        nickname, email, age, money, phoneNo, salary, financial_products
      }
    })
      .then((res) => {
        console.log(res)
        const password = password1
        logIn({ username, password })
      })
      .catch((err) => {
        console.log(err)
      })
  }
  // 인자를 받아서 서버로 로그인 요청, 응답 데이터에서 토큰을 받아서 저장
  const logIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        console.log(res.data)
        token.value = res.data.key
        router.push({ name: 'Home' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
      .then((res) => {
        token.value = null
        router.replace({ name: 'Home' })
        // router.push({ name: 'Home' })
        console.log('집으로 가는중')
      })
      .catch((err) => {
        console.log(err)
      })
  }
  
  const getExchangeRate = function () {
    axios({
      method: 'get',
      url: `${API_URL}/calc/`, 
    })
      .then((res) => {
        // console.log('여기와?')
        // console.log(res.data)
        exchangeRate.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getFinlife = function () {
    axios({
      method: 'get',
      url: `${API_URL}/finlife/`, 
    })
      .then((res) => {
        // console.log('여기와?')
        // console.log(res.data)
        finlife.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
  const getFinlife2 = function () {
    axios({
      method: 'get',
      url: `${API_URL}/finlife2/`, 
    })
      .then((res) => {
        // console.log('여기와?')
        // console.log(res.data)
        finlife2.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getComments = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/comments/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
        console.log(res.data)
        comments.value = res.data
      })
      .catch((err) => {
        console.log(err)
      });
  };


  const getUserInfo = function () {
    axios({
      method: 'get',
      url: `${API_URL}/accounts/user/`, 
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
        console.log('여기와?')
        console.log(res.data)
        accounts.value = res.data
        // console.log(res.data)
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const submitSurvey = function(data) {
    console.log('Data to send:', data); // 전송하는 데이터를 콘솔에 출력
    surveyData.value = data
    console.log('SurveyData:', surveyData.value); // 저장된 데이터를 콘솔에 출력
  }

  return { articles, API_URL, getArticles, signUp, logIn, token, isLogin, logOut, exchangeRate, getExchangeRate, finlife, getFinlife, finlife2, getFinlife2, surveyData, submitSurvey, comments, getComments, accounts, getUserInfo }
}, { persist: true })
