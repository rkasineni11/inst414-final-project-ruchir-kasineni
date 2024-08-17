import matplotlib.pyplot as plt
import warnings
from evaluate import evaluate_contract_value
import pandas as pd
import re
from analysis.model import find_similar_players

def clean_string(input_string):
    """
    Cleans a string by converting it to lowercase and removing non-alphanumeric characters.
    
    Args:
        input_string (str): The string to be cleaned.
    
    Returns:
        str: The cleaned string with only lowercase alphanumeric characters.
    """
    lowercased = input_string.lower()
    no_special_chars = re.sub(r'[^a-z0-9]', '', lowercased)
    return no_special_chars

def generate_bar_graph(df, player_name):
    """
    Generates a bar graph comparing the actual and projected contract values for a player.
    
    Args:
        df (pd.DataFrame): DataFrame containing player data, including actual contract values.
        player_name (str): The name of the player whose contracts are being compared.
    
    Returns:
        None: Displays the bar graph.
    """
    # Clean the player's name to ensure consistent matching
    player_name = clean_string(player_name)
    
    # Suppress any warnings that might occur during the plotting
    warnings.filterwarnings("ignore")

    # Evaluate the projected contract value for the player
    project_contract_total = evaluate_contract_value(player_name)
    
    # Get the actual contract value from the DataFrame
    actual_contract = df.loc[df['Player'] == player_name, 'APY'].values[0]
    
    # Prepare data for plotting
    contracts = [actual_contract / 1_000_000, project_contract_total / 1_000_000]  # Convert to millions
    labels = ['Actual Contract', 'Projected Contract']

    # Create the bar graph
    plt.bar(labels, contracts, color=['blue', 'orange'])
    plt.title(f'Actual vs Projected Contract for {player_name.capitalize()}')
    plt.ylabel('Contract Value (Millions)')
    plt.show()

def interactive_plot(df, wr_df, player_name):
    """
    Creates an interactive scatter plot showing similarity scores vs. contract values for similar players.
    
    Args:
        df (pd.DataFrame): DataFrame containing player data, including contract values.
        wr_df (pd.DataFrame): DataFrame containing wide receiver data for similarity analysis.
        player_name (str): The name of the player being analyzed.
    
    Returns:
        None: Displays the scatter plot.
    """
    # Clean the player's name to ensure consistent matching
    player_name = clean_string(player_name)
    
    # Find similar players and their similarity scores
    similar_players, similarity_scores = find_similar_players(wr_df, player_name)
    
    # Get contract values for the similar players
    similar_contracts = []
    for p in similar_players:
        contract_value = df.loc[df['Player'] == p, 'APY'].values[0]
        similar_contracts.append(contract_value / 1e6)  # Convert to millions

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
    """
    Main function to generate visualizations based on user input.
    
    Continuously prompts the user for a player's name, generates a bar graph comparing
    the player's actual and projected contract values, and generates a scatter plot showing
    the relationship between similarity scores and contract values for similar players.
    
    Returns:
        None: Displays the graphs for the input player.
    """
    # Load data from CSV files
    df = pd.read_csv('data/outputs/contract_data_aggregated.csv')
    wr_df = pd.read_csv('data/outputs/wide_receiver_data_aggregated.csv')
    
    # Continuous loop to allow for multiple player queries
    while True:
        warnings.filterwarnings("ignore")  # Suppress warnings
        
        # Prompt user for player name
        player_name = input("Please enter the player's name (e.g., 'Calvin Ridley'): ")
        print()
        
        try:
            # Generate and display the graphs for the player
            project_contract_total = evaluate_contract_value(player_name)
            generate_bar_graph(df, player_name)
            interactive_plot(df, wr_df, player_name)
            print()
        except:
            # Handle any errors that occur during the process
            print("Invalid Player Input")
            print()

# Run the generate_graphs function when the script is executed
generate_graphs()
