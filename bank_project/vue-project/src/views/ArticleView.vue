<template>
  <div class="bank-recommendation">
    <div class="login-container">
      <h1>커뮤니티</h1>
      <div class="create">
        <RouterLink :to="{ name: 'CreateView' }" class="create-text">
          새 글 작성하기
        </RouterLink>
      </div>
      <div class="article-box">
        <div v-if="store.articles && store.articles.length > 0">
          <ArticleList />
        </div> 
        <div v-else>
          <h6>작성된 글이 없습니다ㅠㅠ</h6>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import ArticleList from '@/components/ArticleList.vue'

const store = useCounterStore()

onMounted(() => {
  store.getArticles()
  console.log(store.articles)
})
</script>

<style scoped>
.bank-recommendation {
  background-color: #f4f4f4;
  padding: 20px;
  height: 900px;
}

.login-container {
  max-width: 850px;
  margin: auto;
  margin-top: 100px;
  text-align: center;
}

.create {
  display: flex;
  text-align: left;
}

.create-text {
  font-size: 16px;
  color: #6f9efc;
  font-weight: 600;
  text-decoration: none;
  transition: color 0.3s;
  /* text-shadow: 2px 2px 4px rgba(241, 153, 153, 0.5); */
}

.space {
  height: 30px;
}

h6 {
  font-size: 1.2em;
  margin-top: 20px;
}

.article-box {
  /* background-color: aliceblue;  */
  text-align: left;
  margin-top: 40px;
}

.article-list {
  margin-top: 20px;
  border-top: 1px solid #ccc;
  padding-top: 10px;
}
</style>
