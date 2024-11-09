#!/usr/bin/env python3i
"""Use of regex in replacing occurences of certain field values."""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Returns regex obfuscated log messages."""
    return re.sub(rf"({'|'.join(fields)})=[^{separator}]*",
                  lambda m: f"{m.group(1)}={redaction}", message)
