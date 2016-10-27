.. image:: https://badge.waffle.io/indacode/pygalume.svg?label=ready&title=Ready
   :height: 18px
   :width: 70px
   :alt: Stories in Ready
   :align: left

========
pygalume
========

A simple python command line utility using the Vagalume API to search and show songs lyrics.

.. image:: http://i.imgur.com/q4S2vw8.jpg
   :height: 524px
   :width: 582px
   :alt: Usage
   :align: center


Installing
----------

Via pip

.. code-block:: bash

    $ pip install pygalume


Clone this project and install via setup.py

.. code-block:: bash

    $ git clone git@github.com:dunderlabs/pygalume.git
    $ cd pygalume/
    $ python setup.py install


Usage example
-------------

Here you can see pygalume in action. How to get a lyric from your favorite artist?

  Pygalume works offline for those lyrics you had already searched for.
 
Note: if the artist's name or music have more than one word, wrap it with double quotes.

.. code-block:: bash

    $ pygalume -a Sia -m "Bird set free"


How to get the discography?

.. code-block:: bash

    $ pygalume -a Sia -d


How to get songs name from an album?

.. code-block:: bash

    $ pygalume -a Sia --al "This Is Acting"


How to list all songs in cache?

.. code-block:: bash

    $ pygalume --lc # or
    $ pygalume --list-cache


How to clear all songs in cache?

.. code-block:: bash

    $ pygalume --cc # or
    $ pygalume --clear-cache


Development
-------------

Running unit tests:

.. code-block:: bash

    $ python setup.py test
