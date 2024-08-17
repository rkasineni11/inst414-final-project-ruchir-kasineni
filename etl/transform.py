import os
import pandas as pd

def transform_wr_data(input):
    """
    Transforms wide receiver (WR) data by aggregating stats across multiple years
    and calculating averages per game, normalized to a 17-game season.

    Args:
        input (list of str): List of file paths to the WR data CSV files.
    
    Returns:
        None: The processed data is saved as a new CSV file in the 'data/outputs' directory.
    """
    # Initialize an empty DataFrame to hold player data
    player_data_df = pd.DataFrame()

    for file_path in input:
        # Extract the year from the file name
        year = os.path.basename(file_path).split('_')[-1].split('.')[0]
        
        # Read the data, filter by position (WR or TE), and select necessary columns
        df = pd.read_csv(file_path)
        df = df[df['Pos'].isin(['WR', 'TE'])]
        df = df[['Player', 'G', 'Tgt', 'Rec', 'Yds', 'TD']]
        
        # Concatenate data for all years into a single DataFrame
        player_data_df = pd.concat([player_data_df, df], ignore_index=True)

    # Aggregate data by player, summing up all relevant columns
    aggregated_df = player_data_df.groupby('Player').agg({
        'G': 'sum',
        'Tgt': 'sum',
        'Rec': 'sum',
        'Yds': 'sum',
        'TD': 'sum'
    }).reset_index()

    # Calculate averages per game for 'Tgt', 'Rec', 'Yds', 'TD', normalized to a 17-game season
    for col in ['Tgt', 'Rec', 'Yds', 'TD']:
        aggregated_df[col] = ((aggregated_df[col] / aggregated_df['G']) * 17).round(2)

    # Drop the 'G' (Games Played) column as it's no longer needed
    aggregated_df.drop(columns='G', inplace=True)

    # Define the output directory and create it if it doesn't exist
    output_dir = 'data/outputs'
    os.makedirs(output_dir, exist_ok=True)

    # Set the path for the output CSV and save the aggregated DataFrame
    output_csv_path = os.path.join(output_dir, 'wide_receiver_data_aggregated.csv')
    aggregated_df.to_csv(output_csv_path, index=False)

def transform_contract_data(input):
    """
    Transforms contract data by converting salary strings into numerical values.

    Args:
        input (str): File path to the player contract data CSV file.
    
    Returns:
        None: The processed data is saved as a new CSV file in the 'data/outputs' directory.
    """
    # Read the contract data into a DataFrame
    df = pd.read_csv(input)

    # Function to convert salary strings to integers
    def convert_to_number(value):
        return int(value.replace("$", "").replace(",", ""))

    # Apply the conversion function to the 'APY' (Average Per Year) column
    df["APY"] = df["APY"].apply(convert_to_number)

    # Save the transformed contract data to a new CSV file
    df.to_csv('data/outputs/contract_data_aggregated.csv', index=False)
    
def match_csvs():
    """
    Matches wide receiver data with contract data based on player names,
    filtering the WR data to include only players present in the contract data.

    Returns:
        None: The filtered wide receiver data is saved back to the 'data/outputs' directory.
    """
    # Load the aggregated wide receiver data and contract data
    df1 = pd.read_csv('data/outputs/wide_receiver_data_aggregated.csv')
    df2 = pd.read_csv('data/outputs/contract_data_aggregated.csv')
    
    # Filter df1 (WR data) to only include rows where 'Player' is also in df2 (Contract data)
    filtered_df1 = df1[df1['Player'].isin(df2['Player'])]
    
    # Define the output path for the filtered WR data
    output_csv_path = os.path.join('data/outputs/wide_receiver_data_aggregated.csv')
    
    # Save the filtered DataFrame back to the CSV file
    filtered_df1.to_csv(output_csv_path, index=False)
