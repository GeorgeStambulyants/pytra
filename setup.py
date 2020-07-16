import pathlib
import io
import os
from setuptools import setup, find_packages



HERE = pathlib.PATH(__file__).parent
README = (HERE / 'README.md').read_text()

with io.open(os.path.join(HERE, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [
    req.strip() for req in all_reqs
    if not req.startswith('#')
    and not req.startswith('-')
]

setup(
    name='pytra',
    version='0.1',
    description='Simple command-line tool for translating',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/GeorgeStambulyants/pytra',
    author='GeorgeStambulyants',
    author_email='george.stamb16@gmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    packeges=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'googletrans',
    ],
    python_requires='>=3.7',
    entry_points='''
        [console_scripts]
        pytra=src.pytra:pytra
    '''
)
