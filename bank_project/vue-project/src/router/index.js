import { createRouter, createWebHistory } from 'vue-router'
import ArticleView from '@/views/ArticleView.vue'
import DetailView from '@/views/DetailView.vue'
import CreateView from '@/views/CreateView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import Home from '@/views/Home.vue'
import CurrencyView from '@/views/CurrencyView.vue'
import Finlife from '@/views/Finlife.vue'
import Finlife2 from '@/views/Finlife2.vue'
import Recommendation from '@/views/Recommendation.vue'
import Recommendation2 from '@/views/Recommendation2.vue'
import Result from '@/views/Result.vue'
import Result2 from '@/views/Result2.vue'
import KakaoView from '@/views/KakaoView.vue'
import Profile from '@/views/Profile.vue'
import CartView from '@/views/CartView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/cart',
      name: 'cart',
      component: CartView
    },
    {
      path: '/article',
      name: 'ArticleView',
      component: ArticleView
    },
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/articles/:id',
      name: 'DetailView',
      component: DetailView
    },
    {
      path: '/create',
      name: 'CreateView',
      component: CreateView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
    {
      path: '/currency',
      name: 'CurrencyView',
      component: CurrencyView
    },
    {
      path: '/finlife',
      name: 'Finlife',
      component: Finlife
    },
    {
      path: '/finlife2',
      name: 'Finlife2',
      component: Finlife2
    },
    {
      path: '/recommendation',
      name: 'Recommendation',
      component: Recommendation
    },
    {
      path: '/recommendation2',
      name: 'Recommendation2',
      component: Recommendation2
    },
    {
      path: '/result',
      name: 'Result',
      component: Result
    },
    {
      path: '/result2',
      name: 'Result2',
      component: Result2
    },
    {
      path: '/maps',
      name: 'maps',
      component: KakaoView
    },
    {
      path: '/Profile',
      name: 'Profile',
      component: Profile
    },

  ]
    
})

import { useCounterStore } from '@/stores/counter'

router.beforeEach((to, from) => {
  const store = useCounterStore()
  if (to.name === 'ArticleView' && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogInView' }
  }
  if (to.name === 'Finlife' && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogInView' }
  }
  // if (to.name === 'ArticleView' && !store.isLogin) {
  //   window.alert('로그인이 필요합니다.')
  //   return { name: 'LogInView' }
  // }
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin)) {
    window.alert('이미 로그인 했습니다.')
    return { name: 'ArticleView' }
  }
})

export default router
