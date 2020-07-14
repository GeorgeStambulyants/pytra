from setuptools import setup


setup(
    name='pytra_cli',
    version='0.1',
    py_modules=['pytra_cli'],
    install_requires=[
        'click',
        'googletrans',
    ],
    entry_points='''
        [console_scripts]
        pytra_cli=pytra_cli:pytra
    '''
)
