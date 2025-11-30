import pandas as pd

def analyze_pokemon_stats(file_path):
    dataframe = pd.read_csv(file_path)

    stats_columns = ['HP', 'Attack', 'Defense', 'Sp.Atk', 'Sp.Def', 'Speed', 'Total_Stats']

    stats_dataframe = dataframe[stats_columns]
    descriptive_stats = stats_dataframe.describe()
    
    print("\n|\t\t\t     Pokemon Battle Stats - Statistics Analysis     \t\t\t|")
    print(descriptive_stats.to_markdown())


    max_index = dataframe['Total_Stats'].idxmax()
    min_index = dataframe['Total_Stats'].idxmin()
    mid_index = (dataframe['Total_Stats'] - dataframe['Total_Stats'].median()).abs().idxmin()

    comparison_columns = ['Name'] + stats_columns
    comparion_stats = dataframe.loc[[max_index, mid_index, min_index], comparison_columns]
    comparion_stats = comparion_stats.rename(index={max_index: 'Highest Stats', mid_index: 'Average Stats', min_index: 'Lowest Stats'})
    
    print("\n|\t\t\t\t\t        Max-Min Comparison        \t\t\t\t\t|")
    print(comparion_stats.to_markdown())

if __name__ == "__main__":
    file_path = "pokedataset.csv"
    analyze_pokemon_stats(file_path)
