import { useState } from "react";

export default function Journal({ setActive, setJournalText }) {
  const [text, setText] = useState("");

  function handleNext() {
    if (!text.trim()) return;

    setJournalText(text);
    setActive("Check-in");
  }

  return (
    <div className="container">
      <div className="card" style={{ maxWidth: "700px", margin: "0 auto" }}>
        <h2>Journal Entry</h2>
        <p>Write freely about how you're feeling.</p>

        <textarea
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="I am feeling overwhelmed but trying to stay positive..."
          style={textareaStyle}
        />

        <div style={footer}>
          <span>{text.length} characters</span>
          <button style={button} onClick={handleNext}>
            Next
          </button>
        </div>
      </div>
    </div>
  );
}

/* ---------- styles ---------- */

const textareaStyle = {
  width: "100%",
  minHeight: "180px",
  marginTop: "20px",
  padding: "20px",
  borderRadius: "16px",
  border: "1px solid #e5e7eb",
  background: "#fbfaf7",
  fontSize: "16px",
};

const footer = {
  marginTop: "20px",
  display: "flex",
  justifyContent: "space-between",
  alignItems: "center",
};

const button = {
  padding: "10px 24px",
  borderRadius: "24px",
  border: "none",
  background: "#4f8f6f",
  color: "#fff",
  cursor: "pointer",
};
