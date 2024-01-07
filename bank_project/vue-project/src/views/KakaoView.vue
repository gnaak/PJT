<template>
  <div class="bank-recommendation">

    <div class="container">
      <div class="searchbox">
        <div class="input-container">
          <input
            type="text"
            v-model="searchInput"
            @focus="clearDefaultText"
            @blur="restoreDefaultText"
            @keyup.enter="searchPlace"
            />
            <button @click="getCurrentLocation">내 위치</button>
          </div>
          <div class="results">
            <div class="place" v-for="rs in search.results" :key="rs.id" @click="showPlace(rs)">
              <h6>{{ rs.place_name }}</h6>
              <span>{{ rs.address_name }}</span>
            </div>
          </div>
        </div>
        
        <div class="map-area">
          <kakaoMap class="kmap" :options="mapOption" />
        </div>
      </div>
    </div>
    </template>
  
  <script>
  import kakaoMap from '@/components/kakaoMap.vue'
  
  export default {
    components : {
      kakaoMap
    },
    data() {
      return {
        mapOption : {
          center : {
            lat: 37.5012860931305,
            lng: 127.039604663862,
          },
          level: 4,
        },  
        search: {
          keyword: null,
          pgn: null,
          results: []
        },
        searchInput:'검색어를 입력하세요'
      }
    },
    mounted() {},
    methods: {
      searchPlace(e) {
        // console.log(e)
        const keyword = e.target.value.trim()
        if (keyword.length ===0) {
          return;
        }
  
        const ps = new kakao.maps.services.Places()
        ps.keywordSearch(keyword, (data, status, pgn) => {
          this.search.keyword = keyword
          this.search.pgn = pgn
          this.search.results = data
        })
      },
      showPlace(place) {
        // console.log(place)
        this.mapOption.center = {
          lat: place.y,
          lng: place.x,
        }
        console.log(this.mapOption.center)
      },
      getCurrentLocation() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
          this.onSuccessGeolocation,
          this.onErrorGeolocation
        );
      } else {
        console.error("Geolocation is not supported by this browser.");
      }
    },
    onSuccessGeolocation(position) {
      const { latitude, longitude } = position.coords;
      this.mapOption.center = {
        lat: latitude,
        lng: longitude,
      };

      // 추가된 부분: 내 위치로 지도 이동 및 마커 표시
      this.$refs.kakaoMap.addMyLocationMarker(this.mapOption.center);
    },
    onErrorGeolocation(error) {
      console.error(`Error getting geolocation: ${error.message}`);
    },
    clearDefaultText() {
      if (this.searchInput === '검색어를 입력하세요') {
        this.searchInput = '';
      }
    },
    restoreDefaultText() {
      if (this.searchInput === '') {
        this.searchInput = '검색어를 입력하세요';
      }
    },
  },
};
  </script>
  
<style scoped>
.kmap {
  width: 100%;
  height: 800px;
}

/* 스타일 조정 시작 */
.container {
  display: flex;
}
.input-container {
  display: flex;
  align-items: center;
}

.searchbox {
  width: 24%; /* Adjust the width as needed */
  padding: 16px;
  background-color: #fff;
  border: 1px solid #dfe1e5;
  border-radius: 12px;
  margin-right: 16px;
}

button {
  background-color: #4285f4;
  color: #fff;
  border: none;
  padding: 8px;
  border-radius: 8px;
  cursor: pointer;
  margin-right: 8px;
}

input {
  flex: 1;
  border: none;
  padding: 8px;
  border-radius: 8px;
  outline: none;
}

.results {
  margin-top: 16px;
}

.place {
  background-color: #fff;
  border: 1px solid #dfe1e5;
  border-radius: 8px;
  padding: 8px;
  padding: 12px; /* Adjust the padding to change the size */
  margin-bottom: 8px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.place > span{
  text-align: left;
  font-size: smaller;
}
.place:hover {
  background-color: #f1f3f4;
}

.map-area {
  flex: 1;
  background-color: #f8f9fa;
  padding: 16px;
}

.bank-recommendation {
  background-color: #f4f4f4;
  padding: 20px;
  height: 850px;
}
</style>
