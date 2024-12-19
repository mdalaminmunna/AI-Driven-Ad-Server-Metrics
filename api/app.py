#Flask-based API to expose metrics

from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/metrics', methods=['GET'])
def get_metrics():
    df = pd.read_csv("data/preprocessed_data.csv")
    avg_ctr = df['CTR'].mean()
    metrics = {
        "average_ctr": round(avg_ctr, 4),
        "total_clicks": int(df['Clicks'].sum()),
        "total_impressions": int(df['Impressions'].sum())
    }
    return jsonify(metrics)

@app.route('/anomalies', methods=['GET'])
def get_anomalies():
    anomalies = pd.read_csv("reports/anomalies.csv")
    return anomalies.to_json(orient="records")

if __name__ == "__main__":
    app.run(debug=True)