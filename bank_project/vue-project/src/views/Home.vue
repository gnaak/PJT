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
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
    </head>
    <div class="bank-recommendation">
        <div id="carouselExample" class="carousel slide custom-header" data-bs-ride="carousel" data-bs-interval="4000">
            <div class="carousel-inner">
                <div class="gnak">
                    <div class="carousel-item active">
                        <img src="@/images/header1.png" class="d-block w-100" alt="...">
                    </div>
                    <div class="carousel-item">
                        <img src="@/images/header2.png" class="d-block w-100" alt="...">
                    </div>
                    <div class="carousel-item">
                        <img src="@/images/header3.png" class="d-block w-100" alt="...">
                    </div>
                    <div class="carousel-item">
                        <img src="@/images/header4.png" class="d-block w-100" alt="...">
                    </div>
                </div>
            </div>
            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
            </button>
        </div>
        <div class="iconname">
            <h3>서비스</h3>
        </div>
        <div class="iconcontainer">
        <!-- <div class="row row-cols-3 row-cols-md-6 row-cols-lg-6"> -->
            <div class="iconbox">
                <RouterLink to="/finlife">
                <img class="iconimg" src="@/images/pig1.png">
                </RouterLink>
                <div class="icontext">예금</div>
            </div>
            <div class="iconbox">
                <RouterLink to="/finlife2">
                <img class="iconimg" src="@/images/pig2.png">
                </RouterLink>
                <div class="icontext">적금</div>
            </div>
            <div class="iconbox">
                <RouterLink to="/">
                <img class="iconimg" src="@/images/home.png">
                </RouterLink>
            <div class="icontext">전세대출</div>
        </div>
        <div class="iconbox">
            <RouterLink to="/currency">
                <img class="iconimg" src="@/images/exchange.png">
            </RouterLink>
            <div class="icontext">환율</div>
        </div>
        <div class="iconbox">
            <RouterLink to="/maps">
                <img class="iconimg" src="@/images/map.png">
            </RouterLink>
            <div class="icontext">지도</div>
        </div>
        <div class="iconbox">
            <RouterLink to="/article">
                <img class="iconimg" src="@/images/community.png">
            </RouterLink>
            <div class="icontext">커뮤니티</div>
        </div>
        <!-- </div> -->
    </div>
    
    <div class="iconname">
        <h3>기타 서비스</h3>
        <div>
            <div style="display: flex; justify-content: center;"></div>
        </div>
    </div>
    
    
    <div class="container">
        <div class="row row-cols-1 row-cols-md-2 row-cols-lg-2">
            <div class="col">
                <div class="card-border">
                    <div class="card">
                        <div class="numbertext">
                            <Lottery />
                            <p class="card-text">Lotto 6/45<br><br>45개의 숫자 중 6개를 맞히면 1등!</p>
                            <p style="margin: 10px;">매주 토요일 오후 8시 35분 당첨자를 추첨합니다</p>
                            <a href="https://m.dhlottery.co.kr/common.do?method=main">동행복권 홈페이지 바로가기</a>
                        </div>
                    </div>
                </div>
            </div>
            <div class="numbertext">
                <div class="card">
                    <div>
                        <NewsList />
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

    <footer class="footer">&copy; COPYRIGHTS SSAFYRecommend. ALL RIGHTS RESERVED</footer>
</template>

<script setup>
import 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js';
import { useCounterStore } from '@/stores/counter'
import { RouterLink, RouterView } from 'vue-router'
import Lottery from '@/components/Lottery.vue';
import NewsList from '@/components/NewsList.vue';
const store = useCounterStore()

</script>


<style scoped>
@import 'bootstrap/dist/css/bootstrap.min.css';

.carousel-inner{
    align-items: center;
    justify-content: center;
}
.carousel-item{
    width: 82%;
    height: 610px;
    margin-left:120px;
}

@media (max-width: 1399px) {
    .custom-header {
        width: 100%;
    }
}

@media (min-width: 1400px) {
    .custom-header {
        width: 1320px;
        margin: auto;
    }
}

.box {
    border: 1px solid black;
    background-color: white;
    text-align: left;
}

.w-100 {
    height: 650px;
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
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1)
}

.iconcontainer {
    display: flex;
    flex-direction: row;
    justify-content: center;
    gap: 50px;

}

.iconimg {
    width: 90px;
    height: 90px;

}

.icontext {
    text-align: center;
}


.iconname {
    display: flex;
    justify-content: center;
    margin: 20px;
}

.card {
    height: 500px;
}

.card-border {
    background-color: #e3f2fd;

}

.card-text {
    text-align: center;
}

.numbertext {
    background-color: #e3f2fd;
    height: 500px;
    text-align: center;
}

.bank-recommendation {
  background-color: #f4f4f4;
  padding: 20px;
  height: 1800px;
  box-sizing: border-box;
}


</style>