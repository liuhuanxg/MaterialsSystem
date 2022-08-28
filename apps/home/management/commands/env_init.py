#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, Group
from django.core.management.base import BaseCommand
from django.utils import timezone
from home.models import MaterialsType


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
    ("盒装带滤芯吸嘴", "盒", "10ul（加长），96个/盒"),
    ("盒装带滤芯吸嘴", "盒", "1250ul，96个/盒"),
    ("核酸清除剂", "瓶", "≥500 mL/瓶"),
    ("新型冠状病毒抗原检测试剂", "袋", "1人份/袋。样本类型：鼻拭子"),
    ("新型冠状病毒抗原检测试剂", "盒", "40人份/盒。样本类型：鼻拭子"),
    ("样本释放剂", "份", "1人份。样本类型：拭子类样本（咽/鼻/眼结膜）"),
    ("盒装带滤芯吸嘴", "盒", "10ul，96个/盒"),
    ("盒装带滤芯吸嘴", "盒", "200ul，96个/盒"),
    ("盒装带滤芯吸嘴", "盒", "100ul，96个/盒"),
    ("8连管（含盖）", "盒", "125排/盒"),
    ("微量离心管（EP管）", "盒", "1.5ml"),
    ("微量离心管（EP管）", "盒", "2.0ml"),
    ("核酸提取试剂", "盒", "8人份/盒"),
    ("核酸提取试剂", "盒", "24人份/盒"),
    ("核酸提取试剂", "盒", "48人份/盒"),
    ("核酸提取试剂", "盒", "96人份/盒"),
    ("核酸提取试剂", "人份", "48人份/盒、96人份/盒。"),
    ("核酸提取试剂", "人份", "48人份/盒、96人份/盒。处理样本体积：50-200ul"),
    ("新型冠状病毒2019-nCoV核酸检测试剂盒", "人份", "50人份/盒、200人份/盒。"),
    ("新型冠状病毒2019-nCoV核酸检测试剂盒", "人份", "100人份/盒"),
    ("新型冠状病毒2019-nCoV核酸检测试剂盒", "人份", "50 人份/盒、96人份/盒"),
    ("新型冠状病毒2019-nCoV核酸检测试剂盒", "人份", "48人份/盒、96人份/盒"),
    ("新型冠状病毒2019-nCoV核酸检测试剂盒", "人份", "试剂盒内所提供试剂量≥48次检测需求。最低检出限：不高于200 copies /mL"),
    ("新型冠病毒核酸检测质控品", "盒", "0.5ml/支"),
    ("新型冠病毒核酸检测质控品", "盒", "装量不得小于1ml/支"),
    ("新型冠状病毒(2019-nCoV)IgM/IgG抗体检测试剂盒", "人份", "测定速度：10分钟。样本量：20µL"),
    ("新型冠状病毒(2019-nCoV)IgM/IgG抗体检测试剂盒", "人份", "检测速度：≤15 分钟。样本量：检测 IgM、IgG 所需总样本量≤20 微升"),
]


def add_types():
    for m_type in materials_types:
        mater_type = MaterialsType.objects.filter(materials_name=m_type[0], specifications=m_type[2], unit=m_type[1])
        if mater_type.exists():
            continue
        material_type = MaterialsType()
        material_type.materials_name = m_type[0]
        material_type.specifications = m_type[2]
        material_type.unit = m_type[1]
        material_type.save()


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
