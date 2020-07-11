import click
from googletrans import Translator, LANGCODES

from .decorators import (
    check_file_exists,
    language_code_is_correct,
    language_name_is_correct,
)


translator = Translator()


@language_code_is_correct
def get_translated_text(trans_from, trans_to, origin_text):
    translated_obj = translator.translate(
        text=origin_text,
        origin=trans_from,
        dest=trans_to,
    )
    return translated_obj.text


def get_detected_language_obj(sentence):
    return translator.detect(sentence)


@language_code_is_correct
@check_file_exists
def create_translated_file(output_file_name, file_to_translate, translate_to):
    with open(output_file_name, 'w') as translated_file:
        with open(file_to_translate, 'r') as original_file:
            for line in original_file:
                translated_line = translator.translate(
                    text=line,
                    dest=translate_to,
                ).text
                translated_file.write(translated_line + '\n')


@check_file_exists
def get_detected_file_language_obj(file):
    with open(file, 'r') as f:
        first_line = f.readline()
        return translator.detect(first_line)


@language_name_is_correct
def print_language_code(language):
    language = language.strip().lower()
    click.echo(f'{language} -- "{LANGCODES[language]}"')


def print_all_language_codes():
    for (lang, code) in LANGCODES.items():
        click.echo(f'{lang} -- "{code}"')
