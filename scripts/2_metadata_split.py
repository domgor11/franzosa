import os
import pandas as pd

def split_and_save_metadata(file_path, output_folder):
    # Create output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Load the data
    df = pd.read_excel(file_path, engine='calamine')
    
    # Filter for CD and UC groups
    df_cd = df[df['Study.Group'] == 'CD']
    df_uc = df[df['Study.Group'] == 'UC']
    
    # Define output file paths
    cd_file = os.path.join(output_folder, 'CD_metadata.xlsx')
    uc_file = os.path.join(output_folder, 'UC_metadata.xlsx')
    
    # Save to separate excel files
    df_cd.to_excel(cd_file, index=False)
    df_uc.to_excel(uc_file, index=False)
    
    print('Files saved:', cd_file, 'and', uc_file)

# Call the function with the specified folder
split_and_save_metadata('data_cleaning/metadata_filtered.xlsx', 'data_cleaning')