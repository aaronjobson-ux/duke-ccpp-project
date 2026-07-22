import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

def evaluate(model, X_test, y_test):
    preds = model.predict(X_test)

    mae = mean_absolute_error(y_test, preds)
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    r2 = r2_score(y_test, preds)

    return {"MAE": mae, "RMSE": rmse, "R2": r2}

def plot_predictions(model, X_test, y_test):
    preds = model.predict(X_test)

    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, preds, alpha=0.6)
    plt.xlabel("Actual PE")
    plt.ylabel("Predicted PE")
    plt.title("Actual vs Predicted Power Output")
    plt.grid(True)
    plt.show()
