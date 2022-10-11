Changes in 6.7.1
================

* ``psql_to_obj`` now assumes the number of columns equal to the header.
  If a column could have the `` | `` deliminator then the safest thing to do
  would be to make it the last column.  If multiple columns could have the
  `` | ``, then it will need to be fixed before hand.  This feature can be
  turned off with option ``assume_header`` = False.


Changes in 6.7.0
================

* Header cells within and HTML table will be marked with ``th`` instead of
  ``td``.

* Empty cells will be marked with ``<td/>`` instead of ``<td></td>``.


Changes in 6.6.0
================

* Added ``rename_column`` method for renaming column.


Changes in 6.5.0
================

* Added ``transpose`` method to transpose the table.

* Added argument ``--limit`` and ``--offset`` to reduce rows.

* Added argument ``--transpose`` to transpose the table.

* Added argument ``--column-key`` to key table before transposing.

* Added argument ``key-only`` to reduce rows to certain keys within
  --column-key.

* Added ``--print`` option to only print the table to the screen.

* Fixed bug in list_to_obj where columns is specified.


Changes in 6.4.0
================

* Added capability of handling yaml.


Changes in 6.3.0
================

* Added a feature of setup_live_table; which will write to a file or screen
  every time a row is added.

* Updated Exception types to specify the type of error.

* MIN_WIDTH and MAX_WIDTH can now be set at the class level.

* max_width, width, clip_width, and slice have now been added to all obj_to_*.


Changes in 6.2.0
================

* Replaced manual parsing args with ArgumentParser.

* Added ``--column`` command line argument to specify the new columns.

* Added ``--order-by`` command line argument to specify how to sort the rows.


Changes in 6.1.0
================

* Added ``break_line`` argument to obj_to_md, obj_to_str, obj_to_rst,
  obj_to_psql, obj_to_grid methods which will insert a new row
  whenever a cell has a line break in it.  A table created with break_line,
  is not reverseable, which means the table cannot be read back in.


Changes in 6.0.1
================

* Fixed bug in SeabornRow.dict_to_obj.


Changes in 6.0.0
================

* Added ``align`` with values left, right, center, none to align cells.

* Replaced ``space_columns`` in obj_to_csv with ``align``.

* Added validate option to SeabornTable to skip validating.


Changes in 5.1.0
================

* SeabornRow is now a member of SeabornTable to make subclassing easier.

* Added method ``add`` to SeabornTable for append a new row using **kwargs.

* Added method ``dict_to_obj`` to SeabornRow.


Changes in 5.0.0
================

* ``__getitem__`` changed to only treat the table as a list.  Use the get method
  to treat it as a dictionary.
    - This is a breaking change.

* Added method ``setdefault`` which treats the table as a dictionary.

* The method ``keys`` now returns the proper keys if column_key is set.
    - This is a breaking change because keys was returning columns

* Added method ``items`` which requires column_key to be set.


Changes in 4.1.0
================

* txt_to_obj and str_to_obj default deliminator to \t but after parsing.


Changes in 4.0.0
================

* Added the concept of column_key which will key the table on a single column.
  This uses a hash instead of key_on's search feature, so it fast but it also
  static as it needs ``update_column_key_values`` to be called if the key or
  rows change.

* Update all of the *_to_obj functions to use kwargs for standard __init__
  variables.  This causes argument order to change which is the breaking change.

* Added __iter__ method.

* Added get method that uses column_key.


Changes in 3.3.0
================

* added argument ``quote_texts`` to obj_to_str and obj_to_txt.


Changes in 3.2.2
================

* Added pad_last_column to obj_to_str.


Changes in 3.2.1
================

* Fixed bug with obj_to_str not quoting string with space within the cell.


Changes in 3.2.0
================

* Added slice capability to SeabornRow and SeabornTable.


Changes in 3.1.0
================

* Added argument of ``string_comparison`` to sort_by_key incase the types match.


Changes in 3.0.2
================

* Fixed bug with ``get_column`` when referencing column index.


Changes in 3.0.1
================

* Fixed bug with shared column widths when using default shared_limit.


Changes in 3.0.0
================

* Added pop_empty_columns method for removing from displayed columns if the
  column is only '' or None.

* Fixed a bug with popping column.

* Reordered some of the method args to make the calls more consistent.

* Fixed extra space in psql columns.

* Added a share column widths method to sync the widths between two tables.

* Dropped backwards compatibility for seaborn/seaborn_table.py

* list_to_obj and all type_to_obj assume first row is the header.


Changes in 2.3.0
================

* Added quote_empty_str option to obj_to_str or obj_to_txt.


Changes in 2.2.0
================

* Added file format psql.

* Added file format rst.

* Added known format as ``KNOWN_FORMATS``.

* Added ability to force writing strings of numbers and bools without quotes,
  through the ``quote_numbers`` argument.

* Added ability to not evaluate numbers and bools without quotes upon read,
  through the ``eval_cells`` argument.


Changes in 2.1.0
================

* file_to_obj now accepts the key_on argument.

* file_to_obj and obj_to_file now handles 'json' file extension.

* fixed reference when calling seaborn_table as a entry point.


Changes in 2.0.0
================

* PIP library somehow got an older version (1.3.3), so we are starting fresh
  with a major bump.

* import from seaborn_table.__init__ now works.


Changes in 1.3.2
================

* Added fancy grid option


Changes in 1.3.1
================

* Reorganized code to table.table structure


Changes in 1.3.0
================

* Reorganized code and made function private

* Added column_index for faster lookup

* Normalized to unicode bases for py2 and py3
