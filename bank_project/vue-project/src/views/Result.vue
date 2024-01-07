<!-- ResultView.vue -->
<template>
  <div class="bank-recommendation">
    <div class="bank-recommendation-container">
      <h1>설문 결과</h1>
        <div>
          <div v-if="store.surveyData.intrRateType1 === 'S'" class="product-recommendation"> 
            <div v-for="product in product1.result.baseList" >
              <div v-for="item in product1.result.optionList">
                <div v-if="item.intr_rate_type_nm === '단리'">
                  <div v-if="product.fin_prdt_cd === item.fin_prdt_cd && store.surveyData.months == item.save_trm && product.join_way.includes(joinWay[store.surveyData.way-1]) && product.fin_co_no === product.fin_co_no" class="product-card">
                    <h2> {{ product.fin_prdt_nm }} </h2>
                    <p class="bank-name">{{ product.kor_co_nm }}</p>
                    <a href="" @click="addCart(product)" style="border: 1px solid blue; border-radius: 4px; background-color: #3498db; color: white;">상품 담기</a>
                    <div class="link" v-if="product.fin_co_no === '0010001'">
                      <a :href="`https://www.wooribank.com/`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0010002'">
                      <a :href="`https://www.standardchartered.co.kr/np/kr/Intro.jsp`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0010016'">
                      <a :href="`https://dgb.co.kr/dgb_ebz_main.jsp`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0010017'">
                      <a :href="`https://www.busanbank.co.kr/ib20/mnu/BHP00001`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0010019'">
                      <a :href="`https://pib.kjbank.com/ib20/mnu/BPB0000000001`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0010020'">
                      <a :href="`https://www.e-jejubank.com/JeJuBankInfo.do`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0010022'">
                      <a :href="`https://www.jbbank.co.kr/`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0010024'">
                      <a :href="`https://www.knbank.co.kr/`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0010026'">
                      <a :href="`https://mybank.ibk.co.kr/uib/jsp/index.jsp`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0010030'">
                      <a :href="`https://www.kdb.co.kr/index.jsp`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0010927'">
                      <a :href="`https://www.kbstar.com/`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0011625'">
                      <a :href="`https://www.shinhan.com/index.jsp`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0013175'">
                      <a :href="`http://banknh.kr/`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0013909'">
                      <a :href="`https://www.kebhana.com/`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0014674'">
                      <a :href="`https://www.kbanknow.com/ib20/mnu/PBKMAN000000`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0014807'">
                      <a :href="`https://www.suhyup-bank.com/`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0015130'">
                      <a :href="`https://www.kakaobank.com/`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0017801'">
                      <a :href="`https://www.tossbank.com/`">바로가기</a>
                    </div>
                    <p class="interest-rate">{{ product.mtrt_int }}</p>
                    <p class="additional-info">{{ product.etc_note }}</p>
                    <p class="interest-rate2">저축금리{{ item.intr_rate }}</p>
                    <p class="interest-rate2">최고우대금리{{ item.intr_rate2 }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
            
          <!-- 복리의 경우 -->
          <div v-if="store.surveyData.intrRateType1 === 'M'" class="product-recommendation"> 
            <div v-for="product in product1.result.baseList" >
              <div v-for="item in product1.result.optionList">
                <div v-if="item.intr_rate_type_nm === '복리'">
                  <div v-if="product.fin_prdt_cd === item.fin_prdt_cd && store.surveyData.months == item.save_trm && product.join_way.includes(joinWay[store.surveyData.way-1]) && product.fin_co_no === product.fin_co_no" class="product-card">
                    <h2> {{ product.fin_prdt_nm }} </h2>
                    <p class="bank-name">{{ product.kor_co_nm }}</p>
                    <a href="" @click="addCart(product)" style="border: 1px solid blue; border-radius: 4px; background-color: #3498db; color: white;">상품 담기</a>
                    <div class="link" v-if="product.fin_co_no === '0010001'">
                      <a :href="`https://www.wooribank.com/`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0010002'">
                      <a :href="`https://www.standardchartered.co.kr/np/kr/Intro.jsp`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0010016'">
                      <a :href="`https://dgb.co.kr/dgb_ebz_main.jsp`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0010017'">
                      <a :href="`https://www.busanbank.co.kr/ib20/mnu/BHP00001`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0010019'">
                      <a :href="`https://pib.kjbank.com/ib20/mnu/BPB0000000001`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0010020'">
                      <a :href="`https://www.e-jejubank.com/JeJuBankInfo.do`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0010022'">
                      <a :href="`https://www.jbbank.co.kr/`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0010024'">
                      <a :href="`https://www.knbank.co.kr/`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0010026'">
                      <a :href="`https://mybank.ibk.co.kr/uib/jsp/index.jsp`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0010030'">
                      <a :href="`https://www.kdb.co.kr/index.jsp`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0010927'">
                      <a :href="`https://www.kbstar.com/`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0011625'">
                      <a :href="`https://www.shinhan.com/index.jsp`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0013175'">
                      <a :href="`http://banknh.kr/`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0013909'">
                      <a :href="`https://www.kebhana.com/`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0014674'">
                      <a :href="`https://www.kbanknow.com/ib20/mnu/PBKMAN000000`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0014807'">
                      <a :href="`https://www.suhyup-bank.com/`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0015130'">
                      <a :href="`https://www.kakaobank.com/`">바로가기</a>
                    </div>
                    <div class="link" v-else-if="product.fin_co_no === '0017801'">
                      <a :href="`https://www.tossbank.com/`">바로가기</a>
                    </div>
                    <p class="interest-rate">{{ product.mtrt_int }}</p>
                    <p class="additional-info">{{ product.etc_note }}</p>
                    <p class="interest-rate2">저축금리{{ item.intr_rate }}</p>
                    <p class="interest-rate2">최고우대금리{{ item.intr_rate2 }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useCounterStore } from '@/stores/counter';
import axios from 'axios';
const store = useCounterStore();
const router = useRouter();

onMounted(() => {
  store.getFinlife();
});

const product1 = store.finlife;

const addCart =(product) => {
  console.log('상품이 제대로 나오나?', product.fin_prdt_nm)
  const existingCart = JSON.parse(localStorage.getItem('cart')) || []
  const isDuplicate = existingCart.length > 0 && existingCart.find((item) => item.fin_prdt_nm === product.fin_prdt_nm)
  // 중복이 아니라면 추가
  if(!isDuplicate) {
  alert('상품을 담습니다')
  existingCart.push(product)
} else {
  alert('이미 있는 상품입니다.')
}
  // 수정된 카트 데이터를 localStorage 에 저장
  localStorage.setItem('cart', JSON.stringify(existingCart))
}


const joinWay = [
    ('영업점'),
    ('인터넷'),
    ('스마트폰'),
    ('전화'),
    ('기타'),
  ]


</script>

<style scoped>

.link {
  margin-top: 10px;
  margin-bottom: 10px;
}

a {
  text-decoration: none;
  cursor: pointer;
  font-size: 0.9em;
  color: #3498db;
}

.classdiff {
  cursor: pointer;
  font-size: 1.7em;
  font-weight: 700;
}

.bank-recommendation {
  background-color: #f4f4f4;
  padding: 20px;
  height: 1800px;
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
  height: 55vh;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  border: 1px solid black;
}
.product-card h2 {
  font-size: 1.25em;
  margin-bottom: 8px;
  font-weight: bolder;
  margin-top: 20px;
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
</style>
