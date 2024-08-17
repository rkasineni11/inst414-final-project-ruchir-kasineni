import matplotlib.pyplot as plt
import warnings
from evaluate import evaluate_contract_value
import pandas as pd
import re
from analysis.model import find_similar_players

def clean_string(input_string):
    lowercased = input_string.lower()
    no_special_chars = re.sub(r'[^a-z0-9]', '', lowercased)
    return no_special_chars

def generate_bar_graph(df, player_name):
    player_name = clean_string(player_name)
    
    warnings.filterwarnings("ignore")

    project_contract_total = evaluate_contract_value(player_name)
    actual_contract = df.loc[df['Player'] == player_name, 'APY'].values[0]
    
    contracts = [actual_contract / 1_000_000, project_contract_total / 1_000_000]
    labels = ['Actual Contract', 'Projected Contract']

    plt.bar(labels, contracts, color=['blue', 'orange'])
    plt.title(f'Actual vs Projected Contract for {player_name}')
    plt.ylabel('Contract Value (Millions)')
    plt.show()

import matplotlib.pyplot as plt

def interactive_plot(df, wr_df, player_name):
    player_name = clean_string(player_name)
    
    similar_players, similarity_scores = find_similar_players(wr_df, player_name)
    
    similar_contracts = []
    for p in similar_players:
        contract_value = df.loc[df['Player'] == p, 'APY'].values[0]
        similar_contracts.append(contract_value / 1e6)

    # Scatter Plot
    plt.figure(figsize=(10, 6))
    plt.scatter(similarity_scores, similar_contracts, color='purple', s=100)

    # Adding labels to points
    for i in range(len(similar_players)):
        plt.text(similarity_scores[i], similar_contracts[i] + 0.3, 
                 similar_players[i], fontsize=12, ha='center')

    plt.xlabel('Similarity Score')
    plt.ylabel('Contract Value (Millions)')
    plt.title(f'Similarity Scores vs. Contract Values for {player_name.capitalize()}')
    plt.grid(True)
    plt.show()


def generate_graphs():
    df = pd.read_csv('data/outputs/contract_data_aggregated.csv')
    wr_df = pd.read_csv('data/outputs/wide_receiver_data_aggregated.csv')
    while True:
        warnings.filterwarnings("ignore")
        player_name = input("Please enter the player's name (e.g., 'Calvin Ridley'): ")
        print()
        try:
            project_contract_total = evaluate_contract_value(player_name)
            generate_bar_graph(df, player_name)
            interactive_plot(df, wr_df, player_name)
            print()
        except:
            print("Invalid Player Input")
            print()

generate_graphs()