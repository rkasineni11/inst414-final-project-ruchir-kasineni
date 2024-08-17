# inst414-final-project-ruchir-kasineni

## Project Overview
This project aims to predict the fair contract value of NFL wide receivers based on historical performance data and contract values of similar players. The business problem addressed is the estimation of a player's contract value, which can assist teams, agents, and analysts in making informed decisions regarding player contracts.

## Data Sets Used
* Wide Receiver Data: Includes player performance metrics such as targets, receptions, yards, and touchdowns for multiple years.
* NFL Contracts Data: Contains contract details, including the Average Per Year (APY) salary of NFL players.

## Techniques Employed
* Data Extraction, Transformation, and Loading (ETL): Data is extracted, cleaned, and transformed to be used for analysis.
* Nearest Neighbors Algorithm: Used to find players similar to the input player based on performance statistics.
* Weighted Average Calculation: The contract value is predicted by calculating a weighted average of the contracts of similar players.

## Expected Outputs
* Predicted Contract Value: The main output is the projected fair contract value (APY) for a given player, based on the contracts of similar players.

## Setup Instructions

1. **Clone the repository**: Download the repository to your local machine.
2. **Set up a virtual environment**: Create a virtual environment in the project directory.
3. **Activate the virtual environment**: Activate the environment to manage dependencies.
4. **Install dependencies**: Use the requirements.txt file to install all necessary packages.

## Makefile Usage
The `Makefile` in the project allows you to easily run various tasks:

This command will start the interactive prompt for predicting NFL player contract values.
`make run`


To run the tests for the project, use the following command:
`make test`

To generate visualizations and charts for the project, run:
`make charts`


## Code Package Structure
The project is organized into the following main directories:
* `data/`: Contains the raw and processed data files.
    * `reference_tables/`: Original datasets for wide receivers and contracts.
    * `extracted/`: Cleaned and transformed datasets.
    * `outputs/`: Final aggregated data used for analysis.

* `etl/`: Contains scripts for Extract, Transform, and Load (ETL) operations.
    * `extract.py`: Handles data extraction and cleaning.
    * `transform.py`: Manages data transformation and aggregation.
    * `load.py`: Responsible for loading data into DataFrames.
* `analysis/`: Contains scripts for data analysis and modeling.
    * `model.py`: Includes functions for finding similar players and calculating weighted contract values.
* `main.py`: The main entry point for running the project.
* `README.md`: Documentation for the project.
* `Makefile`: Contains commands for running tests, cleaning up files, and other utility tasks.

