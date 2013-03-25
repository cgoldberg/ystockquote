ystockquote
===========

**Python module - retrieve stock quote data from Yahoo Finance.**

 * created by: Corey Goldberg (2007,2008,2013)
 * license: GNU LGPLv2+

----

~~~~~~~~~~~~
Requirements
~~~~~~~~~~~~

 * Python 2.7/3.2+

~~~~~~~
Install
~~~~~~~


`ytockquote` can be installed from `PyPI` with :code:`pip`::

    pip install ystockquote

You can also clone the development repo and install (requires `git` and runs unit-tests)::

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
    '810.31'

.. code:: python


    >>> import ystockquote
    >>> import pprint
    >>> pprint.pprint(ystockquote.get_historical_prices('GOOG', '20130103', '20130108'))
    [['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close'],
     ['2013-01-08', '735.54', '736.30', '724.43', '733.30', '1676100', '733.30'],
     ['2013-01-07', '735.45', '739.38', '730.58', '734.75', '1655700', '734.75'],
     ['2013-01-04', '729.34', '741.47', '727.68', '737.97', '2763500', '737.97'],
     ['2013-01-03', '724.93', '731.93', '720.72', '723.67', '2318200', '723.67']]
    >>>

.. code:: python

    >>> import ystockquote
    >>> import pprint
    >>> pprint.pprint(ystockquote.get_all('GOOG'))
    {'avg_daily_volume': '2311630',
     'book_value': '217.332',
     'change': '0.00',
     'dividend_per_share': '0.00',
     'dividend_yield': 'N/A',
     'earnings_per_share': '32.214',
     'ebitda': '16.278B',
     'fifty_day_moving_avg': '802.107',
     'fifty_two_week_high': '844.00',
     'fifty_two_week_low': '556.52',
     'market_cap': '267.1B',
     'price': '810.31',
     'price_book_ratio': '3.73',
     'price_earnings_growth_ratio': '1.26',
     'price_earnings_ratio': '25.15',
     'price_sales_ratio': '5.32',
     'short_ratio': '1.90',
     'stock_exchange': '"NasdaqNM"',
     'two_hundred_day_moving_avg': '733.759',
     'volume': '3772'}
    >>> 
