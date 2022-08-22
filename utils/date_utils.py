#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os

from MaterialsSystem.settings import base_path


def get_date_str():
    now = datetime.datetime.now()
    month = now.month
    if now.month < 10:
        month = "0{}".format(now.month)
    date_str = str(now.year) + str(month) + str(now.day)
    return date_str


def upload_path_handler(db_path):
    now = datetime.datetime.now()
    file_path = os.path.join(base_path, db_path, str(now.year), str(now.month), str(now.day))
    return file_path
