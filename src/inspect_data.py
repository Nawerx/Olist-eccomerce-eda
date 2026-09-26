"""Display basic observations about raw CSV files without changing them."""

import argparse

import pandas as pd

from config import RAW_DIR


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "filenames",
        nargs="*",
        help="CSV filenames in data/raw. Leave empty to inspect all CSV files.",
    )
    args = parser.parse_args()

    if args.filenames:
        csv_paths = [RAW_DIR / filename for filename in args.filenames]
    else:
        csv_paths = sorted(RAW_DIR.glob("*.csv"))

    if not csv_paths:
        raise SystemExit(f"No CSV files found in {RAW_DIR}")

    for path in csv_paths:
        if not path.is_file():
            raise SystemExit(f"CSV file not found: {path}")

    for path in csv_paths:
        # ============================================================
        # 1. Load one raw file
        # ============================================================
        print(f"\nFile: {path.name}")
        df_raw = pd.read_csv(path)

        # ============================================================
        # 2. Shape, sample rows, columns and inferred data types
        # ============================================================
        print(f"Rows: {df_raw.shape[0]}, columns: {df_raw.shape[1]}")
        print("\nFirst rows:")
        print(df_raw.head().to_string())
        print("\nColumn names:")
        print(df_raw.columns.tolist())
        print("\nInferred data types and non-null counts:")
        df_raw.info()

        # ============================================================
        # 3. Missing values, unique values and exact duplicate rows
        # ============================================================
        print("\nMissing values by column:")
        print(df_raw.isna().sum().sort_values(ascending=False))
        print("\nUnique value counts excluding missing values:")
        print(df_raw.nunique(dropna=True))
        print(f"\nExact duplicate rows: {df_raw.duplicated().sum()}")

        del df_raw
