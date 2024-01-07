<!-- ImageGallery.vue -->

<template>
    <div>
      <p>움직이는 이미지</p>
      <div v-for="(image, index) in images" :key="index" @click="addImage">
        <img :src="image" alt="Image" />
      </div>
    </div>
  </template>
  
  <script>
  export default {
  data() {
    return {
      images: ['/images/clover.png'],
    };
  },
  methods: {
    // addInitialImage() {
    //   // 초기 이미지 추가
    //   const initialImage = '@/images/clover.png'
    //   this.images.push(initialImage)
    // },
    addImage(index) {
      // 클릭 시 이미지 추가
      const baseImage = '/images/clover.png'
      const newImage = `${baseImage}?${this.images.length + 1}`
      this.images.push(newImage)
    },
  },
};
  </script>
  
  <style>
  /* 필요한 스타일 추가 */
  </style>
  