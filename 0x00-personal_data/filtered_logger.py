#!/usr/bin/env python3
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
     Args:
        fields: list of fields to redact
        redaction: the value to use for redaction
        message: the string message to filter
        separator: the separator to use between fields

    Returns regex obfuscated log messages.
    """
    return re.sub(rf"({'|'.join(fields)})=[^{separator}]*",
                  lambda m: f"{m.group(1)}={redaction}", message)
