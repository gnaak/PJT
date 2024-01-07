<template>
  <header>
    <Navigation/>
    <!-- <KakaoMap /> -->
  </header>
  <RouterView />
</template>

<script setup>
import Navigation from '@/components/Navigation.vue';
import { RouterView } from 'vue-router'
import KakaoMap from "@/components/KakaoMap.vue";


</script>
