import pandas as pd
import numpy as np

# Load the data
df = pd.read_excel('raw_data/mtb.xlsx', engine='calamine')

# Get cluster columns
cluster_cols = [col for col in df.columns if 'Cluster' in col]

# Calculate percentage of zeros in each cluster column
zero_percentages = {}
cols_to_drop = []

for col in cluster_cols:
    zero_count = (df[col] == 0).sum()
    total_count = len(df[col])
    zero_percentage = (zero_count / total_count) * 100
    
    if zero_percentage >= 10:
        cols_to_drop.append(col)

# Remove columns with >= 10% zeros
df_filtered = df.drop(columns=cols_to_drop)

# Save filtered dataframe
df_filtered.to_excel('data_cleaning/mtb_cleanup_1.xlsx', index=False)

print('Original number of cluster columns:', len(cluster_cols))
print('Number of columns removed:', len(cols_to_drop))
print('Number of columns remaining:', len([col for col in df_filtered.columns if 'Cluster' in col]))
print('Saved filtered data to data_cleaning/mtb_cleanup_1.xlsx')

# Original number of cluster columns: 8848
# Number of columns removed: 6229
# Number of columns remaining: 2619