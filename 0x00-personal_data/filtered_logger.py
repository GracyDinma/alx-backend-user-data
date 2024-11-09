#!/usr/bin/env python3i
"""Use of regex in replacing occurences of certain field values."""
import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Returns filtered values from log records."""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self, self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Returns regex obfuscated log messages."""
    return re.sub(rf"({'|'.join(fields)})=[^{separator}]*",
                  lambda m: f"{m.group(1)}={redaction}", message)
