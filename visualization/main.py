import pandas as pd
import time
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('gtk3cairo')


data_dir = '../data'


def parse_global_temperature_measurements():
    df = pd.read_csv(f'{data_dir}/measurements/global-temperatures/graph.csv')
    print(df)
    return df


if __name__ == '__main__':
    df = parse_global_temperature_measurements()
    df.plot()
    plt.show(block=True)
