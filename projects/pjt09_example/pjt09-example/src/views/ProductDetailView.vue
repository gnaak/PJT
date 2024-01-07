<template>
    <div>
        <h3>상품 페이지</h3>
        <div v-if="product">
            <img :src="product.image" alt="">
            <strong>{{ product.title }}</strong>
            <p>가격 : ${{product.price}}</p>
            <button @click="goDetail(product)">상세 페이지로 이동</button>
        </div>
        <div v-else>로딩중 ...</div>
    </div>
</template>

<script setup>
import {ref} from 'vue'
import axios from 'axios';
import { useRoute } from 'vue-router';

const route = useRoute()
const product = ref('')
const productId = route.params.productId
console.log(productId)
const storeURL = `https://fakestoreapi.com/products/${productId}`

axios.get(storeURL)
    .then((response) => {
        console.log(response)
        product.value = response.data
    }). catch((error) => {
        console.error(error)
    })
</script>

<style scoped>

</style>