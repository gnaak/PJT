<template>
  <div>
    <h5 style="margin-top: 50px; text-align: center;"><strong>당첨 번호를 뽑아보세요</strong></h5>
    <div class="servicebox"></div>
    <div class="lucky">
      <img class="img" src="@/images/clover.png" alt="lucky">
      <button @click="generateLotteryNumbers" class="custom-button">번호 뽑기</button>
    </div>
    <div v-if="lotteryNumbers.length > 0">
      <h5> 추천하는 행운의 번호</h5>
      <div style="display: flex; gap: 10px; justify-content: center;">
        <ul>
          <div v-for="number in lotteryNumbers" :key="number" :class="getNumberClass(number)">
            {{ number }}
          </div>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      lotteryNumbers: [],
    };
  },
  methods: {
    generateLotteryNumbers() {
      this.lotteryNumbers = this.shuffle([...Array(45).keys()].map((n) => n + 1)).slice(0, 7);
    },
    shuffle(array) {
      for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
      }
      return array;
    },
    getNumberClass(number) {
      // 숫자의 범위에 따라 클래스를 반환합니다.
      if (number <= 10) {
        return 'circle-number range-1';
      } else if (number <= 20) {
        return 'circle-number range-2';
      } else if (number <= 30) {
        return 'circle-number range-3';
      } else if (number <=40){
        return 'circle-number range-4';
      } else {
        return 'circle-number range-5'
      }
    },
  },
};
</script>

<style scoped>
/* 기존 스타일 유지 */
.circle-number {
  display: inline-block;
  width: 30px;
  height: 30px;
  line-height: 30px;
  text-align: center;
  border-radius: 50%;
  margin-right: 10px;
  box-shadow: 2px 2px 4px rgba(0.2, 0.2, 0.2, 0.2);
  text-shadow: -1px -1px 1px black, 1px -1px 1px black, -1px 1px 1px black, 1px 1px 1px black;

}

/* 추가된 스타일 */
.range-1 {
  background-color: rgb(216, 216, 73); /* 범위 1에 해당하는 색상 */
  color: white;
}

.range-2 {
  background-color: blue; /* 범위 2에 해당하는 색상 */
  color: white;

}

.range-3 {
  background-color: red; /* 범위 3에 해당하는 색상 */
  color: white;

}

.range-4 {
  background-color: gray; /* 범위 4에 해당하는 색상 */
  color: white;

}.range-5 {
  background-color: green; /* 범위 4에 해당하는 색상 */
  color: white;

}

.custom-button {
  border: 1px solid black;
  margin-top: 10px;
}

.img {
  width: 50px;
  height: 50px;
}

.lucky {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 10px;
  margin-bottom: 10px;
}
</style>
