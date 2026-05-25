import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, f1_score

print("Environment setup successful!")

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

df['target'] = iris.target

df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

print(df.head())
df.info()
print(df.isnull().sum())

x = df.drop(columns=['target', 'species'])
y = df['target']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=42)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(x_train_scaled, y_train)

print("Model training complete!")

y_pred = knn.predict(x_test_scaled)
f1 = f1_score(y_test, y_pred, average='macro')
cm = confusion_matrix(y_test, y_pred)

print("\n--- Model Evaluation Results ---")
print(f"F1-Score: {f1:.4f}")
print("\nConfusion Matrix:")
print(cm)




