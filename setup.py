from setuptools import setup

setup(
    name='mandible',
    version='0.5',
    py_modules=['mandible'],
    install_requires=[
        'Click',
        'colorama'
    ],
    entry_points='''
        [console_scripts]
        mandible=mandible:cli
    ''',

    # metadata
    author="Varun Jawarani",
    author_email="vjawarani@gmail.com",
    description="Mandible is designed to improve efficiency in removal of file types from certain locations",
    keywords="remove efficiency specific files",
    url="https://github.com/vjawarani/mandible",
)