<template>
  <div class="bank-recommendation">
    <div class="bank-recommendation-container">
      <div class="selection">
        <label for="bankDropdown">국가 선택 :  &nbsp;</label>
        <select id="bankDropdown" @change="selectBank($event.target.value)" v-model="selectedCurrency">
          <option value="1">전체</option>
          <template v-for="gnak in unique">
            <option>{{ gnak.cur_nm }}</option>
          </template>
        </select>
      </div>
      <h1>환율 계산기</h1>
      <form @submit.prevent="calculateExchange" class="exchange-form">
        <div class="form-group">
          <label for="amount"></label>
          <input type="number" id="amount" v-model="amount" placeholder="금액을 입력하세요" />
          <button type="submit">\</button>
        </div>
        <div class="result" v-if="convertedAmount !== null">
          <p>환전 결과:</p>
          <p>{{ amount }}원은 약 {{ convertedAmount.toFixed(4) }} {{ selectedCurrency }}입니다.</p>
        </div>
      </form>
      <form @submit.prevent="calculateExchange2" class="exchange-form">
        <div class="form-group">
          <label for="amount"></label>
          <input type="number" id="amount" v-model="amount2" placeholder="금액을 입력하세요" />
          <button type="submit">$</button>
        </div>
        <div class="result" v-if="convertedAmount !== null">
          <p>환전 결과:</p>
          <p>{{ amount2 }}{{ selectedCurrency }}은 약 {{ convertedAmount.toFixed(4) }}원 입니다.</p>
        </div>
      </form>
      <div class="product-recommendation">
        <div v-for="current in currencies" class="product-card">
            <h2>국가/통화명</h2> 
            <h2>{{ current.cur_nm }}</h2>
            <p>전신환(송금) 받으실 때: {{ current.ttb }}</p>
            <p>전신환(송금) 보내실 때 : {{ current.ttb }}</p>
            <p>매매 기준율 : {{ current.deal_bas_r }}</p>
            <p>장부 가격 : {{ current.bkpr }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore();

onMounted(() => {
  store.getExchangeRate()
});

const amount = ref(0);
const amount2 = ref(0)
const selectedCurrency = ref('');
const convertedAmount = ref(null);
const currencies = store.exchangeRate;

const calculateExchange = function () {
  const selectedCurrencyInfoArray = currencies.filter(currency => currency.cur_nm === selectedCurrency.value);
  const selectedCurrencyInfo = selectedCurrencyInfoArray.length > 0 ? selectedCurrencyInfoArray[0] : null;

  if (selectedCurrencyInfo) {
    const rate = parseFloat(selectedCurrencyInfo.deal_bas_r.replace(/,/g, ''));
    convertedAmount.value = amount.value / rate;
  }
}
const calculateExchange2 = function () {
  const selectedCurrencyInfoArray = currencies.filter(currency => currency.cur_nm === selectedCurrency.value);
  const selectedCurrencyInfo = selectedCurrencyInfoArray.length > 0 ? selectedCurrencyInfoArray[0] : null;

  if (selectedCurrencyInfo) {
    const rate = parseFloat(selectedCurrencyInfo.deal_bas_r.replace(/,/g, ''));
    convertedAmount.value = amount2.value * rate;
  }
}

const unique = new Set()
for (const currency of currencies){
  unique.add(currency)
}

const selectedBank = ref('')
// Add a method to set the selected bank code
const selectBank = (e) => {
  console.log(e)
  selectedBank.value = e
  console.log(selectedBank)
};

</script>

<style scoped>


#bankDropdown{
  max-width: 180px;
  height: 38px;
}

.bank-recommendation {
  background-color: #f4f4f4;
  padding: 20px;
  height: 2050px;
}

.product-card h2 {
  font-size: 1.09em;
  margin-bottom: 8px;
  font-weight: bolder;
  margin-top: 20px;
}
.exchange-form {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-top: 16px;
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
  width: 11.5vw;
  height: 35vh;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.form-group {
  text-align: center;
}

label {
  display: block;
  margin-bottom: 4px;
}

input,
select {
  width: 40%;
  padding: 8px;
  font-size: 14px;
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
}

.result {
  margin-top: 20px;
  padding: 10px;
  background-color: #ecf0f1;
  border-radius: 4px;
}
.bank-recommendation-container {
  max-width: 1600px;
  margin: auto;
  text-align: center;
}
.selection {
  text-align: left;  /* Align text to the left */
  font-size: 15px;
  margin-top: 10px;   /* Add margin to the top */
  margin-bottom: 10px;   /* Add margin to the bottom */
  height: 20px;
}
</style>
