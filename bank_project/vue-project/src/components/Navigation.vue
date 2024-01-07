<template>
    <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <!-- Google Font 적용 -->
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@500&display=swap" rel="stylesheet">
            <title>내 포트폴리오 사이트~..</title>
            <!-- 1. Bootstrap 적용 -->
            <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
            <link rel="icon" href="/favicon.ico" type="image/x-icon">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
        </head>
        <nav class="navbar navbar-expand-lg navbar-light" style="background-color: #e3f2fd;" >
            <div class="container-fluid">
                <img src="@/images/logo.png" height="50px" width="120px" alt="숲" >
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
                    <ul class="navbar-nav">
                        <div class="nav-item text-end">
                            <a class="nav-link text-black" href="" @click="navigateToHome">Home</a>
                        </div>
                        <div class="nav-item text-end">
                            <a class="nav-link text-black" href="" @click="navigateToFinlife">예/적금</a>
                        </div>
                        <div class="nav-item text-end">
                            <a class="nav-link text-black" href="" @click="navigateToCurrency">환율</a>
                        </div>
                        <div class="nav-item text-end">
                            <a class="nav-link text-black" href="" @click="navigateToMaps">지도</a>
                        </div>
                        <div class="nav-item text-end">
                            <a class="nav-link text-black" href="" @click="navigateToArticle">게시판</a>
                        </div>
                        <div class="nav-item text-end" v-if="!store.isLogin">
                            <a class="nav-link text-black" href="" @click="navigateToSignUp">회원가입</a>
                        </div>
                        <div class="nav-item text-end" v-if="!store.isLogin">
                            <a class="nav-link text-black" href="" @click="navigateToLogIn">로그인</a>
                        </div>
                        <div class="nav-item text-end" v-if="store.isLogin">
                            <a class="nav-link text-black" href="" @click="navigateToProfile">프로필</a>
                        </div>
                        <div class="nav-item text-end" v-if="store.isLogin">
                            <a class="nav-link text-black" href="" @click.prevent="store.logOut">로그아웃</a>
                        </div>
                    </ul>
                </div>    
            </div>
        </nav>
        <div class="moving-image-container" @click="addPig">
          <img v-for="n in pigCount" :key="n" src="@/images/pig.png" alt="moving-img" class="moving">
            <!-- <img src="@/images/pig.png" alt="moving-img" class="moving">
            <img src="@/images/pig.png" alt="moving-img" class="moving">
            <img src="@/images/pig.png" alt="moving-img" class="moving">
            <img src="@/images/pig.png" alt="moving-img" class="moving">
            <img src="@/images/pig.png" alt="moving-img" class="moving"> -->
            <img src="@/images/coin.png" style="width: 50px; margin-left: 100px;">
        </div>
  <footer class="footer">&copy; COPYRIGHTS SSAFYRecommend. ALL RIGHTS RESERVED</footer>
    </template>
    
    <script setup>
    import { ref } from 'vue';
    import { useRouter } from 'vue-router';
    import { useCounterStore } from '@/stores/counter'
    
    const store = useCounterStore()
    const router = useRouter();
    const navigateToHome = () => {
        console.log('집으로가는중')
      router.push({ name: 'Home' });
    };
    
    const navigateToSignUp = () => {
        router.push({ name: 'SignUpView' });
    };
    
    const navigateToLogIn = () => {
        router.push({ name: 'LogInView' });
    };
    
    const navigateToCurrency = () => {
      router.push({ name: 'CurrencyView' });
    };
    const navigateToArticle = () => {
      router.push({ name: 'ArticleView' });
    };
    const navigateToMaps = () => {
      router.push({ name: 'maps' });
    };
    const navigateToFinlife = () => {
      router.push({ name: 'Finlife' });
    };
    const navigateToProfile = () => {
      router.push({ name: 'Profile' });
    };

    const pigCount = ref(3)
    const addPig = () => {
      pigCount.value += 1
      console.log('increase')
    }
    </script>
    
    <style scoped>
    
.moving {
  width: 60px;
  height: 60px;
}

@keyframes moveImage {
  0% { transform: translateX(0); }
  50% { transform: translateX(800px); }
  100% { transform: translateX(0); }
}

.moving-image-container {
  display: inline-block;
  animation: moveImage 13s infinite;
  position: fixed;
  bottom: 35px;
  z-index: 9998;
}

.footer {
  height: 30px;
  background-color: #f8f9fa;
  color: #343a40;
  position: fixed;
  bottom: 0;
  z-index: 9999;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
}
    </style>