import { useState } from "react";

export default function CheckIn({ journalText, setActive }) {
  const questions = [
    "I feel mentally exhausted by the end of the day.",
    "I feel emotionally supported by people around me.",
    "I find it hard to control my emotions.",
    "I feel calm and relaxed most of the time.",
    "I feel anxious about my future.",
    "I am able to focus on tasks without feeling overwhelmed.",
    "I feel satisfied with my daily routine.",
    "I often feel stressed without knowing why."
  ];

  const [current, setCurrent] = useState(0);
  const [answers, setAnswers] = useState(
    Array(questions.length).fill(null)
  );
  const [report, setReport] = useState(null);
  const [loading, setLoading] = useState(false);

  function handleSelect(value) {
    const updated = [...answers];
    updated[current] = value;
    setAnswers(updated);
  }

  function handleNext() {
    if (answers[current] === null) return;
    if (current < questions.length - 1) {
      setCurrent(current + 1);
    }
  }

  function handleBack() {
    if (current > 0) {
      setCurrent(current - 1);
    } else {
      setActive("Journal");
    }
  }

  async function handleAnalyze() {
    if (answers.includes(null)) {
      alert("Please answer all questions.");
      return;
    }

    setLoading(true);

    try {
      const response = await fetch("https://mental-wellness-detection-2.onrender.com/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          text: journalText,
          questionnaire_answers: answers
        })
      });

      const data = await response.json();
      setReport(data);
    } catch (err) {
      alert("Analysis failed. Please try again.");
    } finally {
      setLoading(false);
    }
  }

  /* ---------- SHOW REPORT ---------- */

  if (report) {
    return (
      <div className="container">
        <div className="card" style={{ maxWidth: "700px", margin: "0 auto" }}>
          <h2>Mental Wellness Report</h2>

          <p><strong>Status:</strong> {report.status}</p>
          <p><strong>Final Wellness Score:</strong> {report.final_wellness_score}</p>
          <p><strong>Stress Detected:</strong> {report.stress_detected ? "Yes" : "No"}</p>

          <h4>Emotion Distribution</h4>
          {Object.entries(report.emotion_distribution).map(([emotion, value]) => (
            <p key={emotion}>
              {emotion}: {Math.round(value * 100)}%
            </p>
          ))}

          <h4>Personalized Recommendations</h4>
          <ul>
            {report.recommendations.map((r, i) => (
              <li key={i}>{r}</li>
            ))}
          </ul>

          <button
            style={button}
            onClick={() => setActive("Journal")}
          >
            Back to Journal
          </button>
        </div>
      </div>
    );
  }

  /* ---------- QUESTION FLOW ---------- */

  return (
    <div className="container">
      <div className="card" style={{ maxWidth: "700px", margin: "0 auto" }}>
        <h2>Emotional Check-in</h2>
        <p>Answer honestly — there are no right or wrong answers.</p>

        <div style={progressBar}>
          <div
            style={{
              ...progressFill,
              width: `${((current + 1) / questions.length) * 100}%`
            }}
          />
        </div>

        <h3>{questions[current]}</h3>

        <div style={scale}>
          {[1, 2, 3, 4, 5].map((n) => (
            <button
              key={n}
              style={{
                ...scaleBtn,
                background:
                  answers[current] === n ? "#4f8f6f" : "#fff",
                color:
                  answers[current] === n ? "#fff" : "#000"
              }}
              onClick={() => handleSelect(n)}
            >
              {n}
            </button>
          ))}
        </div>

        <div style={footer}>
          <button style={secondaryBtn} onClick={handleBack}>
            Back
          </button>

          {current < questions.length - 1 ? (
            <button style={button} onClick={handleNext}>
              Next
            </button>
          ) : (
            <button style={button} onClick={handleAnalyze}>
              {loading ? "Analyzing..." : "Analyze"}
            </button>
          )}
        </div>
      </div>
    </div>
  );
}

/* ---------- styles ---------- */

const progressBar = {
  height: "6px",
  background: "#e5e7eb",
  borderRadius: "6px",
  margin: "20px 0"
};

const progressFill = {
  height: "100%",
  background: "#4f8f6f",
  borderRadius: "6px"
};

const scale = {
  display: "flex",
  gap: "12px",
  margin: "20px 0"
};

const scaleBtn = {
  flex: 1,
  padding: "16px",
  borderRadius: "12px",
  border: "1px solid #e5e7eb",
  cursor: "pointer"
};

const footer = {
  display: "flex",
  justifyContent: "space-between",
  alignItems: "center",
  marginTop: "32px"
};

const button = {
  padding: "10px 24px",
  borderRadius: "24px",
  border: "none",
  background: "#4f8f6f",
  color: "#fff",
  cursor: "pointer"
};

const secondaryBtn = {
  ...button,
  background: "#e5e7eb",
  color: "#333"
};
