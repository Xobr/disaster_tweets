import typer
import pandas as pd
from sklearn.model_selection import train_test_split


def main(input_file: str, res_dir: str, test_size: float = 0.2):
    df = pd.read_csv(input_file)
    train, test = train_test_split(df, test_size=test_size, random_state=42, stratify=df['target'])
    train.to_csv(res_dir + '/train.csv', index=False)
    test.to_csv(res_dir + '/test.csv', index=False)


if __name__ == '__main__':
    typer.run(main)


