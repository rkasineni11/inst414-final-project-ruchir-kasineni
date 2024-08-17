from etl.extract import extract_wr_data, extract_contract_data
from etl.load import load_dataframes
from etl.transform import transform_wr_data, transform_contract_data, match_csvs
from analysis.model import find_similar_players, calculate_weights, calculate_weighted_contract_total

# File paths for wide receiver data across multiple years
wr_data_file_paths = [
    'data/reference_tables/2021_Wide_Receiver_Data - Sheet1.csv',
    'data/reference_tables/2022_Wide_Receiver_Data - Sheet1.csv',
    'data/reference_tables/2023_Wide_Receiver_Data - Sheet1.csv'
]

# File paths for the extracted wide receiver data
extracted_wr_data_file_paths = [
    'data/extracted/Extracted_Wide_Receiver_Data_2021.csv',
    'data/extracted/Extracted_Wide_Receiver_Data_2022.csv',
    'data/extracted/Extracted_Wide_Receiver_Data_2023.csv'
]

# File path for the NFL contract data
contract_data_file_path = 'data/reference_tables/NFL Contracts - Sheet1.csv'

# File path for the extracted contract data
extracted_contract_data_file_path = 'data/extracted/Extracted_Player_Contracts.csv'

def evaluate_contract_value(player_name):
    """
    Evaluates the projected contract value for a given player based on similar players' data.
    
    This function extracts, transforms, and loads the necessary data, identifies players
    similar to the input player, calculates the similarity weights, and then computes
    the weighted average contract value for the input player.
    
    Args:
        player_name (str): The name of the player whose contract value is being evaluated.
    
    Returns:
        float: The projected contract value (APY) for the input player.
    """
    # Extract wide receiver and contract data from the specified file paths
    extract_wr_data(wr_data_file_paths)
    extract_contract_data(contract_data_file_path)
    
    # Transform the extracted data
    transform_wr_data(extracted_wr_data_file_paths)
    transform_contract_data(extracted_contract_data_file_path)
    
    # Match the wide receiver data with contract data
    match_csvs()
    
    # Load the transformed data into DataFrames
    wr_dataframe, contract_dataframe = load_dataframes()
    
    # Find the players similar to the input player and calculate their similarity scores
    similar_players, similarity_scores = find_similar_players(wr_dataframe, player_name)
    
    # Normalize the similarity scores to get weights
    normalize_weights = calculate_weights(similarity_scores)
    
    # Calculate the weighted average contract value using the similar players' data
    project_contract_total = calculate_weighted_contract_total(contract_dataframe, similar_players, normalize_weights)
    
    return project_contract_total
