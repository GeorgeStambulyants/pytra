import click


def check_file_exists(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            click.echo(f'Can\'t find specified file. Please check its name')

    return wrapper
