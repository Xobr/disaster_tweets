import re
import typer
import pandas as pd
from src.text_cleaner import hashtags_regex, mentions_regex

_join_char = ', '


def _remove_char(text: str, char_to_remove: str):
    if char_to_remove and char_to_remove in text:
        return text.replace(char_to_remove, '')
    return text


def _generate_feature(df: pd.DataFrame, text_column: str, regex: str, feature_name: str, char_to_remove: str):
    df[feature_name] = df[text_column].apply(lambda x: _join_char.join(map(lambda s: _remove_char(s, char_to_remove),
                                                                           re.findall(regex, x))))


def feature_engineering(df: pd.DataFrame, text_column: str = 'text'):
    for name, feature, char in [('mentions', mentions_regex, '@'),
                                ('hashtags', hashtags_regex, '#')]:
        _generate_feature(df, text_column, feature, name, char)
    return df


def main(input_file: str, output_file: str, text_column: str = 'text'):
    df = pd.read_csv(input_file)
    df = feature_engineering(df, text_column)
    df.to_csv(output_file, index=False)


if __name__ == '__main__':
    typer.run(main)
