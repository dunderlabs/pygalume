from setuptools import setup, find_packages


long_description = """
Pygalume is a simple python command line utility using the
Vagalume API to search and show songs lyrics.
"""

setup(
    name='Pygalume',
    version='0.2.2',
    description='Pygalume is a simple Python CLI to get lyrics',
    long_description=long_description,
    url='https://github.com/dunderlabs/pygalume',
    author='Dunderlabs Team',
    author_email='dunderlabs@gmail.com',
    maintainer='Dunderlabs Team',
    maintainer_email='dunderlabs@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: System :: Shells',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='pygalume cli lyrics shell vagalume music song',
    download_url='https://pypi.python.org/pypi/Pygalume',
    packages=find_packages(exclude=['tests*']),
    install_requires=['requests>=2.7.0', 'peewee>=2.8.0'],
    scripts=['bin/pygalume'],
    platforms='windows linux',
)
