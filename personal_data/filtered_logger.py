#!/usr/bin/env python3

"""
A module for providing a RedactingFormatter
class for logging with sensitive data redacted
"""
import logging
import re
from typing import List


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        initialize the RedactingFormatter with a list of fields to redact
        """
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        format a log record, redacting sensitive information
        """
        message = super().format(record)
        for field in self.fields:
            message = re.sub(
                r"{}=[^{}]+".format(field, re.escape(self.SEPARATOR)),
                "{}={}".format(field, self.REDACTION),
                message,
            )
        return message
