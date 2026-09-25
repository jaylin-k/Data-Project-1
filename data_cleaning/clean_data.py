# import pandas as pd



# traffic = pd.read_excel('revenue_raw.xlsx')
# revenue = pd.read_excel('traffic_raw.xlsx')
# merged_data = pd.merge(traffic, revenue, on=['user_id', 'date'], how='left')
# merged_data.columns = merged_data.columns.str.strip().str.lower().str.replace(" ", "_", regex=False)
# merged_data = merged_data.drop_duplicates()
# merged_data['keyword_searched'] = merged_data['keyword_searched'].fillna("No Keyword (Social/Email/Direct)")

# merged_data['revenue_amount'] = merged_data['revenue_amount'].fillna(0)
# merged_data['order_id'] = merged_data['order_id'].fillna('No Order')
# merged_data['product_category'] = merged_data['product_category'].fillna('None')

# merged_data.to_csv('cleaned_marketing_master.csv', index=False)
# print("Pipeline complete. 'cleaned_marketing_master.csv' is ready to use for SQL.")

import pandas as pd
import numpy as np

# 1. Load the raw Excel files
traffic_df = pd.read_excel('traffic_raw.xlsx')
revenue_df = pd.read_excel('revenue_raw.xlsx')


traffic_df['keyword_searched'] = traffic_df['keyword_searched'].fillna('No Keyword (Social/Email/Direct)')


merged_df = pd.merge(
    traffic_df, 
    revenue_df, 
    on=['user_id', 'date'], 
    how='left'
)


merged_df['revenue_amount'] = merged_df['revenue_amount'].fillna(0)
merged_df['order_id'] = merged_df['order_id'].fillna('No Order')
merged_df['product_category'] = merged_df['product_category'].fillna('None')


merged_df.to_csv('clean_marketing_master.csv', index=False)
print("Pipeline complete! 'clean_marketing_master.csv' is ready for SQL ingestion.")