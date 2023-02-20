import pandas as pn


def remove_duplicates(df: pn.DataFrame):
    df_cleaned = df.groupby('text_cleaned').agg({
        'id': 'first',
        'keyword': 'first',
        'location': 'first',
        'text': 'first',
        'text_cleaned': 'first',
        'target': 'mean'
    })

    df_cleaned = df_cleaned[(df_cleaned['target'] < 0.49) | (df_cleaned['target'] > 0.51)]
    df_cleaned['target'] = round(df_cleaned['target'])

    return df_cleaned

