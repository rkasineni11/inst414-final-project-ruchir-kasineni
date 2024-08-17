import warnings
from evaluate import evaluate_contract_value

while True:
    warnings.filterwarnings("ignore")
    player_name = input("Please enter the player's name (e.g., 'Calvin Ridley'): ")
    print()
    try:
        print(evaluate_contract_value(player_name))
        print()
    except:
        print("Invalid Player Input")
        print()
