import unittest

from seaborn_table.table import main as cli_converter
from test.support import BaseTest, FormatMixin


class FileConversionMixin(FormatMixin):
    def validate_test_condition(self, source):
        dest = self.DEST
        source_file = self.test_data_path('test_file.%s' % source)
        expected_file = self.test_data_path('test_file.%s' % dest)
        result_file = self.test_data_path('_%s' % source, 'test_file.%s' % dest)
        cli_converter([source_file, result_file])
        self.assert_result_file(expected_file, result_file,
                                "Failure converting %s into %s" % (
                                    source, dest))
        self.remove_file(result_file)

    def test_html(self):
        raise unittest.SkipTest("reading html has not been implemented")


class FileConversionTestTxt(BaseTest, FileConversionMixin):
    DEST = 'txt'


class FileConversionTestCsv(BaseTest, FileConversionMixin):
    DEST = 'csv'


class FileConversionTestMd(BaseTest, FileConversionMixin):
    DEST = 'md'


class FileConversionTestHtml(BaseTest, FileConversionMixin):
    DEST = 'html'


class FileConversionTestGrid(BaseTest, FileConversionMixin):
    DEST = 'grid'


class FileConversionTestJson(BaseTest, FileConversionMixin):
    DEST = 'json'


class FileConversionTestRst(BaseTest, FileConversionMixin):
    DEST = 'rst'


class FileConversionTestPsql(BaseTest, FileConversionMixin):
    DEST = 'psql'


class ParseArgsTest(BaseTest):
    def validate_test_condition(self, name, source, dest, *columns):
        source_file = self.test_data_path('test_file.%s' % source)
        expected_file = self.test_data_path('expected', '%s.%s' % (name, dest))
        result_file = self.test_data_path('_parse_args', '%s.%s' % (name, dest))
        cli_converter([source_file, result_file] + list(columns))
        self.assert_result_file(expected_file, result_file,
                                "Failure converting %s into %s" % (
                                    source, dest))
        self.remove_file(result_file)

    def test_reorder_columns(self):
        self.validate_test_condition('test_reorder_columns', 'txt', 'grid',
                                     '--columns', 'Target', 'Action', 'Role',
                                     'Player', 'TU')

    def test_remove_columns(self):
        self.validate_test_condition('test_remove_columns', 'json', 'psql',
                                     '--columns', 'TU', 'Player', 'Action')

    def test_add_columns(self):
        self.validate_test_condition('test_add_columns', 'csv', 'md',
                                     '--columns', 'TU', 'Addition1', 'Player',
                                     'Action', 'Role', 'Player', 'TU',
                                     'Addition2')

    def test_reorder_rows(self):
        self.validate_test_condition('test_reorder_rows', 'csv', 'md',
                                     '--order-by', 'TU', 'Role')

    def test_reorder_rows_reverse(self):
        self.validate_test_condition('test_reorder_rows_reverse', 'csv', 'md',
                                     '--order-by', '~Player', 'Target')


class MergeTest(BaseTest):
    def test_merge_tables(self):
        source_file = self.test_data_path('test_file.csv')
        expected_file = self.test_data_path('expected', 'merge_file.md')
        result_file = self.test_data_path('_merge_files', 'merge_file.md')
        merge_file1 = self.test_data_path('merge_file1.psql')
        merge_file2 = self.test_data_path('merge_file2.rst')
        cli_converter([source_file, result_file, '--merge-file',
                       merge_file1, merge_file2])
        self.assert_result_file(expected_file, result_file,
                                'Failure merging %s with %s and %s in %s'%(
                                source_file, merge_file1, merge_file2,
                                result_file))


if __name__ == '__main__':
    unittest.main()
