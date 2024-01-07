<template>
  <div class="bank-recommendation">
    <div class="login-container">
      <h1>장바구니</h1>
    </div>
    <div class="bank-recommendation-container">
      <div v-if="cartItems.length>0" class="product-recommendation">
        <div v-for="product in cartItems" :key="product.kor_co_nm">
          <div class="product-card">
            <h2> {{ product.fin_prdt_nm }} </h2>
            <p class="bank-name">{{ product.kor_co_nm }}</p>
            <button @click="removeCart(product)" 
            style="border: 1px solid blue; border-radius: 4px; background-color: #3498db; color: white;">
            장바구니에서 삭제</button>
            <p class="interest-rate">{{ product.mtrt_int }}</p>
            <p class="additional-info">{{ product.etc_note }}</p>
            <p class="additional-info">{{ product.join_way }}</p>
            <p class="additional-info">{{ product.spcl_cnd }}</p>
            <div v-for="it in item">
              <div v-for="it2 in item2">
                <div v-if="product.fin_prdt_nm === it.fin_prdt_nm
                && it.fin_prdt_cd === it2.fin_prdt_cd">
                  <p class="inin-info">{{ it2.save_trm }}개월 : 저축금리{{ it2.intr_rate }}
                  / 최고 우대 금리 {{ it2.intr_rate2 }}</p>
                </div>
              </div>
            </div>
            <div v-for="it in items">
              <div v-for="it2 in items2">
                <div v-if="product.fin_prdt_nm === it.fin_prdt_nm
                && it.fin_prdt_cd === it2.fin_prdt_cd">
                  <p class="inin-info">{{ it2.save_trm }}개월 : 저축금리{{ it2.intr_rate }}
                  / 최고 우대 금리 {{ it2.intr_rate2 }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div v-else class="else">
        <div class="product-card2">
          <strong>장바구니에 담긴 상품이 없습니다ㅠㅠ</strong>
        </div>
        <a href="" @click="navigateToRecommendation">추천받으러가기</a>
      </div>
    </div>
  </div>
</template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { useRouter } from 'vue-router'
  import { useCounterStore } from '@/stores/counter';

  const router = useRouter()
  const store = useCounterStore()
  const cartItems = ref(null)
  
  cartItems.value = JSON.parse(localStorage.getItem('cart'))
  
  
  const removeCart = (product) => {
    // localStoage 에서 삭제
    // 현재 cartItems.value 에서 삭제
    // 1. 현재 localStorage 에 저장된 데이터를 가져오기
    // 이 코드는 valid 하기 위해 한 단계 더 작성했다고 생각하시면 됩니다.
    // const existingCart = JSON.parse(localStorage.getItem('cart'))
    alert('상품을 지웁니다')
    // 2. 삭제할 아이템 index 검색
    const itemIdx = cartItems.value.findIndex((item) => item.fin_prdt_nm === product.fin_prdt_nm)
    
    // 3. 데이터 삭제
    cartItems.value.splice(itemIdx, 1)
    
    // 4. 삭제된 데이터를 기준으로 데이터를 반영
    localStorage.setItem('cart', JSON.stringify(cartItems.value))
  }
  
  const navigateToRecommendation = () => {
  router.push({ name: 'Recommendation' });
};

onMounted(() => {
  store.getFinlife();
  store.getFinlife2();
});

const product1 = store.finlife;
const product2 = store.finlife2
const item = product1.result.baseList
const item2 = product1.result.optionList
const items = product2.result.baseList
const items2 = product2.result.optionList

// const items2 = product2.result.optionList
</script>

<style scoped>
.else {
  justify-self: center;
}
.product-card2{

  justify-self: center;
}
.login-container {
  max-width: 400px;
  margin: auto;
  margin-top: 100px;
  text-align: center;
}
.product-card h2 {
  font-size: 1.25em;
  margin-bottom: 8px;
  font-weight: bolder;
  margin-top: 20px;
}

.bank-recommendation {
  background-color: #f4f4f4;
  padding: 20px;
  height: 850px;
}

.bank-recommendation-container {
  max-width: 1600px;
  margin: auto;
  text-align: center;
  flex-wrap: wrap;
}
.product-recommendation {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  padding: 0px;  
  /* border: 1px solid red; */
}
.product-card {
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  margin: 20px;
  width: 18.7vw;
  height: 60vh;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  border: 1px solid black;
}

.bank-name {
  color: #3498db;
  font-weight: bold;
  margin-top: 10px;
  margin-bottom: 10px;
  font-size: 1.2em;
}

.interest-rate {
  color: #27ae60;
  margin-top: 8px;
  font-size: 0.96em;
}
.interest-rate2 {
  color: #ae2749;
  margin-top: 10px;
  font-size: 0.88em;
}

.additional-info {
  color: #555;
  font-size: 0.9em;
  margin-top: 12px;
  margin-bottom: 10px;
}
.inin-info {
  color: red;
  font-size: 0.8em;
  margin-top: 1px;
  margin-bottom: 10px;
}
  </style>
  