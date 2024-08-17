import warnings
from evaluate import evaluate_contract_value

warnings.filterwarnings("ignore")

player_name = input("Please enter the player's name (e.g., 'Calvin Ridley'): ")

try:
    print(evaluate_contract_value(player_name))
except:
    print("Invalid Player Input")