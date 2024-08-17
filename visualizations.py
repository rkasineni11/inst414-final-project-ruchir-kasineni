import matplotlib.pyplot as plt
import warnings
from evaluate import evaluate_contract_value
import pandas as pd
import re
import plotly.express as px

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

def interactive_plot(similar_players, similarity_scores):
    data = {
        'Player': similar_players,
        'Similarity Score': similarity_scores,
        'Contract': contracts
    }
    df = pd.DataFrame(data)

    fig = px.scatter(df, x='Similarity Score', y='Contract', text='Player', title="Similarity Scores vs Contracts")
    fig.update_traces(textposition='top center')
    fig.show()


df = pd.read_csv('data/outputs/contract_data_aggregated.csv')

while True:
    warnings.filterwarnings("ignore")
    player_name = input("Please enter the player's name (e.g., 'Calvin Ridley'): ")
    print()
    try:
        project_contract_total = evaluate_contract_value(player_name)
        generate_bar_graph(df, player_name)
        print()
    except:
        print("Invalid Player Input")
        print()