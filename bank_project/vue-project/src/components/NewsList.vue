<!-- NewsList.vue -->

<template>
  <div>
  <h5 style="margin-top: 50px; text-align: center;"><strong>최신 금융 뉴스</strong></h5>
  <div class="newsbox" style="margin-top: 20px;">
  <ul class="newslist"  v-if="defaultNewsList.length > 0">
    <li v-for="newsItem in defaultNewsList.slice(0, 5)" :key="newsItem.link">
      <a :href="newsItem.link" target="_blank">
      <div v-html="newsItem.title"></div>
    </a>
    </li>
  </ul>
 </div>
</div>
<div>
  <h5 style="margin-top: 10px; text-align: center;"><strong>뉴스 검색하기</strong></h5>
  <div class="search">
  <input v-model="searchQuery" placeholder="뉴스 검색어" class="input-box"/>
    <button class="input-button" @click="searchNews">검색</button>
  </div>

  <div style></div>
  <div class="newsbox">
  <ul class="newslist" v-if="newsList.length > 0">
    <li v-for="newsItem in newsList.slice(0, 5)" :key="newsItem.link">
      <a :href="newsItem.link" target="_blank">
        <div v-html="newsItem.title"></div>
      </a>
    </li>
  </ul>
 </div>
</div>
</template>

<script>
import axios from 'axios'

export default {
data() {
  return {
    searchQuery: '',
    newsList: [],
    defaultNewsList: []
  };
},
methods: {
  loadDefaultNews() {
    const apiUrl = 'http://127.0.0.1:8000/news/api/news/금융/'

    axios.get(apiUrl)
      .then(response => {
        this.defaultNewsList = response.data.items
      })
      .catch(error => {
        console.error('Error fetching default news:', error);
      })
  },

  searchNews() {
    const apiUrl = `http://127.0.0.1:8000/news/api/news/${encodeURIComponent(this.searchQuery)}/`

    axios.get(apiUrl)
      .then(response => {
        this.newsList = response.data.items
      })
      .catch(error => {
        console.error('Error fetching news:', error)
      });
  },
},
mounted() {
  // 컴포넌트가 마운트될 때 기본 금융 뉴스를 불러오는 메서드 호출
  this.loadDefaultNews();
},

};

</script>

<style>
.newsbox {
  display: flex;
  width: auto;
}

.newslist {
  text-align: left;
  font-size: 0.9em;
}

.newslist a {
  color: black;
  text-decoration: none; 
}

/* 금융 뉴스 제목에 적용되는 스타일 */
.newsbox .newslist a {
  color: black; /* 원하는 색상으로 변경 */
  text-decoration: none; /* 밑줄 제거 */
}

ul li,
ol li {
  margin-bottom: 8px; /* 각 리스트 아이템 간격 조절 */
  list-style: none; /* 목록 기호(쩜) 제거 */
}

.search {
  /* margin-left: 350px;
  width: 50%; */
  margin-left: auto; /* 왼쪽 여백을 최대로 확보 */
  margin-right: auto; /* 오른쪽 여백을 최대로 확보 */
  width: 70%; /* 적절한 폭 설정 */
  display: flex; /* 자식 요소들을 가로로 나열 */
  justify-content: center; /* 가운데 정렬 */
}

/* 추가된 스타일 */
.search-input {
  width: 70%; /* input 크기 조절 */
  padding: 8px; /* input padding 조절 */
}

.search-button {
  margin-left: 8px; /* 버튼과의 간격 조절 */

}

.search-result {
  font-size: 0.9em; /* 글씨 크기 키우기 */
}

.input-box{
 margin-right: 10px;
}
.input-button {
    width: 50px;
    height: 30px;
    background-color: #db9834 ;
    color: white;
    border: none;
    text-align: center;
    font-size: 16px;
    cursor: pointer;
    border-radius: 4px;
}
</style>
