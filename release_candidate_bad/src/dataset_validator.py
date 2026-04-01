from __future__ import annotations
#
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

DATASET_PATH = Path("data/processed/cleaned_customers.csv")
EXPECTED_ROWS = 5
EXPECTED_COLUMNS = 4


@dataclass(frozen=True)
class ValidationReport:
    rows: int
    columns: int
    missing_values: int
    duplicate_rows: int


def load_cleaned_dataset(dataset_path: Path = DATASET_PATH) -> pd.DataFrame:
    return pd.read_csv(dataset_path)


def build_validation_report(df: pd.DataFrame) -> ValidationReport:
    return ValidationReport(
        rows=len(df),
        columns=len(df.columns),
        missing_values=int(df.isna().sum().sum()),
        duplicate_rows=int(df.duplicated().sum()),
    )


def validate_cleaned_dataset(df: pd.DataFrame) -> ValidationReport:
    report = build_validation_report(df)
    assert report.rows == EXPECTED_ROWS, f"Expected {EXPECTED_ROWS} rows, got {report.rows}"
    assert report.columns == EXPECTED_COLUMNS, (
        f"Expected {EXPECTED_COLUMNS} columns, got {report.columns}"
    )
    assert report.missing_values == 0, f"Found {report.missing_values} missing values"
    assert report.duplicate_rows == 0, f"Found {report.duplicate_rows} duplicate rows"
    return report


def main() -> None:
    df = load_cleaned_dataset()
    report = validate_cleaned_dataset(df)
    print(report)


if __name__ == "__main__":
    main()
