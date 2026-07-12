// api.js

import axios from "axios";

const api= axios.create({
    baseURL:"http://127.0.0.1:8000"
})
export default api;

export const analyseResume = async(file, filejd)=> {
    const formData = new FormData();
    formData.append("file", file);
    formData.append("filejd", filejd);
    const response = await api.post("/analyze", formData);
    return response.data;
}