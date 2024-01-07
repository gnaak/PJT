<template>
  <div class="article">
    <div class="num">
      글 번호 : {{ article.id }}
    </div>
    <div>
      <p>글 제목 : {{ article.title }}</p>
    </div>
    <div class="titled">
      <p>작성 시간 : {{ formatCreatedAt(article.created_at) }}</p>
    </div>
    <div class="link">
      <RouterLink :to="{ name: 'DetailView', params: { id: article.id }}">
        게시글 상세보기
      </RouterLink>
    </div>
  </div>
  <hr class="one">
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  article: Object
})

const formatCreatedAt = (createdAt) => {
  const date = new Date(createdAt);
  const formattedDate = `${date.getFullYear()}-${(date.getMonth() + 1)
    .toString()
    .padStart(2, '0')}-${date.getDate().toString().padStart(2, '0')}`;
  const formattedTime = `${date.getHours().toString().padStart(2, '0')}:${date
    .getMinutes()
    .toString()
    .padStart(2, '0')}:${date.getSeconds().toString().padStart(2, '0')}`;

  return `${formattedDate} / ${formattedTime}`;
};
</script>
<style>

.article{
  display: flex;
  flex-direction: row;

}
.num {
  margin-right: 40px;

}

.titled{
  margin-right: 40px;
  margin-left: 40px;
}

.link {
  text-decoration: underline; /* You can customize the style */
  justify-content: left;
  left: 0px;
  margin-right: 40px;
  margin-left: 40px;
}
</style>

