import click

from utils.translator import get_translated_text


@click.command()
@click.option('-f', '--translate_from', default='auto')
@click.option('-t', '--translate_to', default='en')
@click.argument('origin_text')
def pytra(translate_from, translate_to, origin_text):
    translated_text = get_translated_text(
        translate_from,
        translate_to,
        origin_text,
    )

    click.echo(translated_text)


if __name__ == '__main__':
    pytra()
