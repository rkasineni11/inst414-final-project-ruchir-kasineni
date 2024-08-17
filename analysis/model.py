from sklearn.linear_model import LinearRegression
from sklearn.neighbors import NearestNeighbors
import numpy as np

def project_next_year_stats(player_stats):
    X = np.arange(len(player_stats)).reshape(-1, 1)
    projections = {}
    
    for stat in player_stats.columns[1:]:
        y = player_stats[stat].values
        model = LinearRegression().fit(X, y)
        next_year = np.array([[len(player_stats)]])
        projections[stat] = model.predict(next_year)[0]
    
    return projections

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
