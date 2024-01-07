<template>
    <div class="bank-recommendation">
      <div class="bank-recommendation-container">
        <div class="selection">
          <label for="bankDropdown">국가 선택 :  &nbsp;</label>
          <select id="bankDropdown" @change="selectBank($event.target.value)">
            <option value="1">전체</option>
              <template v-for="gnak in unique">
                <option>{{ gnak }}</option>
              </template>
          </select>
        </div>
        <h1>환율 계산기</h1>
        <form @submit.prevent="calculateExchange" class="exchange-form">
            <div class="form-group">
              <label for="amount"></label>
              <input type="number" id="amount" v-model="amount" placeholder="금액을 입력하세요" />
            </div>
            <button type="submit">\</button>
          </form>
  
          <div v-for="current in currencies" :key="product.dcls_month" class="product-recommendation">
            <div v-for="item in product.baseList" :key="item.fin_prdt_cd" class="product-cards">
              <div v-if="selectedBank === '1' || !selectedBank" class="product-card">
                <div class="product-card-child">
                  <h2>{{ item.fin_prdt_nm }}</h2>
                  <p class="bank-name">{{ item.kor_co_nm }}</p>
                  <div class="link" v-if="item.fin_co_no === '0010001'">
                    <a :href="`https://www.wooribank.com/`">바로가기</a>
                  </div>
                  <div class="link" v-else-if="item.fin_co_no === '0010002'">
                    <a :href="`https://www.standardchartered.co.kr/np/kr/Intro.jsp`">바로가기</a>
                  </div>
                  <div class="link" v-else-if="item.fin_co_no === '0010016'">
                    <a :href="`https://dgb.co.kr/dgb_ebz_main.jsp`">바로가기</a>
                  </div>
                  <div class="link" v-else-if="item.fin_co_no === '0010017'">
                    <a :href="`https://www.busanbank.co.kr/ib20/mnu/BHP00001`">바로가기</a>
                  </div>
                  <div class="link" v-else-if="item.fin_co_no === '0010019'">
                    <a :href="`https://pib.kjbank.com/ib20/mnu/BPB0000000001`">바로가기</a>
                  </div>
                  <div class="link" v-else-if="item.fin_co_no === '0010020'">
                    <a :href="`https://www.e-jejubank.com/JeJuBankInfo.do`">바로가기</a>
                  </div>
                  <div class="link" v-else-if="item.fin_co_no === '0010022'">
                    <a :href="`https://www.jbbank.co.kr/`">바로가기</a>
                  </div>
                  <div class="link" v-else-if="item.fin_co_no === '0010024'">
                    <a :href="`https://www.knbank.co.kr/`">바로가기</a>
                  </div>
                  <div class="link" v-else-if="item.fin_co_no === '0010026'">
                    <a :href="`https://mybank.ibk.co.kr/uib/jsp/index.jsp`">바로가기</a>
                  </div>
                  <div class="link" v-else-if="item.fin_co_no === '0010030'">
                    <a :href="`https://www.kdb.co.kr/index.jsp`">바로가기</a>
                  </div>
                  <div class="link" v-else-if="item.fin_co_no === '0010927'">
                    <a :href="`https://www.kbstar.com/`">바로가기</a>
                  </div>
                  <div class="link" v-else-if="item.fin_co_no === '0011625'">
                    <a :href="`https://www.shinhan.com/index.jsp`">바로가기</a>
                  </div>
                  <div class="link" v-else-if="item.fin_co_no === '0013175'">
                    <a :href="`http://banknh.kr/`">바로가기</a>
                  </div>
                  <div class="link" v-else-if="item.fin_co_no === '0013909'">
                    <a :href="`https://www.kebhana.com/`">바로가기</a>
                  </div>
                  <div class="link" v-else-if="item.fin_co_no === '0014674'">
                    <a :href="`https://www.kbanknow.com/ib20/mnu/PBKMAN000000`">바로가기</a>
                  </div>
                  <div class="link" v-else-if="item.fin_co_no === '0014807'">
                    <a :href="`https://www.suhyup-bank.com/`">바로가기</a>
                  </div>
                  <div class="link" v-else-if="item.fin_co_no === '0015130'">
                    <a :href="`https://www.kakaobank.com/`">바로가기</a>
                  </div>
                  <div class="link" v-else-if="item.fin_co_no === '0017801'">
                    <a :href="`https://www.tossbank.com/`">바로가기</a>
                  </div>
                  <p class="interest-rate">{{ item.mtrt_int }}</p>
                  <p class="additional-info">{{ item.etc_note }}</p>
                </div>
              </div>
              <div v-if="selectedBank === item.kor_co_nm" class="product-card">
              <h2>{{ item.fin_prdt_nm }}</h2>
              <p class="bank-name">{{ item.kor_co_nm }}</p>
              <div class="link" v-if="item.fin_co_no === '0010001'">
                <a :href="`https://www.wooribank.com/`">바로가기</a>
              </div>
              <div class="link" v-else-if="item.fin_co_no === '0010002'">
                <a :href="`https://www.standardchartered.co.kr/np/kr/Intro.jsp`">바로가기</a>
              </div>
              <div class="link" v-else-if="item.fin_co_no === '0010016'">
                <a :href="`https://dgb.co.kr/dgb_ebz_main.jsp`">바로가기</a>
              </div>
              <div class="link" v-else-if="item.fin_co_no === '0010017'">
                <a :href="`https://www.busanbank.co.kr/ib20/mnu/BHP00001`">바로가기</a>
              </div>
              <div class="link" v-else-if="item.fin_co_no === '0010019'">
                <a :href="`https://pib.kjbank.com/ib20/mnu/BPB0000000001`">바로가기</a>
              </div>
              <div class="link" v-else-if="item.fin_co_no === '0010020'">
                <a :href="`https://www.e-jejubank.com/JeJuBankInfo.do`">바로가기</a>
              </div>
              <div class="link" v-else-if="item.fin_co_no === '0010022'">
                <a :href="`https://www.jbbank.co.kr/`">바로가기</a>
              </div>
              <div class="link" v-else-if="item.fin_co_no === '0010024'">
                <a :href="`https://www.knbank.co.kr/`">바로가기</a>
              </div>
              <div class="link" v-else-if="item.fin_co_no === '0010026'">
                <a :href="`https://mybank.ibk.co.kr/uib/jsp/index.jsp`">바로가기</a>
              </div>
              <div class="link" v-else-if="item.fin_co_no === '0010030'">
                <a :href="`https://www.kdb.co.kr/index.jsp`">바로가기</a>
              </div>
              <div class="link" v-else-if="item.fin_co_no === '0010927'">
                <a :href="`https://www.kbstar.com/`">바로가기</a>
              </div>
              <div class="link" v-else-if="item.fin_co_no === '0011625'">
                <a :href="`https://www.shinhan.com/index.jsp`">바로가기</a>
              </div>
              <div class="link" v-else-if="item.fin_co_no === '0013175'">
                <a :href="`http://banknh.kr/`">바로가기</a>
              </div>
              <div class="link" v-else-if="item.fin_co_no === '0013909'">
                <a :href="`https://www.kebhana.com/`">바로가기</a>
              </div>
              <div class="link" v-else-if="item.fin_co_no === '0014674'">
                <a :href="`https://www.kbanknow.com/ib20/mnu/PBKMAN000000`">바로가기</a>
              </div>
              <div class="link" v-else-if="item.fin_co_no === '0014807'">
                <a :href="`https://www.suhyup-bank.com/`">바로가기</a>
              </div>
              <div class="link" v-else-if="item.fin_co_no === '0015130'">
                <a :href="`https://www.kakaobank.com/`">바로가기</a>
              </div>
              <div class="link" v-else-if="item.fin_co_no === '0017801'">
                <a :href="`https://www.tossbank.com/`">바로가기</a>
              </div>
              
              
              <p class="interest-rate">{{ item.mtrt_int }}</p>
              <p class="additional-info">{{ item.etc_note }}</p>
            </div>
          </div>
        </div> -->
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted, computed } from 'vue';
  import { useCounterStore } from '@/stores/counter';
  import { useRouter } from 'vue-router';
  
  const router = useRouter();
  const store = useCounterStore();
  
  onMounted(() => {
    store.getFinlife();
  });
  
  
  const currencies = store.exchangeRate;
  // console.log(products.result.baseList)
  
  const unique = new Set()
    for (const currency of currencies){
      unique.add(currency)
    }
  console.log(unique)
  
  //
  const selectedBankCode = ref(null);
  
  
  const selectedBank = ref('')
  // Add a method to set the selected bank code
  const selectBank = (e) => {
    console.log(e)
    selectedBank.value = e
    console.log(selectedBank)
  };
  //
  const filteredProducts = computed(() => {
  if (!selectedBankCode.value) {
    return products.result.baseList;
  } else {
    return products.result.baseList.filter((item) => item.kor_co_nm === selectedBankCode.value);
  }
  });
  
  </script>
  
  <style scoped>
  
  .selection {
    text-align: left;  /* Align text to the left */
    font-size: 15px;
    margin-top: 10px;   /* Add margin to the top */
    margin-bottom: 10px;   /* Add margin to the bottom */
  }
  
  .link{
    margin-top: 10px;
    margin-bottom: 10px;
  }
  a {
    text-decoration: none; /* 밑줄 제거 */
    cursor: pointer; /* 커서 모양 변경 (선택 사항) */
    font-size: 0.9em;
  }
  
  .classdiff {
    cursor: pointer; /* 커서 모양 변경 (선택 사항) */
    font-size: 1.7em;
    font-weight: 700;
  }
  .bank-recommendation {
    background-color: #f4f4f4;
    padding: 20px;
  }
  
  .bank-recommendation-container {
    max-width: 1600px;
    margin: auto;
    text-align: center;
  }
  
  .product-recommendation {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    padding: 0px;
    
  }
  
  /* .product-cards {
    display: inline-block;
    border: 1px solid black;
  } */
  
  .product-card {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    margin: 20px;
    width: 18.7vw;
    height: 50vh;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
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
  
  .additional-info {
    color: #555;
    font-size: 0.9em;
    margin-top: 12px;
    margin-bottom: 10px;
  }
  </style>
  