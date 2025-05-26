import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
    Main function to load the CSV file and plot the data.
    """
    dp = load("life_expectancy_years.csv")
    if (dp.empty):
        raise ValueError("dp is empty")
    row = dp[dp["country"] == "Morocco"].drop(columns=['country']).transpose()
    if (row.empty):
        raise ValueError("row is empty")
    row.columns = ["Morocco"]
    row.index.name = "Years"
    row.plot(title="Morocco Life Expectancy Projections")
    plt.legend()
    plt.xlabel("Years")
    plt.ylabel("Life Expectancy")
    plt.show()


if __name__ == "__main__":
    main()
