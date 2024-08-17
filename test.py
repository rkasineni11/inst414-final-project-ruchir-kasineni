import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error
from evaluate import evaluate_contract_value
from tqdm import tqdm
import warnings

# Suppress warnings to keep the output clean
warnings.filterwarnings("ignore")

# Load the CSV data into a DataFrame
testing_df = pd.read_csv('data/outputs/contract_data_aggregated.csv')

def predict_contract(player_name):
    """
    Predicts the contract value (APY) for a given player using the evaluate_contract_value function.
    
    Args:
        player_name (str): The name of the player whose contract value is to be predicted.
    
    Returns:
        float or None: The predicted contract value (APY) in dollars, or None if an error occurs.
    """
    try:
        return evaluate_contract_value(player_name)  # Replace this with your model's prediction logic
    except:
        return None

# Initialize a progress bar with tqdm and a custom message
tqdm.pandas(desc="Running Accuracy Tests")

# Apply the prediction function with a progress bar
testing_df['Predicted_APY'] = testing_df['Player'].progress_apply(predict_contract)

# Drop rows with NaN values in 'Predicted_APY' (in case there were any prediction errors)
testing_df.dropna(subset=['Predicted_APY'], inplace=True)

# Calculate error metrics
mae = mean_absolute_error(testing_df['APY'], testing_df['Predicted_APY'])
mae_millions = mae / 1_000_000  # Convert MAE to millions for easier interpretation

# Print the results
print()
print(f"Mean Absolute Error (MAE): ${mae:.2f}")
print(f"This MAE means that, on average, the predictions made by the model are off by about ${mae_millions:.2f} million.")
print()
