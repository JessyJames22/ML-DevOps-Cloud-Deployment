import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import joblib 

# Load dataset
data = pd.read_excel('data/Online Retail.xlsx')

# Preprocess data
data.dropna(inplace=True)  # Remove rows with missing values
data = data[data['Quantity'] > 0]  # Filter out rows with negative or zero quantity

# Create a new DataFrame with relevant features
# Here, we're using 'CustomerID', 'InvoiceDate', 'Quantity', and 'UnitPrice'
data['TotalPrice'] = data['Quantity'] * data['UnitPrice']
customer_data = data.groupby('CustomerID').agg({
    'TotalPrice': 'sum',
    'InvoiceDate': 'nunique',
    'Quantity': 'sum'
}).reset_index()

# Rename columns for clarity
customer_data.columns = ['CustomerID', 'TotalSpend', 'Frequency', 'Quantity']

# Use K-means clustering
X = customer_data[['TotalSpend', 'Frequency']]
kmeans = KMeans(n_clusters=5, random_state=42)  # You can change the number of clusters
customer_data['Cluster'] = kmeans.fit_predict(X)

# Visualize the clusters
plt.scatter(customer_data['TotalSpend'], customer_data['Frequency'], c=customer_data['Cluster'], cmap='viridis')
plt.xlabel('Total Spend')
plt.ylabel('Frequency of Purchases')
plt.title('Customer Segmentation')
plt.show()

# Save the model if needed (optional)
joblib.dump(kmeans, 'model/customer_segmentation_model.pkl')

print("Customer segmentation completed.")

