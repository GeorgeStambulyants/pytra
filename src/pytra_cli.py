import click
from googletrans import LANGUAGES

from utils.translator import (
    get_translated_text,
    get_detected_language_obj
)


@click.group()
def pytra():
    pass


@pytra.command()
@click.option('-f', '--translate_from', default='auto')
@click.option('-t', '--translate_to', default='en')
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


@pytra.command()
@click.argument('sentence')
def detect(sentence):
    detected_language_obj = get_detected_language_obj(sentence)
    detected_language = detected_language_obj.lang
    detected_language_confidence = detected_language_obj.confidence
    click.echo(
        f'"{LANGUAGES[detected_language].title()}" was detected with '
        f'{detected_language_confidence} confidence'
    )


if __name__ == '__main__':
    pytra()
