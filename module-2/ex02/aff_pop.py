import matplotlib.pyplot as plt
import numpy as np
from load_csv import load


def convert_to_numeric(value):
    """
    Cleans the values from the csv file
    """
    try:
        # Remove 'M' suffix and convert to numeric
        if 'B' in value:
            return float(value.rstrip('B')) * 1000000000
        elif 'M' in value:
            return float(value.rstrip('M')) * 1000000
        elif 'k' in value:
            return float(value.rstrip('k')) * 1000
        else:
            return float(value)
    except ValueError:
        # Handle cases where conversion is not possible
        return float('nan')


def format_num(number):
    """
    Re-formats the values to better readability
    """
    suffixes = ["", "k", "M", "B"]
    magnitude = 0

    while number >= 1000 and magnitude < len(suffixes) - 1:
        magnitude += 1
        number /= 1000.0

    return f"{int(number)}{suffixes[magnitude]}"


def calculate_tick_positions(max_value):
    """
    Calculates the optimal ticks
    """
    magnitude = 10 ** (len(str(int(max_value))) - 1)
    rounded_value = int(max_value / magnitude) * magnitude
    last_tick = [rounded_value * i for i in range(0, 3)][1]
    return (last_tick - (last_tick * (2/3)),
            last_tick - (last_tick * (1/3)),
            last_tick)


def data_set_graph(data_set, country1, country2):
    """
    Plots the graph for two countries population projections with shared y-axis
    """
    country1_data = data_set[data_set['country'] == country1]
    country2_data = data_set[data_set['country'] == country2]

    if country1_data.empty or country2_data.empty:
        print("Error: One or both of the countries not found in the dataset.")
        return

    years = data_set.columns[1:252]

    # Convert population values to numeric
    c1_values = (country1_data.iloc[:, 1:252]
                 .map(convert_to_numeric).values.flatten())
    c2_values = (country2_data.iloc[:, 1:252]
                 .map(convert_to_numeric).values.flatten())
    max_value = max(max(c1_values), max(c2_values))
    # Set y-axis limits based on the min and max values of both countries' data
    y_axis_min = min(min(c1_values), min(c2_values))
    y_axis_min -= y_axis_min * 0.9
    y_axis_max = max_value
    y_axis_max += y_axis_max * 0.15
    # Plot for country 1
    plt.plot(years, c1_values, label=f"{country1}")
    # Plot for country 2
    plt.plot(years, c2_values, label=f"{country2}")
    # Customize the plot
    plt.xlabel("Year")
    plt.xticks(np.arange(0, 251, 1)[::40])
    plt.ylabel("Population")
    custom_yticks = calculate_tick_positions(max_value)
    custom_ylabels = [format_num(x) for x in custom_yticks]
    plt.yticks(custom_yticks, custom_ylabels)
    plt.title("Population Projections")
    plt.legend(loc='lower right')
    # Set shared y-axis limits
    plt.ylim(y_axis_min, y_axis_max)
    # Display the plot
    plt.show()


def main():
    """
    Using the functions:
    - Load the data
    - Display the data
    """
    try:
        data_set = load("population_total.csv")
        data_set_graph(data_set, "Portugal", "France")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
