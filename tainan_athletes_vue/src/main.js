import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from "axios";


// 設置全局 Axios Authorization Header
// axios.interceptors.request.use((config) => {
// 	const token = localStorage.getItem("accessToken");
// 	if (token) {
// 		config.headers.Authorization = `Bearer ${token}`;
// 	}
// 	return config;
// });

createApp(App).use(store).use(router).mount('#app')
