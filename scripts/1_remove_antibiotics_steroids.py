import pandas as pd  
  
# Load the metadata file  
df = pd.read_excel('raw_data/metadata.xlsx', engine='calamine')  
  
# Remove rows where 'steroids' or 'antibiotic' are 'Yes' or missing  
filtered_df = df[  
    (df['steroids'] != 'Yes') & (df['steroids'].notna()) &   
    (df['antibiotic'] != 'Yes') & (df['antibiotic'].notna())  
]  
  
# Save the filtered data to a new file  
filtered_df.to_excel('data_cleaning/metadata_filtered.xlsx', index=False)  
print("Filtered file saved as data_cleaning/metadata_filtered.xlsx")