import os
import pandas as pd

extracted_wr_data_file_paths = [
    'data/extracted/Extracted_Wide_Receiver_Data_2021.csv',
    'data/extracted/Extracted_Wide_Receiver_Data_2022.csv',
    'data/extracted/Extracted_Wide_Receiver_Data_2023.csv'
]

extracted_contract_data_file_path = 'data/extracted/Extracted_Player_Contracts.csv'

def transform_wr_data(input):
    player_data_df = pd.DataFrame()

    for file_path in input:
        # Extract the year from the file name
        year = os.path.basename(file_path).split('_')[-1].split('.')[0]
        
        # Read the data, filter by position, and select necessary columns
        df = pd.read_csv(file_path)
        df = df[df['Pos'].isin(['WR', 'TE'])]
        df = df[['Player', 'G', 'Tgt', 'Rec', 'Yds', 'TD']]
        
        # Concatenate data for all years
        player_data_df = pd.concat([player_data_df, df], ignore_index=True)

    # Aggregate data by player, summing up all columns
    aggregated_df = player_data_df.groupby('Player').agg({
        'G': 'sum',
        'Tgt': 'sum',
        'Rec': 'sum',
        'Yds': 'sum',
        'TD': 'sum'
    }).reset_index()

    # Calculate averages per game for 'Tgt', 'Rec', 'Yds', 'TD'
    for col in ['Tgt', 'Rec', 'Yds', 'TD']:
        aggregated_df[col] = ((aggregated_df[col] / aggregated_df['G']) * 17).round(2)

    # Drop the 'G' column as it's no longer needed
    aggregated_df.drop(columns='G', inplace=True)

    # Define the output directory and create it if it doesn't exist
    output_dir = 'data/outputs'
    os.makedirs(output_dir, exist_ok=True)

    # Set the path for the output CSV and save the dataframe
    output_csv_path = os.path.join(output_dir, 'wide_receiver_data_aggregated.csv')
    aggregated_df.to_csv(output_csv_path, index=False)

def transform_contract_data(input):
    df = pd.read_csv(input)

    def convert_to_number(value):
        return int(value.replace("$", "").replace(",", ""))

    df["APY"] = df["APY"].apply(convert_to_number)

    df.to_csv('data/outputs/contract_data_aggregated.csv', index=False)

    
transform_wr_data(extracted_wr_data_file_paths)
transform_contract_data(extracted_contract_data_file_path)