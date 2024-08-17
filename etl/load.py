import os
import pandas as pd
from pro_football_reference_web_scraper import player_game_log as p

def get_player_stats(input_player, input_position):
    # Get the game log data
    game_log = p.get_player_game_log(player=input_player, position=input_position, season=2023)
    
    # Convert the game log data to a pandas DataFrame
    df = pd.DataFrame(game_log)
    
    # Define the output file path
    output_csv_path = f'data/outputs/{input_player}_game_log_2023.csv'
    
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)
    
    # Save the DataFrame to a CSV file
    df.to_csv(output_csv_path, index=False)
    
    print(f"CSV file saved to {output_csv_path}")

# Call the function to save the stats to a CSV file
x = get_player_stats("Cooper Kupp", "WR")
