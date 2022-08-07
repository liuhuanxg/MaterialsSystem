import django.utils.timezone as timezone
from django.db import models
from django.utils.html import format_html


# 地方库基本信息
class LocalLibrary(models.Model):
    class Meta:
        verbose_name = "地方库物料管理"
        verbose_name_plural = "地方库物料管理"

    library_name = models.CharField("地方库名称", unique=True, max_length=100)
    surgical_mask = models.IntegerField("医用外科口罩(平面型/个)", default=0)
    surgical_mask = models.IntegerField("N95口罩(耳挂式/个)", default=0)
    surgical_mask = models.IntegerField("医用检查手套(副)", default=0)
    surgical_mask = models.IntegerField("医用外科手套(副)", default=0)
    surgical_mask = models.IntegerField("印记帐篷(平面型/个)", default=0)
    surgical_mask = models.IntegerField("医用外科口罩(600D/顶)", default=0)
    surgical_mask = models.IntegerField("电暖器(扬子牌/个)", default=0)
    surgical_mask = models.IntegerField("扩音喇叭(个)", default=0)
    surgical_mask = models.IntegerField("桌子(120*60/个)", default=0)
    surgical_mask = models.IntegerField("凳子(塑料/个)", default=0)
    surgical_mask = models.IntegerField("隔离带(不锈钢/个)", default=0)
    surgical_mask = models.IntegerField("医用隔离面罩(200个/箱)", default=0)
    surgical_mask = models.IntegerField("医用隔离眼罩(K01/个)", default=0)
    surgical_mask = models.IntegerField("医用隔离鞋套(XT00/双)", default=0)
    surgical_mask = models.IntegerField("防护服(连体式/件)", default=0)
    surgical_mask = models.IntegerField("隔离服(连体式个/件)", default=0)
    surgical_mask = models.IntegerField("防水隔离衣（手术衣）(非连体式/件)", default=0)
    surgical_mask = models.IntegerField("一次性防护帽(个)", default=0)
    surgical_mask = models.IntegerField("84消毒液(500ml/瓶)", default=0)
    surgical_mask = models.IntegerField("免洗手消毒液(500ml/箱)", default=0)
    surgical_mask = models.IntegerField("消毒片(100片/瓶)", default=0)
    surgical_mask = models.IntegerField("医用酒精(500ml/瓶)", default=0)
    surgical_mask = models.IntegerField("医用酒精(2500ml/瓶)", default=0)
    surgical_mask = models.IntegerField("额温枪(把)", default=0)
    surgical_mask = models.IntegerField("拭子(支)", default=0)
    surgical_mask = models.IntegerField("注射器(1ml/支)", default=0)
    surgical_mask = models.IntegerField("病毒采样管（灭活单只）(A型3ml/支)", default=0)
    surgical_mask = models.IntegerField("病毒采样管（灭活10合1）(A型6ml/支)", default=0)
    surgical_mask = models.IntegerField("核酸检测试剂盒(32人份/盒/人份)", default=0)
    surgical_mask = models.IntegerField("核酸检测试剂盒(48人份/盒/人份)", default=0)
    surgical_mask = models.IntegerField("核酸检测试剂盒(50人份/盒/人份)", default=0)
    surgical_mask = models.IntegerField("核酸检测试剂盒(96人份/盒/人份)", default=0)
    surgical_mask = models.IntegerField("核酸检测试剂盒(100人份/盒/人份)", default=0)
    surgical_mask = models.IntegerField("核酸检测试剂盒(200人份/盒/人份)", default=0)
    surgical_mask = models.IntegerField("核酸提取试剂盒(32人份/盒/人份)", default=0)
    surgical_mask = models.IntegerField("核酸提取试剂盒(96人份/盒/人份)", default=0)
    surgical_mask = models.IntegerField("新冠病毒抗体检测试剂(40人份/人份)", default=0)
    surgical_mask = models.IntegerField("新冠病毒抗体检测试剂(50人份/人份)", default=0)
    surgical_mask = models.IntegerField("自立式病理标本(L号/片)", default=0)
    surgical_mask = models.IntegerField("标本运输箱(25L/个)", default=0)
    surgical_mask = models.IntegerField("集装箱(6*3*2.51/个)", default=0)
    surgical_mask = models.IntegerField("医疗废物专用桶(30L-1脚踏式/个)", default=0)
    surgical_mask = models.IntegerField("垃圾桶(240L/个)", default=0)
    surgical_mask = models.IntegerField("低温保存箱(DW-25L300/个)", default=0)
    surgical_mask = models.IntegerField("行军床(折叠式/张)", default=0)
    surgical_mask = models.IntegerField("棉被(2*1.5/床)", default=0)
    surgical_mask = models.IntegerField("电动喷雾器)", default=0)
    surgical_mask = models.IntegerField("棉被(2*1.5/床)", default=0)
    surgical_mask = models.IntegerField("棉被(2*1.5/床)", default=0)
    surgical_mask = models.IntegerField("棉被(2*1.5/床)", default=0)
    surgical_mask = models.IntegerField("棉被(2*1.5/床)", default=0)
    surgical_mask = models.IntegerField("棉被(2*1.5/床)", default=0)
    surgical_mask = models.IntegerField("棉被(2*1.5/床)", default=0)
    surgical_mask = models.IntegerField("棉被(2*1.5/床)", default=0)
    surgical_mask = models.IntegerField("棉被(2*1.5/床)", default=0)
    surgical_mask = models.IntegerField("棉被(2*1.5/床)", default=0)
    des = models.TextField(verbose_name="类别描述", blank=True)
    add_time = models.DateTimeField(verbose_name="创建时间", default=timezone.now)
    modify_time = models.DateTimeField(verbose_name="修改时间", auto_now_add=True)

    def __str__(self):
        return self.library_name
