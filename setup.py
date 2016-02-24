from setuptools import setup, find_packages


long_description = """
A simple python command line utility using the
Vagalume API to search and show songs lyrics.
"""

setup(
    name='Pygalume',
    version='0.1.2',
    description='A simple CLI Python to get lyrics',
    long_description=long_description,
    url='https://github.com/dunderlabs/pygalume',
    author='Dunderlabs Team',
    author_email='dunderlabs@gmail.com',
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
    keywords='cli lyrics shell',
    packages=find_packages(exclude=['tests*']),
    install_requires=['requests>=2.7.0', 'SQLAlchemy>=1.0.8'],
    scripts=['bin/pygalume'],
)
