import pandas as pd

EXPECTED_COLUMNS = ["AT", "V", "AP", "RH", "PE"]

def load_csv(path: str) -> pd.DataFrame:
    """Load the CCPP dataset and validate structure."""
    df = pd.read_csv(path)

    # Log row count
    print(f"[data_loader] Loaded {len(df):,} rows from {path}")

    # Validate columns
    missing = set(EXPECTED_COLUMNS) - set(df.columns)
    if missing:
        raise ValueError(f"[data_loader] Missing expected columns: {missing}")

    # Validate nulls (idiomatic)
    if df.isnull().any().any():
        raise ValueError("[data_loader] Dataset contains null values.")

    # Validate numeric dtypes
    bad_types = [col for col in EXPECTED_COLUMNS
                 if not pd.api.types.is_numeric_dtype(df[col])]
    if bad_types:
        raise TypeError(f"[data_loader] Non-numeric columns found: {bad_types}")

    return df
