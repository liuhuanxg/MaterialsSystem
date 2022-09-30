#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, Group
from django.core.management.base import BaseCommand
from django.utils import timezone
from home.models import MaterialsType
import traceback

class Command(BaseCommand):
    help = '初始化环境'

    def add_arguments(self, parser):
        parser.add_argument('actions', nargs='+', type=int)

    def handle(self, *args, **options):
        for action in options['actions']:
            if action == 1:
                add_types()
            elif action == 2:
                add_users()
            elif action == 3:
                add_groups()
            else:
                continue
            print("success")


materials_types = [
    ("新型冠状病毒(2019-nCoV)IgM/IgG抗体检测试剂盒", "人份", "检测速度：≤15 分钟。样本量：检测 IgM、IgG 所需总样本量≤20 微升", "描述", "18737307883"),
]

import traceback
def add_types():
    for m_type in materials_types:
        try:
            mater_type = MaterialsType.objects.filter(materials_name=m_type[0], specifications=m_type[2], unit=m_type[1])
            if mater_type.exists():
                continue
            material_type = MaterialsType()
            material_type.materials_name = m_type[0]
            material_type.specifications = m_type[2]
            material_type.unit = m_type[1]
            if len(m_type) > 3:
                material_type.des = m_type[3]
            if len(m_type) > 4:
                material_type.phone = m_type[4]
            material_type.save()
        except:
            print("add_types error:{}".format(traceback.format_exc()))


def add_users():
    users = ["admin", "ybkb", "ybkb1", "ybkb2", "ybkb3", "ybkb4"]
    for username in users:
        user = User.objects.filter(username=username)
        if user.exists():
            user.update(first_name=username)
            continue
        user = User.objects.create_user(
            username=username,
            password="admin123456@",
            first_name=username,
            email="{}@qq.com".format(username),
            last_login=timezone.now(),
            is_active=1,
            is_staff=1
        )
        if username == "admin":
            user.is_superuser = 1
        user.save()


def add_groups():
    groups = ["分管领导", "局长", "仓库管理员", "供应商", "主管科室"]
    for group_name in groups:
        group, err = Group.objects.get_or_create(name=group_name)
