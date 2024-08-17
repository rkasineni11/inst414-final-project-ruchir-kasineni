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
    
    wr_dataframe, contract_dataframe, all_season_logs = load_dataframes(player_name, input_position)
    
    if len(all_season_logs) < 3:
        return "Please Choose a Player Drafted 2021 or Earlier"
    else:
        next_year_projected_stats = project_next_year_stats(all_season_logs)
        similar_players, similarity_scores = find_similar_players(wr_dataframe, next_year_projected_stats, player_name)
        normalize_weights = calculate_weights(similarity_scores)
        calculate_weighted_contract_total = (contract_dataframe, similar_players, normalize_weights)
        return f"Project Fair Value Contract: ${calculate_weighted_contract_total} Million Per Year"