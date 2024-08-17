from etl.extract import extract_wr_data, extract_contract_data
from etl.load import load_dataframes
from etl.transform import transform_wr_data, transform_contract_data, match_csvs
from analysis.model import find_similar_players, calculate_weights, calculate_weighted_contract_total

wr_data_file_paths = [
    'data/reference_tables/2021_Wide_Receiver_Data - Sheet1.csv',
    'data/reference_tables/2022_Wide_Receiver_Data - Sheet1.csv',
    'data/reference_tables/2023_Wide_Receiver_Data - Sheet1.csv'
]

extracted_wr_data_file_paths = [
    'data/extracted/Extracted_Wide_Receiver_Data_2021.csv',
    'data/extracted/Extracted_Wide_Receiver_Data_2022.csv',
    'data/extracted/Extracted_Wide_Receiver_Data_2023.csv'
]

contract_data_file_path = 'data/reference_tables/NFL Contracts - Sheet1.csv'

extracted_contract_data_file_path = 'data/extracted/Extracted_Player_Contracts.csv'

def evaluate_contract_value(player_name, input_position):
    extract_wr_data(wr_data_file_paths)
    extract_contract_data(contract_data_file_path)
    
    transform_wr_data(extracted_wr_data_file_paths)
    transform_contract_data(extracted_contract_data_file_path)
    
    match_csvs()
    
    wr_dataframe, contract_dataframe = load_dataframes()
    
    similar_players, similarity_scores = find_similar_players(wr_dataframe, player_name)
    normalize_weights = calculate_weights(similarity_scores)
    project_contract_total = calculate_weighted_contract_total(contract_dataframe, similar_players, normalize_weights)
    return f"Project Fair Value Contract: ${project_contract_total} Million Per Year"