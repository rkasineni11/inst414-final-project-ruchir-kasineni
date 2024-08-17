from sklearn.linear_model import LinearRegression
from sklearn.neighbors import NearestNeighbors
import numpy as np
from pro_football_reference_web_scraper import player_game_log as p
from sklearn.linear_model import Ridge
import pandas as pd
from sklearn.preprocessing import StandardScaler
import re

def find_similar_players(wr_df, input_player):
    """
    Finds the top 5 players most similar to the input player based on their statistics.

    Args:
        wr_df (pd.DataFrame): DataFrame containing wide receiver statistics.
        input_player (str): Name of the player for whom similar players are to be found.
    
    Returns:
        tuple: A tuple containing:
            - closest_players (list of str): List of the top 5 similar players.
            - similarity_scores (list of float): List of similarity scores for these players.
    """
    # Clean the input player name
    input_player = clean_string(input_player)
    
    # Extract the input player's stats
    input_stats = wr_df[wr_df['Player'] == input_player].iloc[0].tolist()[1:]
    
    # Prepare the data by excluding the input player
    data = wr_df[wr_df['Player'] != input_player]
    
    # Standardize the statistics for comparison
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data[['Tgt', 'Rec', 'Yds', 'TD']])
    
    # Fit the nearest neighbors model
    nn = NearestNeighbors(n_neighbors=5)
    nn.fit(data_scaled)
    
    # Scale the input player's stats and find the nearest neighbors
    input_stats_scaled = scaler.transform([input_stats])
    distances, indices = nn.kneighbors(input_stats_scaled)
    
    # Retrieve the closest players and calculate similarity scores
    closest_players = data.iloc[indices[0]]['Player'].tolist()
    similarity_scores = [1 / dist if dist != 0 else float('inf') for dist in distances[0]]

    return closest_players, similarity_scores

def calculate_weights(distances):
    """
    Calculates the normalized similarity scores (weights) for each similar player.

    Args:
        distances (list of float): List of distances from the input player to each similar player.
    
    Returns:
        list of float: Normalized similarity scores (weights) for each similar player.
    """
    # Calculate the total similarity (sum of distances)
    total_similarity = sum(distances)
    
    # Normalize the similarity scores
    normalized_similarity_scores = [score / total_similarity for score in distances]
    
    return normalized_similarity_scores

def calculate_weighted_contract_total(contract_df, players, weights):
    """
    Calculates the weighted average contract value based on similar players' contracts and weights.

    Args:
        contract_df (pd.DataFrame): DataFrame containing player contract data.
        players (list of str): List of similar players' names.
        weights (list of float): List of weights corresponding to each similar player.
    
    Returns:
        float: The weighted average contract value (APY) for the input player.
    """
    # Filter the contract data to include only the similar players
    data = contract_df
    filtered_data = data[data['Player'].isin(players)]
    filtered_data.set_index('Player', inplace=True)
    
    # Order the data according to the list of players
    filtered_data = filtered_data.loc[players]
    
    # Calculate the weighted APY (Average Per Year)
    filtered_data['Weighted APY'] = filtered_data['APY'] * weights
    
    # Sum up the weighted APY to get the total weighted contract value
    total_weighted_contract = filtered_data['Weighted APY'].sum()
    
    return round(total_weighted_contract)

def clean_string(input_string):
    """
    Cleans a string by converting it to lowercase and removing non-alphanumeric characters.

    Args:
        input_string (str): The string to be cleaned.
    
    Returns:
        str: The cleaned string.
    """
    lowercased = input_string.lower()
    no_special_chars = re.sub(r'[^a-z0-9]', '', lowercased)
    return no_special_chars
