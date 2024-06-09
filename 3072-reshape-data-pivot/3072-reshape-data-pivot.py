import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    df = pd.pivot_table(weather, index='month', values='temperature', columns=['city'])
    return df
    