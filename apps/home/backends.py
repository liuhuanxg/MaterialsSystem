#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from django.contrib.auth.password_validation import NumericPasswordValidator
from django.core.exceptions import (
    ValidationError,
)


# 12位及以上 大小写 特殊字符 数字 四选三
class MyNumericPasswordValidator(NumericPasswordValidator):
    def validate(self, password, user=None):
        number = 0

        if re.search(r'\d+', password):
            number += 1
        if re.search(r'[a-z]+', password):
            number += 1
        if re.search(r'[A-Z]+', password):
            number += 1
        if re.search(r'[!@#$%^&*()_+=-]+', password):
            number += 1

        if number < 3:
            raise ValidationError("密码必须12位，并且包含大小写字母、特殊字符(@#$%^&*()_+=-)、数字中的3种及以上")

    def get_help_text(self):
        return ("密码必须12位，并且包含大小写字母、特殊字符(@#$%^&*()_+=-)、数字中的3种及以上")
