import os
import pandas as pd
from pro_football_reference_web_scraper import player_game_log as p

def get_player_stats(input_player, input_position):
    game_log = p.get_player_game_log(player=input_player, position=input_position, season=2023)
    
    df = pd.DataFrame(game_log)
    
    output_csv_path = f'data/outputs/{input_player}_game_log_2023.csv'
    
    os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)
    
    df.to_csv(output_csv_path, index=False)
    
x = get_player_stats("Cooper Kupp", "WR")
