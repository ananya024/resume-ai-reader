// api.js

import axios from "axios";

const api= axios.create({
    baseURL:"http://127.0.0.1:8000"
})
export default api;

export const analyseResume = async(file)=> {
    const formData = new FormData();
    formData.append("file", file);
    const response =await api.post("/analyze", formData);
    return response.data;
}