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
        p = all_info['dividend_yield']
        self.assertIsInstance(p, str)

    def test_get_historical_prices(self):
        prices_dict = ystockquote.get_historical_prices(
            self.symbol, '2013-01-02', '2013-01-15')
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


if __name__ == '__main__':
    unittest.main()
