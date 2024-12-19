#Script for spotting anomalies in ad performance

import pandas
from sklearn.ensemble import IsolationForest

def detect_anomalies(data_path):
    df = pd.read_csv(data_path)
    model = IsolationForest(contamination=0.05)
    df['CTR'] = df['Clicks'] / df['Impressions']

    #Detect anomalies
    df['Anomaly'] = model.fit_predict(df[['CTR', 'Spend']])
    anomalies = df[df['Anomaly'] == -1]

    anomalies.to.csv('reports/anomalies.csv', index=False)
    print(f"Anomalies detected and saved to reports/anomalies.csv")

if __name__ == "__main__":
    detect_anomalies("data/preprocessed_data.csv")