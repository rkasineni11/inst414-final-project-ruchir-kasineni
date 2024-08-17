import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error
from evaluate import evaluate_contract_value
from tqdm import tqdm
import warnings

warnings.filterwarnings("ignore")

# Load the CSV data into a DataFrame
testing_df = pd.read_csv('data/outputs/contract_data_aggregated.csv')

# Function that predicts contract values (replace this with your actual function)
def predict_contract(player_name):
    try:
        return evaluate_contract_value(player_name)  # Replace this with your model's prediction logic
    except:
        return None

# Initialize a progress bar with tqdm and a custom message
tqdm.pandas(desc="Running Accuracy Tests")

# Apply the function with progress bar
testing_df['Predicted_APY'] = testing_df['Player'].progress_apply(predict_contract)

# Drop rows with NaN values in 'Predicted_APY' (in case there were any prediction errors)
testing_df.dropna(subset=['Predicted_APY'], inplace=True)

# Calculate error metrics
mae = mean_absolute_error(testing_df['APY'], testing_df['Predicted_APY'])
mae_millions = mae / 1_000_000

# Print the results
print()
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"This MAE means that, on average, the predictions made by the model are off by about {mae_millions:.2f} million")
print()
