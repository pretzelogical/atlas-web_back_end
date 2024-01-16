#!/usr/bin/env python3
""" Filtered logger """
import re
import logging
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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        """ Initializes the RedactingFormatter """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Formats the string using filter_datum """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)
