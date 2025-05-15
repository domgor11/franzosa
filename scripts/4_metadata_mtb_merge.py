import pandas as pd
import os

# Create directory structure if it doesn't exist
output_dir = 'data_cleaning'
os.makedirs(output_dir, exist_ok=True)

output_file = os.path.join(output_dir, 'UC_metadata_mtb_merged.xlsx')

# Load and merge files
metadata_df = pd.read_excel('data_cleaning/UC_metadata.xlsx', engine='calamine')
mtb_df = pd.read_excel('data_cleaning/mtb_cleanup_1.xlsx', engine='calamine')
merged_df = pd.merge(metadata_df, mtb_df, on='Sample', how='left')

# Save merged file
merged_df.to_excel(output_file, index=False)
print(f'Successfully created {output_file}')
print('Number of rows in UC_metadata:', len(metadata_df))
print('Number of rows in mtb:', len(mtb_df))
print('Number of rows in merged file:', len(merged_df))


# Number of rows in CD_metadata: 60
# Number of rows in mtb: 220
# Number of rows in merged file: 60

# Number of rows in UC_metadata: 53
# Number of rows in mtb: 220
# Number of rows in merged file: 53