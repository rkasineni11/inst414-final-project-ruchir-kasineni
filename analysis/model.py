from sklearn.linear_model import LinearRegression
from sklearn.neighbors import NearestNeighbors
import numpy as np
from pro_football_reference_web_scraper import player_game_log as p
from sklearn.linear_model import Ridge
import pandas as pd
from sklearn.preprocessing import StandardScaler

def project_next_year_stats(all_season_logs):
    player_stats = np.array(all_season_logs)
    
    model = Ridge(alpha=1.0)
    model.fit(player_stats, player_stats)
    
    predicted = model.predict([player_stats[-1]])[0]
    processed_output = list(np.round(predicted * 17, 2))
    
    return processed_output

def find_similar_players(wr_df, input_stats, input_player):
    data = wr_df[wr_df['Player'] != input_player]
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data[['Tgt', 'Rec', 'Yds', 'TD']])
    
    nn = NearestNeighbors(n_neighbors=5)
    nn.fit(data_scaled)
    
    input_stats_scaled = scaler.transform([input_stats])
    distances, indices = nn.kneighbors(input_stats_scaled)
    
    closest_players = data.iloc[indices[0]]['Player'].tolist()
    similarity_scores = [1 / dist if dist != 0 else float('inf') for dist in distances[0]]

    return closest_players, similarity_scores

def calculate_weights(distances):
    total_similarity = sum(distances)
    normalized_similarity_scores = [score / total_similarity for score in distances]
    return normalized_similarity_scores

def calculate_weighted_contract_total(contract_df, players, weights):
    data = contract_df
    
    filtered_data = data[data['Player'].isin(players)]
    filtered_data.set_index('Player', inplace=True)
    
    filtered_data = filtered_data.loc[players]
    filtered_data['Weighted APY'] = filtered_data['APY'] * weights
    
    total_weighted_contract = filtered_data['Weighted APY'].sum()
    return round(total_weighted_contract)