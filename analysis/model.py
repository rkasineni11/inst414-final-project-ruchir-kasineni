from sklearn.linear_model import LinearRegression
from sklearn.neighbors import NearestNeighbors
import numpy as np
from pro_football_reference_web_scraper import player_game_log as p
from sklearn.linear_model import Ridge

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

def find_similar_players(player_stats, all_wr_stats, n_neighbors=5):
    nbrs = NearestNeighbors(n_neighbors=n_neighbors, metric='euclidean').fit(all_wr_stats)
    distances, indices = nbrs.kneighbors(player_stats.values.reshape(1, -1))
    
    similar_players = all_wr_stats.iloc[indices[0]]
    return similar_players, distances[0]

def calculate_weights(distances):
    total_distance = sum(distances)
    weights = [1 - (d / total_distance) for d in distances]
    normalized_weights = [w / sum(weights) for w in weights]
    return normalized_weights

def estimate_contract(similar_players, weights):
    estimated_contract = 0
    for i, player in enumerate(similar_players.index):
        player_contract = get_contract_for_player(player)
        estimated_contract += player_contract * weights[i]
    
    return estimated_contract

print(project_next_year_stats([[9.375, 6.4375, 83.5, 0.625], [8.5, 6.0625, 76.8125, 0.3125], [9.666666666666666, 7.0, 94.4, 0.7333333333333333], [8.375, 5.75, 70.3125, 0.5625], [8.941176470588236, 6.470588235294118, 78.70588235294117, 0.7058823529411765], [8.066666666666666, 6.2, 65.6, 0.3333333333333333]]))

# [137.39, 101.06, 1115.74, 6.56]

find_similar_players()