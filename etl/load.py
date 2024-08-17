import pandas as pd
from pro_football_reference_web_scraper import player_game_log as p

def load_dataframes(player_name, input_position):
    wr_dataframe = pd.read_csv('data/outputs/contract_data_aggregated.csv')
    contract_dataframe = pd.read_csv('data/outputs/wide_receiver_data_aggregated.csv')
    all_season_logs = []
    
    for i in range(2018, 2024):
        try:
            game_log = p.get_player_game_log(player=player_name, position=input_position, season=i)
            
            filtered_game_log = game_log[['tgt', 'rec', 'rec_yds', 'rec_td']]
            
            season_totals = filtered_game_log.sum().tolist()
            
            total_games = len(filtered_game_log)
            
            if total_games > 0:
                season_averages = [total / total_games for total in season_totals]
            else:
                season_averages = [0] * len(season_totals)
            
            all_season_logs.append(season_averages)
        except:
            continue
        
    return wr_dataframe, contract_dataframe, all_season_logs

a, b, c = load_dataframes("Travis Kelce", "TE")
print(c)