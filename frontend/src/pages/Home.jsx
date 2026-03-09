import { useState, useEffect } from "react";
export default function Home() {
  const [quote, setQuote] = useState("");

  async function fetchQuote() {
    try {
      const response = await fetch("http://127.0.0.1:8000/quote");
      const data = await response.json();
      setQuote(data.quote);
    } catch {
      setQuote("Every day is a new beginning.");
    }
  }

  useEffect(() => {
    fetchQuote();
  }, []);

  return (
    <div className="container">
      <h1>How are you feeling today?</h1>
      <p>
        Track your emotions, understand your patterns, and nurture your mental wellness.
      </p>

      {/* Quote Card */}
      <div style={quoteCard}>
        <div style={{ marginBottom: "8px", color: "#4f8f6f" }}>
          ✨ Daily inspiration
        </div>

        <h3>"{quote}"</h3>

        <button onClick={fetchQuote} style={linkBtn}>
          🔄 New quote
        </button>
      </div>

      {/* Feature Cards */}
      <div style={featureGrid}>
        <Feature title="Journal" desc="Express your thoughts freely" />
        <Feature title="Quick Check-in" desc="Track how you feel right now" />
        <Feature title="Dashboard" desc="View emotional patterns" />
      </div>
    </div>
  );
}

function Feature({ title, desc }) {
  return (
    <div className="card">
      <h3>{title}</h3>
      <p>{desc}</p>
      {/* <span style={{ color: "#4f8f6f" }}>Get started →</span> */}
    </div>
  );
}

// const quoteStyle = {
//   marginTop: "40px",
//   padding: "32px",
//   borderRadius: "20px",
//   background: "linear-gradient(135deg, #eaf3ee, #f3f4ff)"
// };

// const quoteText = {
//   fontSize: "24px",
//   margin: "16px 0"
// };

const featureGrid = {
  marginTop: "40px",
  display: "grid",
  gridTemplateColumns: "repeat(3, 1fr)",
  gap: "24px"
};

const quoteCard = {
  background: "linear-gradient(to right, #eaf3ee, #f4f1fb)",
  padding: "32px",
  borderRadius: "20px",
  marginTop: "32px"
};

const linkBtn = {
  marginTop: "16px",
  border: "none",
  background: "transparent",
  color: "#4f8f6f",
  cursor: "pointer"
};
