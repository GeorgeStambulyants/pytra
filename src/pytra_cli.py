import click
from googletrans import Translator


translator = Translator()


@click.command()
@click.option('-f', '--translate_from', default='auto')
@click.option('-t', '--translate_to', default='en')
@click.argument('origin_text')
def pytra(translate_from, translate_to, origin_text):
    translated_obj = translator.translate(
        text=origin_text,
        origin=translate_from,
        dest=translate_to,
    )
    translated_text = translated_obj.text

    click.echo(translated_text)


if __name__ == '__main__':
    pytra()
