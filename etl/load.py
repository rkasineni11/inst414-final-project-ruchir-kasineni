import pandas as pd

def load_dataframes():
    """
    Loads the wide receiver and contract data from CSV files.

    Returns:
        tuple: A tuple containing two pandas DataFrames:
            - wr_dataframe (pd.DataFrame): The DataFrame containing aggregated wide receiver data.
            - contract_dataframe (pd.DataFrame): The DataFrame containing aggregated contract data.
    """
    # Load the wide receiver data from the specified CSV file
    wr_dataframe = pd.read_csv('data/outputs/wide_receiver_data_aggregated.csv')
    
    # Load the contract data from the specified CSV file
    contract_dataframe = pd.read_csv('data/outputs/contract_data_aggregated.csv')
    
    # Return both DataFrames as a tuple
    return wr_dataframe, contract_dataframe
