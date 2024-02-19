import re


def filter_datum(fields, redaction, message, separator):
    for field in fields:
        message = re.sub(
            r"{}=[^{}]+".format(field, re.escape(separator)),
            "{}={}".format(field, redaction),
            message,
        )
    return message
