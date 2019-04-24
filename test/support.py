import logging
import os
import sys
import unittest

from seaborn_table.table import SeabornTable

PATH = os.path.split(os.path.abspath(__file__))[0]

log = logging.getLogger(__file__)

logging.basicConfig(level=os.getenv('TEST_LOG_LEVEL', 'INFO'),
                    format="%(message)s",
                    handlers=[logging.StreamHandler(sys.__stdout__)])


class BaseTest(unittest.TestCase):
    maxDiff = None

    def assert_result_file(self, expected_file, result_file, message=None):
        with open(expected_file, 'rb') as fp:
            expected = fp.read().decode('utf-8').replace('\r', '').split('\n')

        with open(result_file, 'rb') as fp:
            result = fp.read().decode('utf-8').replace('\r', '').split('\n')

        for i in range(len(result)):
            print(repr(expected[i]))
            print(repr(result[i]))
            print('\n\n')
            self.assertEqual(expected[i], result[i], message)

    def test_data_path(self, *args):
        path = os.path.join(PATH, 'data', *args)
        if not os.path.exists(os.path.dirname(path)):
            os.mkdir(os.path.dirname(path))
        return path

    def remove_file(self, file):
        os.remove(file)
        if not os.listdir(os.path.dirname(file)):
            os.rmdir(os.path.dirname(file))

    def get_base_table(self):
        return SeabornTable.file_to_obj(
            file_path=self.test_data_path('test_file.rst'))

    @classmethod
    def setUpClass(cls):
        answer = """
        Behave examples table with the following results::
            | #  | column 1 | col2  | column 3 | output column  | output col2
            | 0  | 1        | Hello | a        |                | 1
            | 1  | 2        | Hello | a        |                | 2
            | 2  | 1        | World | a        |                | 1
            | 3  | 2        | World | a        |                | 2
            | 4  | 2        | Hello | b        |                | 2
            | 5  | 1        | World | b        |                | 1
            | 6  | 2        | World | b        |                | 2
            | 7  | 1        | Hello | c        |                | 1
            | 8  | 2        | Hello | c        |                | 2
            | 9  | 1        | World | c        |                | 1
            | 10 | 2        | World | c        |                | 2
        """.split('::')[-1]
        if isinstance(answer, bytes):
            answer = answer.decode('utf8')
        cls.answer = answer.strip().replace('\n            ', '\n')

        def clean(cell):
            cell = cell.strip()
            if cell.replace('.', '').isdigit():
                return eval(cell)
            return cell

        cls.list_of_list = [[clean(r) for r in row.split('|')[1:]]
                            for row in cls.answer.split('\n')]
        cls.list_of_list[0][4] += ' '


class TestFormat(BaseTest):
    def validate_test_condition(self, source):
        raise NotImplemented

    def test_md(self):
        self.validate_test_condition('md')

    def test_csv(self):
        self.validate_test_condition('csv')

    def test_txt(self):
        self.validate_test_condition('txt')

    def test_html(self):
        self.validate_test_condition('html')

    def test_grid(self):
        self.validate_test_condition('grid')

    def test_json(self):
        self.validate_test_condition('json')

    def test_rst(self):
        self.validate_test_condition('rst')

    def test_psql(self):
        self.validate_test_condition('psql')