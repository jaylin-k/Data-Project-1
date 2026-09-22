"""Clean two CSV files, handle missing values, and merge them."""

from pathlib import Path

import pandas as pd


def clean_data(path: str | Path) -> pd.DataFrame:
	
	data = pd.read_csv(path)
	data.columns = data.columns.str.strip().str.lower().str.replace(" ", "_", regex=False)
	data = data.drop_duplicates()

	for column in data.select_dtypes(include="number"):
		data[column] = data[column].fillna(data[column].median())
	for column in data.select_dtypes(exclude="number"):
		if data[column].isna().any():
			data[column] = data[column].fillna(data[column].mode().iloc[0] if not data[column].mode().empty else "Unknown")

	return data


def main() -> None:
	first_file = Path("revenue_raw.csv")
	second_file = Path("traffic_raw.csv")
	output_file = Path("cleaned_merged_data.csv")

	first = clean_data(first_file)
	second = clean_data(second_file)

	
	merge_columns = list(first.columns.intersection(second.columns))
	if not merge_columns:
		raise ValueError("The files must have at least one column in common.")

	merged = pd.merge(first, second, on=merge_columns, how="outer")
	merged.to_csv(output_file, index=False)
	print(f"Saved {len(merged)} rows to {output_file}")


if __name__ == "__main__":
	main()
