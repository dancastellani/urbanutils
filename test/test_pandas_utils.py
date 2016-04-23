from unittest import TestCase

import pandas
from pandas.util.testing import assert_frame_equal

from urban_utils import pandas_utils


class TestPandasUtils(TestCase):
    def runTest(self):
        first_series = pandas.Series({'a': 1, 'b': 1})
        second_series = pandas.Series({'b': 1, 'c': 1})

        merged = pandas_utils.merge_series_summing_values(first_series, second_series)

        expected = pandas.Series({'a': 1, 'b': 2, 'c': 1})

        self.assertTrue(merged.equals(expected))
