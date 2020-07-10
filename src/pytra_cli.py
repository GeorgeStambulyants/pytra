import click
from googletrans import LANGCODES, LANGUAGES

from utils.translator import (
    get_translated_text,
    get_detected_language_obj
)
from utils.constants import (
    TRANSLATE_FROM_HELP,
    TRANSLATE_TO_HELP,
    SHOW_LANGUAGE_CODES_HELP,
    TRANSLATE_HELP,
    DETECT_HELP
)


@click.group()
def pytra():
    pass


@pytra.command(help=TRANSLATE_HELP)
@click.option('-f', '--translate_from', default='auto', help=TRANSLATE_FROM_HELP)
@click.option('-t', '--translate_to', default='en', help=TRANSLATE_TO_HELP)
@click.argument('origin_text')
def translate(translate_from, translate_to, origin_text):
    try:
        translated_text = get_translated_text(
            translate_from,
            translate_to,
            origin_text,
        )
        click.echo(translated_text)
    except ValueError as e:
        click.echo(f'Got an exception: {e}')


@pytra.command(help=DETECT_HELP)
@click.argument('sentence')
def detect(sentence):
    detected_language_obj = get_detected_language_obj(sentence)
    detected_language = detected_language_obj.lang
    detected_language_confidence = detected_language_obj.confidence
    click.echo(
        f'"{LANGUAGES[detected_language].title()}" was detected with '
        f'{detected_language_confidence} confidence'
    )


@pytra.command(help=SHOW_LANGUAGE_CODES_HELP)
@click.argument('language', required=False)
def show_language_codes(language):
    if language:
        language = language.strip().lower()
        try:
            click.echo(f'{language} -- "{LANGCODES[language]}"')
        except KeyError:
            click.echo(f'Incorrect language')
    else:
        for (lang, code) in LANGCODES.items():
            click.echo(f'{lang} -- "{code}"')


if __name__ == '__main__':
    pytra()
