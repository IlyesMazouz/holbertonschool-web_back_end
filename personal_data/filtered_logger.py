#!/usr/bin/env python3

"""
A module for filtering sensitive data in log messages
"""

import re
from typing import List


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """
    Filters sensitive data in a log message by obfuscating specified fields
    """
    for field in fields:
        message = re.sub(
            r"{}=[^{}]+".format(field, re.escape(separator)),
            "{}={}".format(field, redaction),
            message,
        )
    return message


if __name__ == "__main__":
    fields = ["password", "date_of_birth"]
    messages = [
        "name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;",
        "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;",
    ]

    for message in messages:
        print(filter_datum(fields, "xxx", message, ";"))
