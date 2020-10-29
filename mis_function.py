'''
mis function
'''
import os
import yaml
import logging
import datetime
LOGGER = logging.getLogger('report_api')
LOGGER.setLevel(logging.INFO)

def date_format(date_str, fromat_from, format_to):
    try:
        return datetime.datetime.strptime(date_str, fromat_from).strftime(format_to)
    except Exception as ex:
        LOGGER.error(f"Error occured while parsing date {date_str},{fromat_from}, {format_to} -> {ex}")
        return date_str