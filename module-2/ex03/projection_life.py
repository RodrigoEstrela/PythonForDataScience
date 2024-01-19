import matplotlib.pyplot as plt
from load_csv import load


def plot_data(data_set_gdp, data_set_life):
    """
    Plots the data
    """
    # get data from the gdp csv file
    gdp_column_index = data_set_gdp.columns.get_loc("1900")
    gdp_dt_set = data_set_gdp.iloc[:, gdp_column_index]
    print("Gdp:\n", gdp_dt_set)
    # get data from the life expectancy file
    life_column_index = data_set_life.columns.get_loc("1900")
    life_dt_set = data_set_life.iloc[:, life_column_index]
    print("Life expectancy:\n", life_dt_set)
    # Draw the data as a scatter graph instead of a plot
    plt.scatter(gdp_dt_set, life_dt_set,
                label="Life Expectancy related to GDP in 1900")
    # Customize x axis
    plt.xlabel("Gross domestic product")
    plt.xscale('log')
    plt.xlim(300, 11000)
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    # Customize y axis
    plt.ylabel("Life Expectancy")
    # Customize image
    plt.title("1900")
    plt.legend(loc='lower right')
    # Display the graph
    plt.show()


def main():
    """
    calls the functions
    - Load the data
    - Plot the data
    """
    try:
        gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        data_set_life = load("life_expectancy_years.csv")
        plot_data(gdp, data_set_life)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
