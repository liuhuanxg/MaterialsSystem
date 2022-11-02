#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from home.models import *
from center_library.models import (
    CenterOutboundOrder,
    CenterOutboundOrderDetail
)
from local_library.models import (
    LocalOutboundOrder,
    LocalOutboundOrderDetail,
)
from material_application.models import (
    ExWarehousingApplication,
    ExApplicationFile,
    ApplicationDetail,
    ApplicationHistory,
    LocalAssessmentDetail,
    CenterAssessmentDetail
)
import traceback
from django.db import transaction

class Command(BaseCommand):
    help = '初始化环境'

    def add_arguments(self, parser):
        parser.add_argument('app_codes', nargs='+', type=int)

    def handle(self, *args, **options):
        for app_code in options['app_codes']:
            applications = ExWarehousingApplication.objects.filter(app_code=app_code)
            if applications.exists():
                tid = transaction.savepoint()
                try:
                    application = applications[0]
                    # 删除申请附件和审批历史，
                    ExApplicationFile.objects.filter(application_id=application.id).delete()
                    ApplicationHistory.objects.filter(application_id=application.id).delete()

                    # 删除地方库和中央库研判记录
                    local_orders = LocalOutboundOrder.objects.filter(app_code_id=application.id)
                    local_orders_ids = [local_order.id for local_order in local_orders]
                    LocalOutboundOrderDetail.objects.filter(app_code_id__in=local_orders_ids).delete()
                    local_orders.delete()

                    # 删除中央库研判记录
                    centerl_orders = CenterOutboundOrder.objects.filter(app_code_id=application.id)
                    center_orders_ids = [center_order.id for center_order in centerl_orders]
                    CenterOutboundOrderDetail.objects.filter(app_code_id__in=center_orders_ids).delete()
                    centerl_orders.delete()

                    # 删除研判详情
                    LocalAssessmentDetail.objects.filter(application_id=application.id).delete()
                    CenterAssessmentDetail.objects.filter(application_id=application.id).delete()
                    # 删除申请单详情
                    ApplicationDetail.objects.filter(application_id=application.id).delete()
                    # 删除申请单
                    applications.delete()
                    transaction.savepoint_commit(tid)
                except:
                    transaction.savepoint_rollback(tid)
                    print(traceback.format_exc())

