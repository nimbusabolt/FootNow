// axios.js

import { getCurrentInstance } from 'vue';
import axios from 'axios';

const instance = getCurrentInstance();

// Ensure that getCurrentInstance() returns a valid instance before accessing its properties
const axiosInstance = instance ? instance.appContext.config.globalProperties.$http : axios;

// Set up interceptors or other configurations as needed
axiosInstance.interceptors.request.use(config => {
    const token = localStorage.getItem('token');
    
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
});

export default axiosInstance;
