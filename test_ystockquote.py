#!/usr/bin/env python
#
#  Copyright (c) 2013, Corey Goldberg (cgoldberg@gmail.com)
#
#  license: GNU LGPL
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License, or (at your option) any later version.
#
#  Requires: Python 2.7/3.2+


import unittest

import pep8

import ystockquote


class Pep8ConformanceTestCase(unittest.TestCase):
    """Test that all code conforms to PEP8."""

    def test_pep8_conformance(self):
        self.pep8style = pep8.StyleGuide(show_source=True)
        files = ('ystockquote.py', 'test_ystockquote.py')
        self.pep8style.check_files(files)
        self.assertEqual(self.pep8style.options.report.total_errors, 0)


class YStockQuoteTestCase(unittest.TestCase):

    def setUp(self):
        self.symbol = 'GOOG'

    def test_get_all(self):
        all_info = ystockquote.get_all(self.symbol)
        self.assertIsInstance(all_info, dict)
        p = all_info['price']
        self.assertIsInstance(p, str)
        self.assertGreater(float(p), 0.0)

    def test_get_historical_prices(self):
        prices = ystockquote.get_historical_prices(
            self.symbol, '2013-01-02', '2013-01-15'
        )
        self.assertIsInstance(prices, list)
        headers = [
            'Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close'
        ]
        self.assertEqual(len(prices), 11)
        self.assertEqual(prices[0], headers)
        self.assertEqual(prices[1][0], '2013-01-15')
        self.assertEqual(prices[-1][0], '2013-01-02')
        self.assertGreater(float(prices[1][6]), 0.0)
        self.assertGreater(float(prices[-1][6]), 0.0)

    def test_get_historical_prices_dict(self):
        prices_dict = ystockquote.get_historical_prices_dict(
            self.symbol, '2013-01-02', '2013-01-15'
        )
        self.assertIsInstance(prices_dict, dict)
        self.assertEqual(len(prices_dict), 10)
        self.assertEqual(sorted(prices_dict.keys())[0], '2013-01-02')
        self.assertEqual(sorted(prices_dict.keys())[-1], '2013-01-15')
        self.assertGreater(float(prices_dict['2013-01-02']['Open']), 0.0)
        self.assertGreater(float(prices_dict['2013-01-02']['High']), 0.0)
        self.assertGreater(float(prices_dict['2013-01-02']['Low']), 0.0)
        self.assertGreater(float(prices_dict['2013-01-02']['Close']), 0.0)
        self.assertGreater(float(prices_dict['2013-01-02']['Volume']), 0.0)
        self.assertGreater(float(prices_dict['2013-01-02']['Adj Close']), 0.0)
        self.assertGreater(float(prices_dict['2013-01-15']['Open']), 0.0)
        self.assertGreater(float(prices_dict['2013-01-15']['High']), 0.0)
        self.assertGreater(float(prices_dict['2013-01-15']['Low']), 0.0)
        self.assertGreater(float(prices_dict['2013-01-15']['Close']), 0.0)
        self.assertGreater(float(prices_dict['2013-01-15']['Volume']), 0.0)
        self.assertGreater(float(prices_dict['2013-01-15']['Adj Close']), 0.0)

    def test_get_price(self):
        value = ystockquote.get_price(self.symbol)
        self.assertIsInstance(value, str)

    def test_get_change(self):
        value = ystockquote.get_change(self.symbol)
        self.assertIsInstance(value, str)

    def test_get_volume(self):
        value = ystockquote.get_volume(self.symbol)
        self.assertIsInstance(value, str)

    def test_get_avg_daily_volume(self):
        value = ystockquote.get_avg_daily_volume(self.symbol)
        self.assertIsInstance(value, str)

    def test_get_stock_exchange(self):
        value = ystockquote.get_stock_exchange(self.symbol)
        self.assertIsInstance(value, str)

    def test_get_market_cap(self):
        value = ystockquote.get_market_cap(self.symbol)
        self.assertIsInstance(value, str)

    def test_get_book_value(self):
        value = ystockquote.get_book_value(self.symbol)
        self.assertIsInstance(value, str)

    def test_get_ebitda(self):
        value = ystockquote.get_ebitda(self.symbol)
        self.assertIsInstance(value, str)

    def test_get_dividend_per_share(self):
        value = ystockquote.get_dividend_per_share(self.symbol)
        self.assertIsInstance(value, str)

    def test_get_dividend_yield(self):
        value = ystockquote.get_dividend_yield(self.symbol)
        self.assertIsInstance(value, str)

    def test_get_earnings_per_share(self):
        value = ystockquote.get_earnings_per_share(self.symbol)
        self.assertIsInstance(value, str)

    def test_get_52_week_high(self):
        value = ystockquote.get_52_week_high(self.symbol)
        self.assertIsInstance(value, str)

    def test_get_52_week_low(self):
        value = ystockquote.get_52_week_low(self.symbol)
        self.assertIsInstance(value, str)

    def test_get_50day_moving_avg(self):
        value = ystockquote.get_50day_moving_avg(self.symbol)
        self.assertIsInstance(value, str)

    def test_get_200day_moving_avg(self):
        value = ystockquote.get_200day_moving_avg(self.symbol)
        self.assertIsInstance(value, str)

    def test_get_price_earnings_ratio(self):
        value = ystockquote.get_price_earnings_ratio(self.symbol)
        self.assertIsInstance(value, str)

    def test_get_price_earnings_growth_ratio(self):
        value = ystockquote.get_price_earnings_growth_ratio(self.symbol)
        self.assertIsInstance(value, str)

    def test_get_price_sales_ratio(self):
        value = ystockquote.get_price_sales_ratio(self.symbol)
        self.assertIsInstance(value, str)

    def test_get_price_book_ratio(self):
        value = ystockquote.get_price_book_ratio(self.symbol)
        self.assertIsInstance(value, str)

    def test_get_short_ratio(self):
        value = ystockquote.get_short_ratio(self.symbol)
        self.assertIsInstance(value, str)


if __name__ == '__main__':
    unittest.main()
