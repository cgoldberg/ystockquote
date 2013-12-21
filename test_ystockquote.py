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
#  Requires: Python 2.7/3.3+


import unittest

import pep8
from testscenarios import generate_scenarios, TestWithScenarios

import ystockquote


class Pep8ConformanceTestCase(unittest.TestCase):
    """Test that all code conforms to PEP8!"""

    def test_pep8_conformance(self):
        self.pep8style = pep8.StyleGuide(show_source=True)
        files = ('ystockquote.py', 'test_ystockquote.py')
        self.pep8style.check_files(files)
        self.assertEqual(self.pep8style.options.report.total_errors, 0)


class YStockQuoteTestCase(TestWithScenarios):

    def test_get_all(self):
        symbol = 'GOOG'
        all_info = ystockquote.get_all(symbol)
        self.assertIsInstance(all_info, dict)
        pc = all_info['previous_close']
        self.assertNotEqual(pc, 'N/A')
        self.assertGreater(float(pc), 0)

    def test_get_historical_prices(self):
        symbol = 'GOOG'
        start_date = '2013-01-02'
        end_date = '2013-01-15'
        prices = ystockquote.get_historical_prices(
            symbol, start_date, end_date)
        self.assertIsInstance(prices, dict)
        self.assertEqual(len(prices), 10)
        self.assertEqual(sorted(prices.keys())[0], '2013-01-02')
        self.assertEqual(sorted(prices.keys())[-1], end_date)
        self.assertGreater(float(prices[start_date]['Open']), 0.0)
        self.assertGreater(float(prices[start_date]['High']), 0.0)
        self.assertGreater(float(prices[start_date]['Low']), 0.0)
        self.assertGreater(float(prices[start_date]['Close']), 0.0)
        self.assertGreater(float(prices[start_date]['Volume']), 0.0)
        self.assertGreater(float(prices[start_date]['Adj Close']), 0.0)
        self.assertGreater(float(prices[end_date]['Open']), 0.0)
        self.assertGreater(float(prices[end_date]['High']), 0.0)
        self.assertGreater(float(prices[end_date]['Low']), 0.0)
        self.assertGreater(float(prices[end_date]['Close']), 0.0)
        self.assertGreater(float(prices[end_date]['Volume']), 0.0)
        self.assertGreater(float(prices[end_date]['Adj Close']), 0.0)


if __name__ == '__main__':
    unittest.main()
