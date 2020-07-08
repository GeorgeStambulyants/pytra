import click


@click.command()
@click.option('-f', '--translate_from', default='auto')
@click.option('-t', '--translate_to', default='en')
def pytra(translate_from, translate_to):
    click.echo(f'Translate from: {translate_from}, Translate to: {translate_to}')


if __name__ == '__main__':
    pytra()
