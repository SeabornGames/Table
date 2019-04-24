import os
import unittest

from seaborn_table.table import SeabornTable

PATH = os.path.split(os.path.abspath(__file__))[0]


class BaseTest(unittest.TestCase):
    file_path = self.test_data_path('test_file.rst')

    def assert_file_equal(self, expected_file, result_file, message):
        with open(expected_file, 'rb') as fp:
            expected = fp.read().decode('utf-8').replace('\r', '').split('\n')

        with open(result_file, 'rb') as fp:
            result = fp.read().decode('utf-8').replace('\r', '').split('\n')

        for i in range(len(result)):
            self.assertEqual(expected[i], result[i], message)

    def test_data_path(self, *args):
        path = os.path.join(PATH, 'data', *args)
        if not os.path.exists(os.path.basename(path)):
            os.mkdir(os.path.basename(path))

    def remove_file(self, file):
        os.remove(file)
        if not os.listdir(os.path.dirname(file)):
            os.rmdir(os.path.dirname(file))

    def get_base_table(self):
        return SeabornTable.file_to_obj(
            file_path=self.test_data_path('test_file.rst'))
