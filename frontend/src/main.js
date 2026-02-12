import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'
import axios from 'axios'

const app = createApp(App)

app.use(router)

// Configure axios global defaults if needed
axios.defaults.baseURL = import.meta.env.VITE_API_URL || '';

app.mount('#app')
