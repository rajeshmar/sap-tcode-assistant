import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
  timeout: 30000,
});

export async function searchTcodes({ query, module, topK = 5 }) {
  const response = await api.post("/search", {
    query,
    module: module || null,
    top_k: topK,
  });

  return response.data;
}

export async function getModules() {
  const response = await api.get("/modules");
  return response.data;
}