#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os

from MaterialsSystem.settings import base_path


def get_date_str():
    date_str = "".join(datetime.datetime.now().strftime("%Y-%m-%d").split("-"))
    return date_str


def upload_path_handler(db_path):
    now = datetime.datetime.now()
    file_path = os.path.join(base_path, db_path, str(now.year), str(now.month), str(now.day))
    return file_path
