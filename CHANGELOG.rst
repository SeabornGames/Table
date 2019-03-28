Changes in 2.2.0
================

* Added file format psql.

* Added file format rst.

* Added known format as ``KNOWN_FORMATS``.


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
