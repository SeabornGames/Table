import unittest

from seaborn_table.table import SeabornTable, UNICODE, BASESTRING
from test.support import BaseTest


class QuoteNumbersTest(BaseTest):
    def quote_number_test(self, source):
        table = self.get_base_table()
        table.map(lambda x: UNICODE(x))
        result_file = self.test_data_path('quote_numbers', 'test_file.%s' % source)
        table.obj_to_file(result_file, quote_numbers=False)
        expected_file = self.test_data_path('expected', 'test_file.%s' % source)
        self.assert_result_file(expected_file, result_file)
        self.remove_file(result_file)

    def test_quote_numbers_md(self):
        self.quote_number_test('md')

    def test_quote_numbers_csv(self):
        self.quote_number_test('csv')

    def test_quote_numbers_txt(self):
        self.quote_number_test('txt')

    def test_quote_numbers_html(self):
        self.quote_number_test('html')

    def test_quote_numbers_grid(self):
        self.quote_number_test('grid')

    def test_quote_numbers_json(self):
        self.quote_number_test('json')

    def test_quote_numbers_rst(self):
        self.quote_number_test('rst')

    def test_quote_numbers_psql(self):
        self.quote_number_test('psql')


class EvalCellsFalseTest(unittest.TestCase):
    def eval_cells_test(self, source):
        file_path = self.test_data_path('test_file.%s' % source)
        table = SeabornTable.file_to_obj(eval_cells=False, file_path=file_path)
        assert isinstance(table[0]['TU'], BASESTRING)

    def test_eval_cells_false_md(self):
        self.eval_cells_test('md')

    def test_eval_cells_false_csv(self):
        self.eval_cells_test('csv')

    def test_eval_cells_false_txt(self):
        self.eval_cells_test('txt')

    # XXX uncomment after implementing html_to_obj
    # def test_eval_cells_false_html(self):
    #     self.eval_cells_test('html')

    def test_eval_cells_false_grid(self):
        self.eval_cells_test('grid')

    def test_eval_cells_false_json(self):
        self.eval_cells_test('json')

    def test_eval_cells_false_rst(self):
        self.eval_cells_test('rst')

    def test_eval_cells_false_psql(self):
        self.eval_cells_test('psql')


class InsertPopRemoveColumnTest(BaseTest):
    def insert_pop_remove_column(self, source):
        table = self.get_base_table()
        table.insert(0, 'remove_column')
        table.insert(None, 'pop_empty_columns')
        table.remove_column('remove_column')
        table.pop_empty_columns()
        result_file = self.test_data_path('column_results',
                                          'test_file.%s' % source)
        table.obj_to_file(result_file)
        expected_file = self.test_data_path('test_file.%s' % source)
        self.assert_result_file(expected_file, result_file)
        self.remove_file(result_file)

    def test_insert_pop_remove_column_md(self):
        self.insert_pop_remove_column('md')

    def test_insert_pop_remove_column_csv(self):
        self.insert_pop_remove_column('csv')

    def test_insert_pop_remove_column_txt(self):
        self.insert_pop_remove_column('txt')

    def test_insert_pop_remove_column_html(self):
        self.insert_pop_remove_column('html')

    def test_insert_pop_remove_column_grid(self):
        self.insert_pop_remove_column('grid')

    def test_insert_pop_remove_column_json(self):
        self.insert_pop_remove_column('json')

    def test_insert_pop_remove_column_rst(self):
        self.insert_pop_remove_column('rst')

    def test_insert_pop_remove_column_psql(self):
        self.insert_pop_remove_column('psql')


class SharedColumnTest(BaseTest):
    SHARED_LIMIT = 0

    def insert_pop_remove_column(self, source):
        tables = [SeabornTable.file_to_obj(
            file_path=self.test_data_path('test_share_columns_%s.rst' % i))
            for i in range(4)]
        for table in tables:
            table.share_column_widths(tables, self.SHARED_LIMIT)
        basename = 'test_share_columns_%s.%s' % (self.SHARED_LIMIT, source)
        expected_file = self.test_data_path('expected', basename)
        result_file = self.test_data_path('shared', basename)
        with open(result_file, 'rb') as fn:
            for table in tables:
                fn.write(table.obj_to_type(source) + b'\n\n')
        self.assert_result_file(expected_file, result_file)
        self.remove_file(result_file)

    def test_share_column_md(self):
        self.share_column('md')

    def test_share_column_csv(self):
        self.share_column('csv')

    def test_share_column_txt(self):
        self.share_column('txt')

    def test_share_column_html(self):
        self.share_column('html')

    def test_share_column_grid(self):
        self.share_column('grid')

    def test_share_column_json(self):
        self.share_column('json')

    def test_share_column_rst(self):
        self.share_column('rst')

    def test_share_column_psql(self):
        self.share_column('psql')


class SharedColumnLimitTest(BaseTest):
    SHARED_LIMIT = 3


if __name__ == '__main__':
    unittest.main()
