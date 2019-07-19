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
