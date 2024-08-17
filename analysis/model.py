from sklearn.linear_model import LinearRegression
from sklearn.neighbors import NearestNeighbors
import numpy as np
from pro_football_reference_web_scraper import player_game_log as p
from sklearn.linear_model import Ridge
import pandas as pd
from sklearn.preprocessing import StandardScaler

def project_next_year_stats(all_season_logs):
    player_stats = np.array(all_season_logs)
    
    # Initialize the Ridge regression model with regularization
    model = Ridge(alpha=1.0)  # alpha is the regularization strength
    
    # Fit the model on the available data
    model.fit(player_stats, player_stats)  # X and y are the same here
    
    # Predict the next year's stats for the last entry (or any new data)
    predicted = model.predict([player_stats[-1]])[0]  # Predict based on the last known data
    
    # Round, multiply by 17, and convert to a list
    processed_output = list(np.round(predicted * 17, 2))
    
    return processed_output

def find_similar_players(input_stats):
    data = pd.read_csv('data/outputs/wide_receiver_data_aggregated.csv')
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

def calculate_weighted_contract_total(players, weights):
    data = pd.read_csv('data/outputs/contract_data_aggregated.csv')
    
    filtered_data = data[data['Player'].isin(players)]
    filtered_data.set_index('Player', inplace=True)
    
    filtered_data = filtered_data.loc[players]
    
    print(filtered_data)
    
   #  total_weighted_contract = filtered_data['Weighted Contract'].sum()
    
    # return total_weighted_contract

# print(project_next_year_stats([[9.375, 6.4375, 83.5, 0.625], [8.5, 6.0625, 76.8125, 0.3125], [9.666666666666666, 7.0, 94.4, 0.7333333333333333], [8.375, 5.75, 70.3125, 0.5625], [8.941176470588236, 6.470588235294118, 78.70588235294117, 0.7058823529411765], [8.066666666666666, 6.2, 65.6, 0.3333333333333333]]))

# [137.39, 101.06, 1115.74, 6.56]

players, weights = find_similar_players([137.39, 101.06, 1115.74, 6.56])
print(calculate_weights(weights))

print(calculate_weighted_contract_total(players, weights))