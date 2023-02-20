import typer
import pandas as pn
from src.text_cleaner import clean_text
from src.remove_duplicates import remove_duplicates


def main(input_file: str,
         output_file: str,
         text_column: str = 'text',
         result_column: str = 'text_cleaned',
         need_remove_duplicates: bool = True):
    df = pn.read_csv(input_file)
    df[result_column] = df[text_column].apply(clean_text)
    if need_remove_duplicates:
        df = remove_duplicates(df)
    df.to_csv(output_file, index=False)


if __name__ == '__main__':
    typer.run(main)

