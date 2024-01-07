<template>
  <div class="bank-recommendation">
  <div class="survey-container">
  <p class="help">검색 조건을 입력하신 후, 금융상품 검색 결과를 확인하세요. 
                <a href="" @click="navigateToDeposit">예금</a>   /   <a href="" @click="navigateToDeposit2">적금</a>
  </p>
  <!-- 정기예금 -->
  <h3 class="sr-only">정기예금</h3>
  <form @submit.prevent="submitSurvey">
    <div class="text-set">
      <p>
        <strong>저축금액</strong>
      </p>
      <input type="text" v-model="form.inputContentMoneyFdrmDpst" maxlength="13" onkeyup="inputNumberFormat(this)" title="정기예금 저축금액">원
    </div>
  <section class="survey-form">
    <div class="m-sh">
      <div>
      </div>
      <div>
        <dt>저축 예정기간</dt>
        <div class="choice-group">
          <div class="label-list">
            <div class="check-set hide-sm">
              <div class="check">6개월
                <input type="radio" name="months" value="6" v-model="form.months">
              </div>
              <div class="check">12개월
                <input type="radio" name="months" value="12" v-model="form.months">
              </div>
              <div class="check">24개월
                <input type="radio" name="months" value="24" v-model="form.months">
              </div>
              <div class="check">36개월
                <input type="radio" name="months" value="36" v-model="form.months">
              </div>
            </div>
          </div>
        </div>
      </div>
      <div>
        <dt>금융권역</dt>
        <div class="choice-group">
          <div class="label-list">
            <div class="check-set hide-sm">
              <div class="check">은행
                <input type="radio" name="bank_local1" checked="checked" value="020000" v-model=form.bank_local1>
              </div>
              <div class="check">저축은행
                <input type="radio" name="bank_local1" value="030300" v-model=form.bank_local1>
              </div>
            </div>
          </div>
        </div>    
      </div>

          <dt>이자계산방식</dt>
          <div class="choice-group">
            <div class="label-list">
              <div class="check-set hide-sm">
                <div class="check">단리
                  <input type="radio" name="intrRateType1" value="S" v-model="form.intrRateType1">
                </div>
                <div class="check">복리
                  <input type="radio" name="intrRateType1" value="M" v-model="form.intrRateType1">
                </div>
              </div>
            </div>
          </div>
          
          
          <dt>지역선택</dt>
          <div class="choice-group">
            <div class="label-list">
              서울
              <input type="radio" name="location[]" value="01" v-model="form.location">
              &nbsp;부산
              <input type="radio" name="location[]" value="02" v-model="form.location">
              &nbsp;대구
              <input type="radio" name="location[]" value="03" v-model="form.location">
              &nbsp;인천
              <input type="radio" name="location[]" value="04" v-model="form.location">
              &nbsp;광주
              <input type="radio" name="location[]" value="05" v-model="form.location">
              &nbsp;대전
              <input type="radio" name="location[]" value="06" v-model="form.location">
              &nbsp;울산
              <input type="radio" name="location[]" value="07" v-model="form.location">
              &nbsp;세종
              <input type="radio" name="location[]" value="08" v-model="form.location">
              &nbsp;경기
              <input type="radio" name="location[]" value="09" v-model="form.location">
              &nbsp;강원
              <input type="radio" name="location[]" value="10" v-model="form.location">
            </div>
          </div>
          <div class="choice-group">
            <div class="label-list">
              충북
              <input type="radio" name="location[]" value="11" v-model="form.location">
              &nbsp;충남
              <input type="radio" name="location[]" value="12" v-model="form.location">
              &nbsp;전북
              <input type="radio" name="location[]" value="13" v-model="form.location">
              &nbsp;전남
              <input type="radio" name="location[]" value="14" v-model="form.location">
              &nbsp;경북
              <input type="radio" name="location[]" value="15" v-model="form.location">
              &nbsp;경남
              <input type="radio" name="location[]" value="16" v-model="form.location">
              &nbsp;제주
              <input type="radio" name="location[]" value="17" v-model="form.location">
                  
            </div>
          </div>

        <dt>
          가입대상
          <div class="tooltip" tabindex="0">
            <span class="sr-only">용어설명</span>
            <div class="tooltiptext">
              <ul>
                <li><span class="t">&nbsp;제한없음</span> <span>일반인 대상의 상품</span></li>
                <li><span class="t">&nbsp;서민전용</span> <span>기초생활수급자 등 서민우대상품으로 상세정보의 가입대상 요건 확인</span></li>
                <li><span class="t">&nbsp;일부제한</span> <span>특정인 대상 상품으로 상세정보의 가입대상 요건 확인</span></li>
              </ul>
            </div>
          </div>
        </dt>
      
        <div class="choice-group">
          <div class="label-list">
              제한없음
              <input type="radio" name="limits[]" checked="checked" value="1" v-model="form.limits">
              &nbsp;서민전용
              <input type="radio" name="limits[]" value="2" v-model="form.limits">
              &nbsp;일부제한
              <input type="radio" name="limits[]" value="3" v-model="form.limits">
          </div>
        </div>
        
        <dt>가입방법</dt>
          <div class="choice-group">
            <div class="label-list">
              영업점
              <input type="radio" name="way[]" id="joinWay1_24" value="1" v-model="form.way">
              &nbsp;인터넷
              <input type="radio" name="way[]" id="joinWay1_25" value="2" v-model="form.way">
              &nbsp;스마트폰
              <input type="radio" name="way[]" id="joinWay1_26" value="3" v-model="form.way">
              &nbsp;전화(텔레뱅킹)                
              <input type="radio" name="way[]" id="joinWay1_28" value="4" v-model="form.way">
              &nbsp;기타
              <input type="radio" name="way[]" id="joinWay1_29" value="5" v-model="form.way">
              </div>
            </div>
            <dl>
              <dt>우대조건</dt>
              <dd>
                <div class="choice-group">
            <div class="label-list">
              비대면 가입
                <input type="radio" name="spclCndCdFdrmDpst[]" id="spclCndCd1_45" value="1" v-model="form.spclCndCdFdrmDpst">
                &nbsp;재예치
                <input type="radio" name="spclCndCdFdrmDpst[]" id="spclCndCd1_46" value="2" v-model="form.spclCndCdFdrmDpst">
                &nbsp;주거래(급여, 연금 이체 등)
                <input type="radio" name="spclCndCdFdrmDpst[]" id="spclCndCd1_47" value="3" v-model="form.spclCndCdFdrmDpst">
                &nbsp;첫거래
                <input type="radio" name="spclCndCdFdrmDpst[]" id="spclCndCd1_48" value="4" v-model="form.spclCndCdFdrmDpst">
                &nbsp;연령
                <input type="radio" name="spclCndCdFdrmDpst[]" id="spclCndCd1_49" value="5" v-model="form.spclCndCdFdrmDpst">
                &nbsp;타상품가입·실적
                <input type="radio" name="spclCndCdFdrmDpst[]" id="spclCndCd1_50" value="6" v-model="form.spclCndCdFdrmDpst">
              </div>
          </div>
          <br>
        </dd>
      </dl>
    </div>
      <button class="search" type="submit">금융상품 검색</button>
  </section>
  </form>
