try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'PWL Maker',
    'author': 'Louis Simons',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'lousimons@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['pwl_maker'],
    'scripts': [],
    'name': 'pwl_maker'
}

setup(**config)