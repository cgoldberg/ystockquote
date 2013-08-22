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

  * Python 2.7/3.2+

~~~~~~~
Install
~~~~~~~

`ytockquote` can be installed from `PyPI <https://pypi.python.org/pypi/ystockquote>`_ with `pip <http://www.pip-installer.org/>`_::

    $ pip install ystockquote

You can also clone the development repo (requires `git <http://git-scm.com/>`_) to install and run unit-tests::

    $ git clone git://github.com/cgoldberg/ystockquote.git
    $ cd ystockquote
    $ python setup.py install
    $ python -m unittest discover

~~~~~~~~~~~~~
Example Usage
~~~~~~~~~~~~~

.. code:: python

    >>> import ystockquote
    >>> ystockquote.get_price('GOOG')
    '869.33'
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


.. code:: python

    >>> import ystockquote
    >>> from pprint import pprint
    >>> pprint(ystockquote.get_all('GOOG'))
    {'avg_daily_volume': '2178170',
     'book_value': '236.698',
     'change': '0.00',
     'dividend_per_share': '0.00',
     'dividend_yield': 'N/A',
     'earnings_per_share': '34.565',
     'ebitda': '17.004B',
     'fifty_day_moving_avg': '894.304',
     'fifty_two_week_high': '928.00',
     'fifty_two_week_low': '636.00',
     'market_cap': '289.5B',
     'price': '869.33',
     'price_book_ratio': '3.67',
     'price_earnings_growth_ratio': '1.37',
     'price_earnings_ratio': '25.15',
     'price_sales_ratio': '5.19',
     'short_ratio': '1.70',
     'stock_exchange': '"NasdaqNM"',
     'two_hundred_day_moving_avg': '848.489',
     'volume': '3800'}
    >>> 


 
