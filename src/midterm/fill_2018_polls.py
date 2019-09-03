import pandas as pd
import json
from pandas.io.json import json_normalize
import state_abbrev

def load_polls():
    nested = json.load(open('../data/fivethirtyeight-polls.json'))
    df = json_normalize(nested)
    #october 16, 2018 - november 6, 2018
    df['endDate'] = pd.to_datetime(df['endDate'])
    print(df)
    mask = (df['endDate'] >= '10-16-2018') & (df['endDate'] <= '11-6-2018')
    df = df.loc[mask]
    df = df.query("(type == 'house' or type == 'senate') or (type == 'governor')")
    df.to_csv('../out/testpolls.csv')
