<template>
  <div class="bank-recommendation">
    <div class="login-container">
      <h1>작성한 글 상세보기</h1>
      <div v-if="article">
        <form class="login-form">
          <div class="form-group">
          </div>
          <div class="form-group">
            <!-- <strong>제목 :</strong>{{ article.title }} -->
            <strong>제목 :</strong>
          <template v-if="isEditing">
            <input v-model="article.title" class="edit-title" />
          </template>
          <template v-else>
            {{ article.title }}
          </template>
          </div>
          <div class="form-group">
            <!-- <strong>내용 :</strong> {{ article.content }} -->
            <strong>내용 :</strong>
          <template v-if="isEditing">
            <textarea v-model="article.content" class="edit-content"></textarea>
          </template>
          <template v-else>
            {{ article.content }}
          </template>
          </div>
          <div class="form-group">
            <strong>작성일 :</strong> {{ formatDate(article.created_at) }}
          </div>
          <div class="form-group">
            <strong>수정일 :</strong> {{ formatDate(article.updated_at) }}
          </div>
          <div class="form-group" v-if="article.user === store.accounts.pk">
            <button @click="deleteArticle" class="delete-button">게시글 삭제</button>
          </div>
          <div class="form-group" v-if="article.user === store.accounts.pk">
            <button @click.prevent="toggleEditMode" class="edit-button">{{ isEditing ? '취소' : '게시글 수정' }}</button>
          </div>
          <div class="form-group" v-if="isEditing">
          <button @click="saveChanges" class="edit-button">저장</button>
        </div>
        <div class="form-group">
          <CommentList :article="article" />
          <CreateComment :article="article"/>
          <div class="create">
          <RouterLink :to="{ name: 'ArticleView' }" class="create-text">
            목록으로
          </RouterLink>
          </div>
        </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'
import CommentList from '@/components/CommentList.vue';
import CreateComment from '@/components/CreateComment.vue';

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const article = ref(null)

const deleteArticle = () => {
  if (article.value) {
    axios({
      method: 'delete',
      url: `${store.API_URL}/api/v1/articles/${article.value.id}/delete/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then(() => {
        console.log('Article deleted successfully');
        router.push({ name: 'ArticleView' })
        // You may want to redirect or perform other actions after deletion
      })
      .catch((err) => {
        console.error('Error deleting article:', err);
      });
  }
};

onMounted(() => {
  store.getUserInfo();
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`
  })
    .then((res) => {
      article.value = res.data
    })
    .catch((err) => {
      router.push({ name: 'ArticleView' })
    })
})

const formatDate = (dateTimeString) => {
  const options = {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: 'numeric',
    minute: 'numeric',
    second: 'numeric',
    timeZoneName: 'short'
  }
  return new Date(dateTimeString).toLocaleDateString(undefined, options)
}

// 게시글 수정 토글 -> 수정 폼 -> 내용 저장 -> 업데이트
const isEditing = ref(false)
const toggleEditMode = () => {
  isEditing.value = !isEditing.value
}

const saveChanges = () => {
  if (article.value) {
    axios({
      method: 'put',
      url: `${store.API_URL}/api/v1/articles/${article.value.id}/`,
      headers: {
        Authorization: `Token ${store.token}`
      },
      data: {
        title: article.value.title,
        content: article.value.content
      }
    })
      .then(() => {
        console.log('게시글이 성공적으로 업데이트되었습니다')
        isEditing.value = false; // 변경 사항 저장 후 편집 모드 종료
      })
      .catch((err) => {
        console.error('게시글 업데이트 중 오류 발생:', err)
      })
  }
}
</script>

<style scoped>
strong {
  color: #1a0dab; /* Google blue color */
}


.create-text {
  font-size: 16px;
  color: #6f9efc;
  font-weight: 600;
  text-decoration: none;
  transition: color 0.3s;
  /* text-shadow: 2px 2px 4px rgba(241, 153, 153, 0.5); */
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
  width: 700px;
  justify-content: center;
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
  width: 500px;
}
.bank-recommendation {
  background-color: #f4f4f4;
  padding: 20px;
  height: 1200px;
}
.login-container {
  max-width: 400px;
  margin: auto;
  margin-top: 100px;
  text-align: center;
}

.contentbox {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  height: auto;
  overflow-y: auto;
}

.edit-button {
  background-color: #2ecc71;
  color: white;
  border: none;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  cursor: pointer;
  border-radius: 4px;
  width: 500px;
}

.edit-title {
  width: 400px;
  margin-left: 10px;
}

.edit-content {
  width: 400px;
  height: 250px;
  margin-left: 10px;
}

.create {
  display: flex;
  text-align: left;
}


</style>
