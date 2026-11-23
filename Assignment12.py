
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("customer_churn.csv")
print("First 5 Rows:")
print(df.head())
print("\nDataset Information:")
print(df.info()
print("\nMissing Values:")
print(df.isnull().sum())
if "TotalCharges" in df.columns:
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
for col in df.select_dtypes(include=np.number).columns:
    df[col] = df[col].fillna(df[col].median())
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].fillna(df[col].mode()[0])
df = df.drop_duplicates()
print("\nSummary Statistics:")
print(df.describe())
print("\nCustomer Churn Count:")
print(df["Churn"].value_counts())
if "MlyCharges" in df.columns:
    print("\nAverage Monthly Charges:")
    print(df["MonthlyCharges"].mean())
sns.countplot(x="Churn", data=df)
plt.title("Customer Churn Distribution")
plt.show()
if "MonthlyCharges" in df.columns:
    sns.histplot(df["MonthlyCharges"], kde=True)
    plt.title("Monthly Charges Distribution")
    plt.show()
if "tenure" in df.columns:
    sns.boxplot(x="Churn", y="tenure", data=df)
    plt.title("Churn vs Customer Tenure")
    plt.show()
numeric_df = df.select_dtypes(include=np.number)

sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

print("\nEDA Completed Successfully!")
