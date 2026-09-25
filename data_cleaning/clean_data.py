import pandas as pd



def clean_data(first_file, second_file):

    data1 = pd.read_excel(first_file)
    data2 = pd.read_excel(second_file)
    merged_data = pd.merge(data1, data2, on=['user_id', 'date'], how='left')
    merged_data.columns = merged_data.columns.str.strip().str.lower().str.replace(" ", "_", regex=False)
    merged_data = merged_data.drop_duplicates()
    merged_data['keyword_searched'] = merged_data['keyword_searched'].fillna("No Keyword (Social/Email/Direct)")

    merged_data['revenue_amount'] = merged_data['revenue_amount'].fillna(0)
    merged_data['order_id'] = merged_data['order_id'].fillna('No Order')
    merged_data['product_category'] = merged_data['product_category'].fillna('None')

    merged_data.to_csv('cleaned_marketing_master3.csv', index=False)
    print("Pipeline complete. 'cleaned_marketing_master3.csv' is ready to use for SQL.")

if __name__ == "__main__":
    clean_data('traffic_raw.xlsx', 'revenue_raw.xlsx')

# import pandas as pd
# import numpy as np

# # 1. Load the raw Excel files
# traffic_df = pd.read_excel('traffic_raw.xlsx')
# revenue_df = pd.read_excel('revenue_raw.xlsx')


# traffic_df['keyword_searched'] = traffic_df['keyword_searched'].fillna('No Keyword (Social/Email/Direct)')


# merged_df = pd.merge(
#     traffic_df, 
#     revenue_df, 
#     on=['user_id', 'date'], 
#     how='left'
# )


# merged_df['revenue_amount'] = merged_df['revenue_amount'].fillna(0)
# merged_df['order_id'] = merged_df['order_id'].fillna('No Order')
# merged_df['product_category'] = merged_df['product_category'].fillna('None')


# merged_df.to_csv('clean_marketing_master.csv', index=False)
# print("Pipeline complete! 'clean_marketing_master.csv' is ready for SQL ingestion.")