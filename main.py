import warnings
from evaluate import evaluate_contract_value

while True:
    warnings.filterwarnings("ignore")
    player_name = input("Please enter the player's name (e.g., 'Calvin Ridley'): ")
    print()
    try:
        project_contract_total = evaluate_contract_value(player_name)
        print(f"Project Fair Value Contract: ${project_contract_total} Million Per Year")
        print()
    except:
        print("Invalid Player Input")
        print()
