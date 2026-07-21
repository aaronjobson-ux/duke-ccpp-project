import joblib
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor
from pathlib import Path

MODEL_DIR = Path("models/")
MODEL_DIR.mkdir(exist_ok=True)

def get_model(model_name: str):
    if model_name == "linear":
        return LinearRegression()
    elif model_name == "ridge":
        return Ridge(alpha=1.0)
    elif model_name == "rf":
        return RandomForestRegressor(n_estimators=200, random_state=42)
    else:
        raise ValueError(f"Unknown model: {model_name}")

def train_model(model_name: str, X_train, y_train):
    model = get_model(model_name)
    model.fit(X_train, y_train)

    save_path = MODEL_DIR / f"{model_name}_model.pkl"
    joblib.dump(model, save_path)

    return model, save_path