</div>
</div>
</template>

  
<script setup>
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { useRouter } from 'vue-router';

const store = useCounterStore();
const router = useRouter();

const form = ref({
  inputContentMoneyFdrmDpst: '10,000,000',
  months: '',
  bank_local1: '',
  intrRateType1: '',
  location: '',
  limits: '',
  way: '',
  spclCndCdFdrmDpst: '',
});

const navigateToDeposit = () => {
  router.push({ name: 'Recommendation' });
};

const navigateToDeposit2 = () => {
  router.push({ name: 'Recommendation2' });
};


const submitSurvey = () => {
  // if (!form.months) {
    // 사용자에게 알림을 보여주거나 다른 조치를 취한다.
    // alert("저축 예정기간을 선택해주세요.");
    store.submitSurvey(form.value);
    console.log(store.surveyData)
  if (!store.surveyData.months) {
    // 사용자에게 알림을 보여주거나 다른 조치를 취한다.
    alert("저축 예정기간을 선택해주세요.");
    return;
  }
  if (!store.surveyData.intrRateType1) {
    // 사용자에게 알림을 보여주거나 다른 조치를 취한다.
    alert("이자계산방식을 선택해주세요.");
    return;
  }
  if (!store.surveyData.location) {
    // 사용자에게 알림을 보여주거나 다른 조치를 취한다.
    alert("지역을 선택해주세요.");
    return;
  }
  if (!store.surveyData.way) {
    // 사용자에게 알림을 보여주거나 다른 조치를 취한다.
    alert("가입방법을 선택해주세요.");
    return;
  }
    router.push({ name: 'Result' });
  };
</script>

<style scoped>

.btns {
  display: flex;
  align-items: center;
}
.bank-recommendation {
  background-color: #f4f4f4;
  padding: 20px;
  height: 1300px;
}
.survey-container {
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  background-color: #f9f9f9;
}

.help {
  font-size: 16px;
  color: #333;
  text-align: center;
}
.sr-only {
  font-size: 26px;
  color: #333;
  text-align: center;
  font-weight: 700;
}
.survey-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #fff; /* survey 내용에만 백그라운드 추가 */
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  margin-top: 20px;
}

.text-set {
  width: 100%;
  margin: 10px 0;
  text-align: right
}

.choice-group{
  text-align: left;
  margin: 10px;
}
.inputContentMoneyFdrmDpst {
  width: calc(100% - 16px);
  padding: 10px;
  font-size: 16px;
  margin-bottom: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.checkbox-group {
  display: flex;
  gap: 10px;
  margin-top: 10px;
}

.checkbox-group label {
  font-size: 14px;
  display: flex;
  align-items: center;
}

.tooltip {
  position: relative;
  display: inline-block;
  cursor: pointer;
}

.tooltip .tooltiptext {
  visibility: hidden;
  width: 200px;
  background-color: #555;
  color: #fff;
  text-align: center;
  border-radius: 6px;
  padding: 8px;
  position: absolute;
  z-index: 1;
  bottom: 125%;
  left: 50%;
  margin-left: -100px;
  opacity: 0;
  transition: opacity 0.3s;
}

.tooltip:hover .tooltiptext {
  visibility: visible;
  opacity: 1;
}

.button-group {
  margin-top: 20px;
}

.search {
  background-color: #4caf50;
  color: white;
  border: none;
  width: 40%;
  font-size: 18px;
  cursor: pointer;
  border-radius: 4px;
  transition: background-color 0.3s;
}

button.search:hover {
  background-color: #45a049;
}
</style>