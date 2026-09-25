import pandas as pd


def clean_data(first_file, second_file):
    traffic = pd.read_excel(first_file)
    revenue = pd.read_excel(second_file)
    merged_data = pd.merge(traffic, revenue, on=['user_id', 'date'], how='left')
    merged_data.columns = merged_data.columns.str.strip().str.lower().str.replace(" ", "_", regex=False)
    merged_data = merged_data.drop_duplicates()
    merged_data['keyword_searched'] = merged_data['keyword_searched'].fillna("No Keyword (Social/Email/Direct)")

    merged_data['revenue_amount'] = merged_data['revenue_amount'].fillna(0)
    merged_data['order_id'] = merged_data['order_id'].fillna('No Order')
    merged_data['product_category'] = merged_data['product_category'].fillna('None')

    merged_data.to_csv('cleaned_marketing_master.csv', index=False)
    print("Pipeline complete. 'cleaned_marketing_master.csv' is ready to use for SQL.")

    return merged_data