#Script for audience segmentation

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns

def load_data(data_path):
    #Load the preprocessed data from a CSV file.
    data = pd.read_csv(data_path)
    data['CTR'] = data['Clicks'] / data['Impressions']
    return data

def preprocessed_data(data):
    #Select relevant columns and sclae date for clustering.
    features = data[['CTR', 'Impressions', 'Conversions']]
    scaler = StandardScaler()
    scaler_features = scaler.fit_transform(features)
    return scaler_features, features

def preform_segmentation(scaled_features, n_clusters=3):
    #Perform audience segmentation using KMeans Clustering.
    KMeans = KMeans(n_clusters=n_clusters, random_state=42)
    segments = KMeans.fit_predict(scaled_features)
    return segments, KMeans

def visualize_segments(data, segments):
    #Visualize the segmentation results.
    data['Segment'] = segments
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        x='CTR',
        y='Impressions',
        hue='Segment',
        data=data,
        palette='viridis',
        style='Segment',
        s=100
    )
    plt.title('Audience Segmentation')
    plt.xlabel('Click-Through Rate')
    plt.ylabel('Impressions')
    plt.legend(title='Segment')
    plt.savefig('reports/segmentation_visualization.png')
    print(f"Segmentation visualization saved to reports/segmentation_visualization.png")

def save_segmented_data(data, output_path):
    #Save the segmented data to a CSV file.
    data.to_csv(output_path, index=False)
    print(f"Segmented data saved to {output_path}")

if __name__ == "__main__":
    #Load and preprocess the data.
    data = load_data("data/preprocessed_data.csv")
    scaled_features, original_features = preprocessed_data(data)

    #Perform segmentation
    segments, KMeans = preform_segmentation(scaled_features, n_clusters=4)

    #Visualize and save the results
    visualize_segments(data, segments)
    save_segmented_data(data, "data/segmented_data.csv")