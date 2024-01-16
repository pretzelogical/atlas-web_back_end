#!/usr/bin/env python3
""" Filtered logger """
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, seperator: str) -> str:
    """
        Filters message so redacted data is replaced with redaction
    """
    for field in fields:
        message = re.sub(f"{field}=.*?{seperator}",
                         f"{field}={redaction}{seperator}", message)
    return message
