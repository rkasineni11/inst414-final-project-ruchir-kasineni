import pandas as pd

def load_dataframes():
    wr_dataframe = pd.read_csv('data/outputs/wide_receiver_data_aggregated.csv')
    contract_dataframe = pd.read_csv('data/outputs/contract_data_aggregated.csv')
    return wr_dataframe, contract_dataframe