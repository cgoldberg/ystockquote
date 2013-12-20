ystockquote
===========

**Python module - retrieve stock quote data from Yahoo Finance**

 * Created by: Corey Goldberg (2007,2008,2013)
 * License: GNU LGPLv2+
 * Dev Home: `https://github.com/cgoldberg/ystockquote <https://github.com/cgoldberg/ystockquote>`_
 * PyPI: `https://pypi.python.org/pypi/ystockquote <https://pypi.python.org/pypi/ystockquote>`_

----

~~~~~~~~~~~~
Requirements
~~~~~~~~~~~~

  * Python 2.7/3.3+

~~~~~~~
Install
~~~~~~~

`ytockquote` can be installed from `PyPI <https://pypi.python.org/pypi/ystockquote>`_ with `pip <http://www.pip-installer.org/>`_::

    $ pip install ystockquote

You can also clone the development repo (requires `git <http://git-scm.com/>`_) to install::

    $ git clone git://github.com/cgoldberg/ystockquote.git
    $ cd ystockquote
    $ python setup.py install
    $ python -m unittest discover

To run unit tests::

    $ python -m unittest discover

~~~~~~~~~~~~~
Example Usage
~~~~~~~~~~~~~

.. code:: python

    >>> import ystockquote
    >>> print(ystockquote.get_price_book('GOOG'))
    '51.18'
    >>> print(ystockquote.get_bid_realtime('GOOG'))
    '904.77'
    >>>

.. code:: python

    >>> import ystockquote
    >>> from pprint import pprint
    >>> pprint(ystockquote.get_historical_prices('GOOG', '2013-01-03', '2013-01-08'))
    {'2013-01-03': {'Adj Close': '723.67',
                    'Close': '723.67',
                    'High': '731.93',
                    'Low': '720.72',
                    'Open': '724.93',
                    'Volume': '2318200'},
     '2013-01-04': {'Adj Close': '737.97',
                    'Close': '737.97',
                    'High': '741.47',
                    'Low': '727.68',
                    'Open': '729.34',
                    'Volume': '2763500'},
     '2013-01-07': {'Adj Close': '734.75',
                    'Close': '734.75',
                    'High': '739.38',
                    'Low': '730.58',
                    'Open': '735.45',
                    'Volume': '1655700'},
     '2013-01-08': {'Adj Close': '733.30',
                    'Close': '733.30',
                    'High': '736.30',
                    'Low': '724.43',
                    'Open': '735.54',
                    'Volume': '1676100'}}
    >>>

