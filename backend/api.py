from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from quote_engine import generate_quote
from emotion_trends import get_emotion_df
import numpy as np
import math

from weekly_analysis import (
    get_weekly_data,
    weekly_emotion_distribution,
    weekly_wellness_metrics,
    detect_weekly_trend,
    generate_weekly_insights
)

from app_flow import run_app_flow

def clean_nan(obj):
    if isinstance(obj, dict):
        return {k: clean_nan(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [clean_nan(i) for i in obj]
    elif isinstance(obj, float) and math.isnan(obj):
        return 0
    else:
        return obj
    
app = FastAPI()

# ✅ ADD CORS MIDDLEWARE
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalyzeRequest(BaseModel):
    text: str
    questionnaire_answers: list[int]


@app.post("/analyze")
def analyze_journal(req: AnalyzeRequest):
    return run_app_flow(req.text, req.questionnaire_answers)


@app.get("/weekly-summary")
def weekly_summary():
    df_week = get_weekly_data()

    if df_week is None or len(df_week) == 0:
        return {"message": "Not enough data for weekly analysis."}

    emotion_dist = weekly_emotion_distribution(df_week)
    avg_score, avg_esi, avg_stress = weekly_wellness_metrics(df_week)
    score_trend, stress_trend = detect_weekly_trend(df_week)

    insights = generate_weekly_insights(
        emotion_dist,
        avg_score,
        avg_esi,
        stress_trend,
        score_trend
    )

    response = {
    "emotion_distribution": emotion_dist,
    "average_score": avg_score,
    "average_esi": avg_esi,
    "average_stress": avg_stress,
    "score_trend": score_trend,
    "stress_trend": stress_trend,
    "insights": insights,
    "dates": df_week["date"].astype(str).tolist(),
    "wellness_scores": df_week["wellness_score"].tolist(),
    "stress_levels": df_week["stress_level"].tolist()
    }   

    return clean_nan(response)

@app.get("/quote")
def get_quote():
    df = get_emotion_df()

    if df is None or len(df) == 0:
        return {"quote": generate_quote({})}

    # Use latest emotion distribution
    latest = df.iloc[-1]["emotion_distribution"]

    return {
        "quote": generate_quote(latest)
    }
