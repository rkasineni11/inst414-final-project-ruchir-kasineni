### 3 Year Average of Every WR
### 5 Year Trailing Stats of Input WR
### Contracts for Every WR
from etl.load import load_dataframes

def create_model():
    wr_df, contract_df = load_dataframes()

    print(wr_df)
    print(contract_df)

print(create_model())