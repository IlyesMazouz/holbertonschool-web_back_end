#!/usr/bin/env python3

import logging
import csv

PII_FIELDS = ("name", "email", "phone_number", "address", "credit_card")


class RedactingFormatter(logging.Formatter):
    """
    redacting Formatter class for logging
    """

    REDACTION = "***"
    SEPARATOR = ";"

    def __init__(self, fields: tuple):
        """
        initialize the RedactingFormatter with a tuple of fields to redact
        """
        super().__init__(
            "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
        )
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        format a log record, redacting sensitive information.

        """
        message = super().format(record)
        for field in self.fields:
            message = re.sub(
                r"{}=[^{}]+".format(field, re.escape(self.SEPARATOR)),
                "{}={}".format(field, self.REDACTION),
                message,
            )
        return message


def get_logger() -> logging.Logger:
    """
    get a logger named "user_data" that logs up to logging.INFO level
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))

    logger.addHandler(handler)

    logger.propagate = False

    return logger
