import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const submitJournal = (text) =>
  API.post("/journal", { text });

export const fetchWeeklyAnalysis = () =>
  API.get("/weekly-analysis");
