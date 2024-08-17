def evaluate_contract_value(player_name, input_position):
    wr_dataframe, contract_dataframe, all_season_logs = load_dataframes(player_name, input_position)
    
    if len(all_season_logs) < 3:
        return "Please Choose a Player Drafted 2021 or Earlier"
    else:
        next_year_projected_stats = project_next_year_stats(all_season_logs)
        similar_players, similarity_scores = find_similar_players(wr_dataframe, next_year_projected_stats)
        normalize_weights = calculate_weights(similarity_scores)
        calculate_weighted_contract_total = (contract_dataframe, similar_players, normalize_weights)
        return f"Project Fair Value Contract: ${calculate_weighted_contract_total} Million Per Year"