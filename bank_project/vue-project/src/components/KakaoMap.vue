<!-- KakaoMap.vue -->
<template>
  <div ref="map"></div>
</template>

<script>
export default {
  props: ['options'],
  data() {
    return {
      // 추가된 부분: 내 위치 마커를 저장하는 변수
      myLocationMarker: null,
    };
  },
  mounted() {
    this.updateMapCenter(); // 초기에도 중앙 위치로 지도를 설정해야 합니다.
  },

  watch: {
    'options.center': 'updateMapCenter',
  },

  methods: {
    updateMapCenter() {
      const { center, level } = this.options;
      const mapInstance = new kakao.maps.Map(this.$refs.map, {
        center: new kakao.maps.LatLng(center.lat, center.lng),
        level: level,
      });

      // 추가된 부분: 내 위치 마커를 추가
      this.addMyLocationMarker(center, mapInstance);
    },
    addMyLocationMarker(center, mapInstance) {
      // 기존 마커가 있다면 제거
      if (this.myLocationMarker) {
        this.myLocationMarker.setMap(null);
      }

      // 새로운 마커 생성
      this.myLocationMarker = new kakao.maps.Marker({
        position: new kakao.maps.LatLng(center.lat, center.lng),
        map: mapInstance,
        title: '현재 위치',
      });
    },
  },
};
</script>

<style scoped>
.k-map {
  width: 600px;
  height: 600px;
}

.bank-recommendation {
  background-color: #f4f4f4;
  padding: 20px;
}
</style>
