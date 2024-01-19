import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from load_csv import load


def data_set_graph(data_set: pd.DataFrame, country: str):
    """
    Displays the info from the specified country
    """
    country_data = data_set[data_set['country'] == country]
    if country_data.empty:
        print(f"Error: '{country} not found in the dataset.")
        return

    years = country_data.columns[1:]
    values = country_data.iloc[:, 1:].values.flatten()

    plt.plot(years, values, label=country)

    plt.title(f"{country} Life expectancy Projections")
    plt.xlabel("Year")
    plt.xticks(np.arange(0, 300, 1)[::40])
    plt.ylabel("Life expectancy")
    plt.legend()
    plt.show()


def main():
    """
    Using the functions:
    - Load the data
    - Display the data
    """
    try:
        data_set = load("life_expectancy_years.csv")
        data_set_graph(data_set, "Portugal")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
