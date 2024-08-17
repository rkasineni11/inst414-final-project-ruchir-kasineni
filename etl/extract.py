import os
import pandas as pd

def extract_wr_data(wr_data_file_paths):
    """
    Extracts wide receiver data from multiple CSV files, cleans the player names, and saves the processed data.

    Args:
        wr_data_file_paths (list of str): List of file paths to the wide receiver data CSV files.
    
    Returns:
        None: The processed data is saved as new CSV files in the 'data/extracted' directory.
    """
    # Columns to keep from the original data
    columns_to_keep = ['Player', 'Pos', 'G', 'Tgt', 'Rec', 'Yds', 'TD']
    
    # Define the output directory for the extracted files
    output_directory = 'data/extracted'
    
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)
    
    # Process each file in the list
    for file_path in wr_data_file_paths:
        # Extract the year from the file name
        year = os.path.basename(file_path).split('_')[0]
        
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        
        # Select only the necessary columns
        df = df[columns_to_keep]
        
        # Clean the 'Player' column: convert to lowercase and remove non-alphabetic characters
        df['Player'] = df['Player'].str.lower().str.replace(r'[^a-z]', '', regex=True)
        
        # Define the output file name and path
        output_file_name = f'Extracted_Wide_Receiver_Data_{year}.csv'
        output_file_path = os.path.join(output_directory, output_file_name)
        
        # Save the processed DataFrame to a CSV file
        df.to_csv(output_file_path, index=False)

def extract_contract_data(contract_data_file_path):
    """
    Extracts and cleans player contract data from a CSV file, then saves the cleaned data.

    Args:
        contract_data_file_path (str): File path to the player contract data CSV file.
    
    Returns:
        None: The processed data is saved as a new CSV file in the 'data/extracted' directory.
    """
    # Read the CSV file into a DataFrame
    df = pd.read_csv(contract_data_file_path)
    
    # Clean the 'Player' column: convert to lowercase and remove non-alphabetic characters
    df['Player'] = df['Player'].str.lower().str.replace(r'[^a-z]', '', regex=True)
    
    # Select relevant columns and clean the 'Player' names further by removing spaces, periods, and hyphens
    df_selected = df[['Player', 'APY']].copy()
    df_selected['Player'] = df_selected['Player'].str.lower().str.replace(' ', '').str.replace('.', '').str.replace('-', '')
    
    # Rename columns to ensure consistency
    df_selected.columns = ['Player', 'APY']
    
    # Save the processed DataFrame to a CSV file
    df_selected.to_csv('data/extracted/Extracted_Player_Contracts.csv', index=False)
