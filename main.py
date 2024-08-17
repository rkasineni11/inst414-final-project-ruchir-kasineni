import warnings
from evaluate import evaluate_contract_value

def main():
    """
    Main interactive loop to evaluate and display a player's projected contract value.
    Continuously prompts the user for a player's name and displays the evaluation.
    """
    while True:
        # Suppress any warnings to keep the output clean
        warnings.filterwarnings("ignore")
        
        # Prompt the user for a player's name
        player_name = input("Please enter the player's name (e.g., 'Calvin Ridley'): ")
        print()
        
        try:
            # Evaluate the contract value for the given player
            project_contract_total = evaluate_contract_value(player_name)
            print(f"Project Fair Value Contract: ${project_contract_total} Million Per Year")
            print()
        except Exception as e:
            # Handle any errors, such as invalid player input
            print("Invalid Player Input")
            print()

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
