import warnings
from evaluate import evaluate_contract_value

warnings.filterwarnings("ignore")

player_name = input("Please enter the player's name (e.g., 'Calvin Ridley'): ")
position = input("Please enter the player's position (e.g., 'WR'): ")    
print(evaluate_contract_value(player_name, position))