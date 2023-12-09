import pandas
import array


def load(path: str) -> array:
    df = pandas.read_csv('life_expectancy_years.csv', index_col=0)
    print(df.shape)
    print(df)
