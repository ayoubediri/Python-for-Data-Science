from load_csv import load
import matplotlib.pyplot as plt


def convert_string_number(value):
    """
    Convert a string representation of a number with suffixes
    (K, M, B) to a float.
    If the value is not a string or cannot be converted, return it unchanged.
    Args:
        value (str or float): The value to convert.
    Returns:
        float: The converted value,
        or the original value if it cannot be converted.
    """

    if isinstance(value, str):
        value = value.strip()
        if value.endswith('M'):
            return float(value[:-1])
        elif value.endswith('B'):
            return float(value[:-1]) * 1_000
        elif value.endswith('K'):
            return float(value[:-1]) / 1_000
    return value


def main():
    """
    Main function to load the CSV file and plot the data.
    """
    dp = load("population_total.csv")
    if dp.empty:
        raise ValueError("dp is empty")
    rows = dp[dp['country'].isin(['France', 'Morocco'])]
    rows = rows.drop(columns=['country']).transpose()
    if rows.empty:
        raise ValueError("rows is empty")
    rows = rows.applymap(convert_string_number)
    if rows.empty:
        raise ValueError("rows after conversion is empty")
    rows.columns = ['France', 'Morocco']
    print(rows)
    rows.index.name = "Years"
    rows.plot(title="France and Morocco Population Projections")
    plt.legend()
    plt.xlabel("Years")
    plt.ylabel("Population")
    plt.show()


if __name__ == "__main__":
    main()
