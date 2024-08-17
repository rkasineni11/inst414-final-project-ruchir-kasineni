import os
import pandas as pd

def extract_wr_data(wr_data_file_paths):
    columns_to_keep = ['Player', 'Pos', 'G', 'Tgt', 'Rec', 'Yds', 'TD']
    output_directory = 'data/extracted'

    os.makedirs(output_directory, exist_ok=True)

    for file_path in wr_data_file_paths:
        year = os.path.basename(file_path).split('_')[0]
        df = pd.read_csv(file_path)
    
        df = df[columns_to_keep]
        df['Player'] = df['Player'].str.lower().str.replace(r'[^a-z]', '', regex=True)
    
        output_file_name = f'Extracted_Wide_Receiver_Data_{year}.csv'
        output_file_path = os.path.join(output_directory, output_file_name)
    
        df.to_csv(output_file_path, index=False)
    
    
def extract_contract_data(contract_data_file_path):
    df = pd.read_csv(contract_data_file_path)
    df['Player'] = df['Player'].str.lower().str.replace(r'[^a-z]', '', regex=True)

    df_selected = df[['Player', 'APY']].copy()
    df_selected['Player'] = df_selected['Player'].str.lower().str.replace(' ', '').str.replace('.', '').str.replace('-', '')
    df_selected['APY'] = df_selected['APY']
    df_selected.columns = ['Player', 'APY']

    df_selected.to_csv('data/extracted/Extracted_Player_Contracts.csv', index=False)