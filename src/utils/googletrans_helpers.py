import click
from googletrans import LANGCODES


def print_all_language_codes():
    for (lang, code) in LANGCODES.items():
        click.echo(f'{lang} -- "{code}"')
