#Script for identifying campaign trends

import pandas as pd
import matplotlib.pyplot as plt

def analyze_trends(data_path):
    df = pd.read_csv(data_path)
    df['CTR'] = df['Clicks'] / df['Impressions']
    df['Date'] = pd.to_datetime(df['Date'])
    trend = df.groupby(df['Date'].dt.to_period('M')).mean()

    plt.plot(trend.index.astype(str), trend['CTR'], marker='o', label='CTR Trend')
    plt.xlabel('Month')
    plt.ylabel('Click-Through Rate')
    plt.title('CTR Trend Analysis')
    plt.legend()
    plt.savefig('reports/ctr_trend.png')
    print(f"CTR trend analysis saved to reports/ctr_trend.png")

if __name__ == "__main__":
    analyze_trends("data/preprocessed_data.csv")