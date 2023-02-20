import typer
import pandas as pd

_rows_to_merge = ['text_cleaned', 'keyword', 'location', 'mentions', 'hashtags']


def add_bert_text(df: pd.DataFrame, bert_column: str = 'text_bert'):
    df[bert_column] = df.apply(lambda row: ' [SEP] '.join((row[r] for r in _rows_to_merge if not pd.isna(row[r]))), axis=1)
    return df


def main(input_file: str, output_file: str, bert_column: str = 'text_bert'):
    df = pd.read_csv(input_file)
    df = add_bert_text(df, bert_column)
    df.to_csv(output_file, index=False)


if __name__ == '__main__':
    typer.run(main)
