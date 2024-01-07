<template>
  <div class="title">
    <ArticleListItem 
      v-for="article in store.articles"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import ArticleListItem from '@/components/ArticleListItem.vue'

const store = useCounterStore()
// console.log(store.articles)

</script>
<style scoped>
.title {
  display: flex;
  flex-direction: column;
  height: 500px;
}
</style>