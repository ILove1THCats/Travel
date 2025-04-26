// mapapp/static/mapapp/script.js
const { createApp } = Vue

createApp({
  data() {
    return {
      locations: [],
      map: null
    }
  },
  mounted() {
    this.initMap();
    this.getLocations();
  },
  methods: {
    initMap() {
      // Khởi tạo bản đồ Leaflet ở TP.HCM
      this.map = L.map('map').setView([10.762622, 106.660172], 12);
      L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
      }).addTo(this.map);
    },
    async getLocations() {
      try {
        const response = await fetch('/locations/'); // Django URL
        this.locations = await response.json();
        this.addMarkersToMap();
      } catch (error) {
        console.error('Lỗi khi lấy dữ liệu:', error);
      }
    },
    addMarkersToMap() {
      this.locations.forEach(location => {
        const marker = L.marker([location.latitude, location.longitude]).addTo(this.map);
        marker.bindPopup(`<b>${location.name}</b><br>${location.description}`).openPopup();
      });
    }
  }
}).mount('#app')