import unittest

from seaborn_table.table import SeabornTable, UNICODE, BASESTRING
from test.support import TestFormat


class QuoteNumbersTest(TestFormat):
    def validate_test_condition(self, source):
        table = self.get_base_table()
        table.map(lambda x: UNICODE(x))
        result_file = self.test_data_path('quote_numbers',
                                          'test_quote.%s' % source)
        table.obj_to_file(result_file, quote_numbers=False)
        expected_file = self.test_data_path('expected',
                                            'test_quote.%s' % source)
        self.assert_result_file(expected_file, result_file)
        self.remove_file(result_file)


class EvalCellsFalseTest(TestFormat):
    def validate_test_condition(self, source):
        file_path = self.test_data_path('test_file.%s' % source)
        table = SeabornTable.file_to_obj(eval_cells=False, file_path=file_path)
        assert isinstance(table[0]['TU'], BASESTRING)

    def test_html(self):
        unittest.skip("uncomment after implementing html_to_obj")


class InsertPopRemoveColumnTest(TestFormat):
    def validate_test_condition(self, source):
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


class HeaderOnlyTest(TestFormat):
    def validate_test_condition(self, source):
        expected = SeabornTable(columns=[
            'TEST COL 1', 'TEST COL TWO', 'LAST COL'])
        text = expected.obj_to_type(source)
        result = SeabornTable.type_to_obj(source, text=text)
        expected_file = self.test_data_path('expected', 'header_only.%s'%source)
        result_file = self.test_data_path('header_only',
                                          'header_only.%s' % source)
        expected.obj_to_file(expected_file)
        result.obj_to_file(result_file)
        self.assert_result_file(expected_file, result_file)
        self.remove_file(result_file)
        self.assertEqual(expected, result)

    def test_html(self):
        unittest.skip("uncomment after implementing html_to_obj")


class SharedColumnTest(TestFormat):
    SHARED_LIMIT = 0

    def validate_test_condition(self, source):
        tables = [SeabornTable.file_to_obj(
            file_path=self.test_data_path('test_share_columns_%s.rst' % i))
            for i in range(4)]
        for table in tables:
            table.share_column_widths(tables, self.SHARED_LIMIT)
        basename = 'test_share_columns_%s.%s' % (self.SHARED_LIMIT, source)
        expected_file = self.test_data_path('expected', basename)
        result_file = self.test_data_path('shared', basename)
        with open(result_file, 'w') as fn:
            for table in tables:
                fn.write(table.obj_to_type(source) + '\n\n')
        self.assert_result_file(expected_file, result_file)
        self.remove_file(result_file)


class SharedColumnLimitTest(SharedColumnTest):
    SHARED_LIMIT = 3


if __name__ == '__main__':
    unittest.main()
