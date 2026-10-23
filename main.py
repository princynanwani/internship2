import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

# Read the dataset
data = pd.read_csv("data/Mall_Customers.csv")

# Show first 5 rows
print("First 5 rows of the dataset:\n")
print(data.head())

# Show all column names
print("\nColumn Names:\n")
print(data.columns)

# Select the two columns we need
X = data[["Annual Income (k$)", "Spending Score (1-100)"]]

# -------------------------
# Elbow Method
# -------------------------

wcss = []

for i in range(1, 11):

    kmeans = KMeans(n_clusters=i, random_state=42, n_init=10)

    kmeans.fit(X)

    wcss.append(kmeans.inertia_)

# Draw the elbow graph

plt.figure(figsize=(6,5))

plt.plot(range(1,11), wcss, marker="o")

plt.title("Elbow Method")

plt.xlabel("Number of Clusters")

plt.ylabel("WCSS")

plt.grid(True)

plt.savefig("images/elbow_method.png")

plt.show()

# -------------------------
# K-Means Clustering
# -------------------------

kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)

data["Cluster"] = kmeans.fit_predict(X)

print("\nCluster added successfully!")

print(data.head())

# -------------------------
# Customer Segmentation Graph
# -------------------------

plt.figure(figsize=(8,6))

plt.scatter(
    data["Annual Income (k$)"],
    data["Spending Score (1-100)"],
    c=data["Cluster"]
)

plt.title("Customer Segmentation using K-Means")

plt.xlabel("Annual Income (k$)")

plt.ylabel("Spending Score (1-100)")

plt.grid(True)

plt.savefig("images/customer_segmentation.png")

plt.show()