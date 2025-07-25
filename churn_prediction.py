import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import os

def load_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ Dataset not found at: {file_path}")
    return pd.read_csv(file_path)

def preprocess_data(df):
    df.drop("customerID", axis=1, inplace=True)
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors='coerce')
    df.dropna(inplace=True)
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})
    X = df.drop("Churn", axis=1)
    y = df["Churn"]
    X = pd.get_dummies(X, drop_first=True)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, y, scaler

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("✅ Model Evaluation:")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

    return model, scaler

def save_model(model, scaler):
    joblib.dump(model, "churn_model.pkl")
    joblib.dump(scaler, "scaler.pkl")
    print("✅ Model and Scaler saved to disk.")

def main():
    print("📂 Current working directory:", os.getcwd())
    print("📁 Files in 'Data':", os.listdir("Data"))

    print("📦 Loading Data...")
    df = load_data("Data/WA_Fn-UseC_-Telco-Customer-Churn.csv")
    
    print("🧼 Preprocessing...")
    X, y, scaler = preprocess_data(df)
    
    print("🧠 Training Model...")
    model, _ = train_model(X, y)
    
    print("💾 Saving Model...")
    save_model(model, scaler)

if __name__ == "__main__":
    main()
