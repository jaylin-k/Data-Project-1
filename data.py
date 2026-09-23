from pathlib import Path

import pandas as pd
import numpy as np


def clean_data(first_file, second_file):
    traffic = pd.read_excel(first_file)
    revenue = pd.read_excel(second_file)
    merged_data = pd.merge(traffic, revenue, on=['user_id', 'date'], how='left')
    merged_data.columns = merged_data.columns.str.strip().lower().str.replace(" ", "_", regex = False)
    merged_data = merged_data.drop_duplicates()
    merged_data['keyword_searched'] = merged_data['keyword_searched'].fillna("No Keyword (Social/Email/Direct)")

    merged_data['revenue_amount'] = merged_data['revenue_amount'].fillna(0)
    merged_data['order_id'] = merged_data['order_id'].fillna('No Order')
    merged_data['product_category'] = merged_data['product_category'].fillna('None')

    merged_data.to_csv('cleaned_marketing_master.csv', index=False)
    print("Pipline complete. 'clean_marketing_master.csv' is ready to use for SQL.")

    return merged_data

def main():
      clean_data('revenue_raw.xlsx', 'traffic_raw.xlsx')


if __name__ == "__main__":
	main()

# def clean_data(path: str | Path) -> pd.DataFrame:
	
# 	data = pd.read_csv(path)
# 	data.columns = data.columns.str.strip().str.lower().str.replace(" ", "_", regex=False)
# 	data = data.drop_duplicates()

# 	for column in data.select_dtypes(include="number"):
# 		data[column] = data[column].fillna(data[column].median())
# 	for column in data.select_dtypes(exclude="number"):
# 		if data[column].isna().any():
# 			data[column] = data[column].fillna(data[column].mode().iloc[0] if not data[column].mode().empty else "Unknown")

# 	return data


# def main() -> None:
# 	first_file = Path("revenue_raw.csv")
# 	second_file = Path("traffic_raw.csv")
# 	output_file = Path("cleaned_merged_data.csv")

# 	first = clean_data(first_file)
# 	second = clean_data(second_file)

	
# 	merge_columns = list(first.columns.intersection(second.columns))
# 	if not merge_columns:
# 		raise ValueError("The files must have at least one column in common.")

# 	merged = pd.merge(first, second, on=merge_columns, how="outer")
# 	merged.to_csv(output_file, index=False)
# 	print(f"Saved {len(merged)} rows to {output_file}")


# if __name__ == "__main__":
# 	main()
