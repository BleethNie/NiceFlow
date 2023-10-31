import abc
import re
import time
from enum import Enum

import duckdb
from duckdb.typing import DuckDBPyType


class FieldType(Enum):
    BIGINT = 1
    BIT = 2
    BOOLEAN = 3
    BLOB = 3
    DATE = 3

class PluginField(metaclass=abc.ABCMeta):

    def __init__(self):
        self.type = None,
        self.length = 0,
        self.scale = 0,
        self.is_null = None,
        self.is_pk = None,
        self.comment = ""
        self.default_value = None

if __name__ == '__main__':
    a= PluginField()
    print(a)


#
#         BIGINT	INT8, LONG	signed eight-byte integer
# BIT	BITSTRING	string of 1’s and 0’s
# BOOLEAN	BOOL, LOGICAL	logical boolean (true/false)
# BLOB	BYTEA, BINARY, VARBINARY	variable-length binary data
# DATE	 	calendar date (year, month day)
# DOUBLE	FLOAT8, NUMERIC, DECIMAL	double precision floating-point number (8 bytes)
# DECIMAL(prec, scale)	 	fixed-precision number with the given width (precision) and scale
# HUGEINT	 	signed sixteen-byte integer
# INTEGER	INT4, INT, SIGNED	signed four-byte integer
# INTERVAL	 	date / time delta
# REAL	FLOAT4, FLOAT	single precision floating-point number (4 bytes)
# SMALLINT	INT2, SHORT	signed two-byte integer
# TIME	 	time of day (no time zone)
# TIMESTAMP	DATETIME	combination of time and date
# TIMESTAMP WITH TIME ZONE	TIMESTAMPTZ	combination of time and date that uses the current time zone
# TINYINT	INT1	signed one-byte integer
# UBIGINT	 	unsigned eight-byte integer
# UINTEGER	 	unsigned four-byte integer
# USMALLINT	 	unsigned two-byte integer
# UTINYINT	 	unsigned one-byte integer
# UUID	 	UUID data type
# VARCHAR	CHAR, BPCHAR, TEXT, STRING	variable-length character string

