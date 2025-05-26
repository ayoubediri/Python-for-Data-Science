import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    Parameters
    ----------
    path : str
        The path to the CSV file.
    """
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {path} was not found.")
    except pd.errors.EmptyDataError:
        raise ValueError("The file is empty.")
    except pd.errors.ParserError:
        raise ValueError(
            "Error parsing the file. Please check the file format. Is it CSV?")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")
