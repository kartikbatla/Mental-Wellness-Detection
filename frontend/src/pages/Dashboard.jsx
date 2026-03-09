import { useEffect, useState } from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer,
  BarChart,
  Bar
} from "recharts";

export default function Dashboard() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch("https://mental-wellness-detection-2.onrender.com/weekly-summary")
      .then(res => res.json())
      .then(data => setData(data));
  }, []);

  if (!data) return <p style={{ textAlign: "center" }}>Loading weekly insights...</p>;

  if (data.message) return <p>{data.message}</p>;

  const scoreData = data.dates.map((date, i) => ({
    date,
    score: data.wellness_scores[i]
  }));

  const stressData = data.dates.map((date, i) => ({
    date,
    stress: data.stress_levels[i]
  }));

  const emotionData = Object.entries(data.emotion_distribution).map(([key, value]) => ({
    emotion: key,
    value: Math.round(value * 100)
  }));

  return (
    <div className="container">
      <h2 style={{ textAlign: "center" }}>Weekly Mental Wellness Dashboard</h2>

      {/* Wellness Score Trend */}
      <div className="card">
        <h3>Wellness Score Trend</h3>
        <ResponsiveContainer width="100%" height={300}>
          <LineChart data={scoreData}>
            <CartesianGrid stroke="#ccc" />
            <XAxis dataKey="date" />
            <YAxis domain={[0, 100]} />
            <Tooltip />
            <Line type="monotone" dataKey="score" stroke="#4f8f6f" strokeWidth={3} />
          </LineChart>
        </ResponsiveContainer>
      </div>

      {/* Stress Trend */}
      <div className="card">
        <h3>Stress Level Trend</h3>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={stressData}>
            <CartesianGrid stroke="#ccc" />
            <XAxis dataKey="date" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="stress" fill="#e57373" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* Emotion Distribution */}
      <div className="card">
        <h3>Weekly Emotion Distribution</h3>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={emotionData}>
            <CartesianGrid stroke="#ccc" />
            <XAxis dataKey="emotion" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="value" fill="#6c8ef5" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* Insights */}
      <div className="card">
        <h3>Weekly Insights</h3>
        <ul>
          {data.insights.map((i, index) => (
            <li key={index}>{i}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}
