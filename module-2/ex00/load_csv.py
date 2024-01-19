import pandas as pd


def load(path: str):
    """
    Load the csv file into a DataSet
    Print the DataSet dimensions
    Return the DataSet
    """

    try:
        dt_set = pd.read_csv(path)
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: File '{path}' is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: Unable to parse '{path}'. File must be a valid csv")
        return None

    print(f"Loading dataset of dimensions {dt_set.shape}")
    return dt_set
