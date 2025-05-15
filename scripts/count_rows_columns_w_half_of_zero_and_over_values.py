import pandas as pd  
  
def count_patients_with_sparse_clusters(file_path):  
    # Load the filtered dataset  
    df = pd.read_excel(file_path, engine='calamine')  
      
    # Get columns that contain 'Cluster'  
    cluster_cols = [col for col in df.columns if 'Cluster' in col]  
      
    # For each row (patient), count number of zero entries in cluster columns  
    # and check if they are 50% or more of the total cluster columns  
    sparse_count = (df[cluster_cols].apply(lambda row: (row == 0).sum(), axis=1)  
                      >= (0.1 * len(cluster_cols))).sum()  
      
    return sparse_count  
  
# Testing the function on the filtered file  
result = count_patients_with_sparse_clusters('data_cleaning/CD_metadata_mtb_merged.xlsx')  
print("Number of patients with 50% or more zeros in cluster columns:", result)  

  
def count_sparse_cluster_columns(file_path):  
    # Load dataset  
    df = pd.read_excel(file_path, engine='calamine')  
      
    # Identify columns with 'Cluster' in the header  
    cluster_cols = [col for col in df.columns if 'Cluster' in col]  
      
    # Calculate the count of columns that have 50% or more zeros in their cells  
    sparse_columns_count = sum([(df[col] == 0).sum() >= 0.5 * len(df[col]) for col in cluster_cols])  
      
    return sparse_columns_count  
  
# Test the function on the current dataset  
result = count_sparse_cluster_columns('data_cleaning/CD_metadata_mtb_merged.xlsx')  
print("Number of cluster columns with 50% or more zeros:", result)  