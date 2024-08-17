### 3 Year Average of Every WR
### 5 Year Trailing Stats of Input WR
### Contracts for Every WR
import pandas as pd

def create_model():
    wr_dataframe = pd.read_csv('data/outputs/contract_data_aggregated.csv')
    contract_dataframe = pd.read_csv('data/outputs/wide_receiver_data_aggregated.csv')

print(create_model())