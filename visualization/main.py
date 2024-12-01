import pandas as pd
import time
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('gtk3cairo')


data_dir = '../data'


def parse_measurements():
    f = f'{data_dir}/measurements/global-temperatures/graph.csv'
    df = pd.read_csv(f, index_col='Year')

    print(df.columns)
    print(df.index)
    print(df)
    # offset to change from 1951-1980 baseline to 1850-1900
    df += 0.35 # somewhere between 0.3 and 0.4?
    return df

def parse_projections():
    f = f'{data_dir}/projections/ssp-iam-v2-201811/data.csv'
    df = pd.read_csv(f)

    df = df[df['VARIABLE'] == 'Diagnostics|MAGICC6|Temperature|Global Mean']
    df['MODEL-SCENARIO'] = df['MODEL'] + df['SCENARIO']
    print(df)
    df = df\
        .set_index(['MODEL-SCENARIO'])\
        .drop(columns=['MODEL', 'SCENARIO', 'REGION', 'VARIABLE', 'UNIT'])\
        .T
    df = df.rename_axis('Year')
    df.index = df.index.astype('int64')
    print(df.columns)
    print(df.index)
    print(df)
    return df

if __name__ == '__main__':
    measurements_df = parse_measurements()
    projections_df = parse_projections()
    df = measurements_df.join(projections_df, how='outer').interpolate(method='linear', limit_area='inside')
    print(df.tail(n=25))
    df.plot()
    plt.show(block=True)
