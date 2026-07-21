import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def build_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["AT_AP_diff"] = df["AT"] - df["AP"]
    return df

def preprocess(df: pd.DataFrame):
    df = build_features(df)

    X = df.drop(columns=["PE"])
    y = df["PE"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test, scaler
