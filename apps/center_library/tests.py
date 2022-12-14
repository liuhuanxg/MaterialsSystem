from django.test import TestCase
from django.db import models
from django.utils.html import format_html
class CenterLibrarySettings(models.Model):
    pass

# 中央库基本信息
class CenterLibrary(models.Model):
    class Meta:
        verbose_name = "中央库物料管理"
        verbose_name_plural = "中央库物料管理"

    code_num = models.CharField("入库单号", unique=True, max_length=100)
    med_sur_mask = models.IntegerField("医用外科口罩(平面挂耳/只)", default=0)
    n95_masks = models.IntegerField("医用防护口罩(N95)(折叠挂耳/只)", default=0)
    dispos_med_rubber_exam_gloves = models.IntegerField("一次性医用橡胶检查手套(乳胶XS/副)", default=0)
    med_hat = models.IntegerField("橡胶外科手套(麻面无粉/副)", default=0)
    protect_suit = models.IntegerField("医用帽子(个)", default=0)
    iso_gown = models.IntegerField("一次性医用防护服(连体式/套)", default=0)
    surgical_mask = models.IntegerField("一次性医用隔离衣(连体式/套)", default=0)
    med_iso_mask = models.IntegerField("医用隔离面罩(中号/个)", default=0)
    med_iso_eye_mask = models.IntegerField("医用隔离眼罩(护目镜型/只)", default=0)
    med_iso_shoe_cover = models.IntegerField("医用隔离鞋套(40*50双)", default=0)
    infrared_thermometer = models.IntegerField("医用红外体温计(个)", default=0)
    disinfectant1 = models.IntegerField("84消毒液5kg(桶)", default=0)
    disinfectant2 = models.IntegerField("84消毒液850ml(瓶)", default=0)
    disinfectant3 = models.IntegerField("84消毒液500ml(瓶)", default=0)
    alcohol1 = models.IntegerField("75%酒精2.5L(瓶)", default=0)
    alcohol2 = models.IntegerField("75%酒精500ml(瓶)", default=0)
    alcohol3 = models.IntegerField("75%酒精100ml(瓶)", default=0)
    hand_sanitizer1 = models.IntegerField("免洗手消毒液500ml(瓶)", default=0)
    hand_sanitizer2 = models.IntegerField("免洗手消毒液1000ml(瓶)", default=0)
    hand_sanitizer3 = models.IntegerField("免洗手消毒凝胶500ml(瓶)", default=0)
    vegetabl_soap = models.IntegerField("天然植物皂液500ml(瓶)", default=0)
    disinfect_tablets = models.IntegerField("消毒片(100片/瓶)", default=0)
    iodine_skin_sanitizer = models.IntegerField("复合碘皮肤消毒液(60ml/瓶)", default=0)
    dispos_virus_samp_tube1 = models.IntegerField("一次性使用病毒采样管（非灭活）(B型单支/套)", default=0)
    dispos_virus_samp_tube2 = models.IntegerField("一次性使用病毒采样管（灭活）(A型5合1/套)", default=0)
    dispos_virus_samp_tube3 = models.IntegerField("一次性使用病毒采样管（灭活）(A型10合1/套)", default=0)
    cotton_swab = models.IntegerField("棉签(8cm/包)", default=0)
    swab = models.IntegerField("拭子(A型/支)", default=0)
    one_time_strap_tourniquet = models.IntegerField("一次性使用捆扎止血带(条)", default=0)
    inspection_box = models.IntegerField("送检箱(个)", default=0)
    dispos_vac_blood_collect_tube = models.IntegerField("一次性使用真空采血管(个)", default=0)
    dispos_venous_blood_samp_needle = models.IntegerField("一次性使用静脉血样采集针(支)", default=0)
    multi_param_monitor = models.IntegerField("多参数监护仪(C100/台)", default=0)
    ventilator1 = models.IntegerField("无创呼吸机(台)", default=0)
    ventilator2 = models.IntegerField("有创呼吸机(台)", default=0)
    air_puri_sterilizer = models.IntegerField("等离子体空气净化消毒机(台)", default=0)
    ecg_machine = models.IntegerField("心电图机(台)", default=0)
    bed_unit_sterilizer = models.IntegerField("床单位臭氧消毒机(台)", default=0)
    infusion_pump = models.IntegerField("输液泵(台)", default=0)
    injection_pump = models.IntegerField("注射泵(台)", default=0)
    injection_methy_sodium_succinate = models.IntegerField("注射用甲泼尼龙琥珀酸钠（40ml/支）", default=0)
    acetaminophen_tablets = models.IntegerField("对乙酰氨基酚片（0.5g*10片/盒）", default=0)
    lianhua_qingwen_capsules = models.IntegerField("连花清瘟胶囊（0.35g*36粒/盒）", default=0)
    shuanghuanglian_oral_liquid = models.IntegerField("双黄连口服液（20ml*6支/盒）", default=0)
    huoxiangzhengqi_soft_capsules = models.IntegerField("藿香正气软胶囊（0.45g*10s*3板/盒）", default=0)
    trash_bag = models.IntegerField("垃圾袋(个)", default=0)
    tie = models.IntegerField("扎口带(各)", default=0)
    sprayer = models.IntegerField("喷雾器(台)", default=0)
    ashcan = models.IntegerField("垃圾桶(个)", default=0)
    waste_bag = models.IntegerField("废物包装袋(套)", default=0)
    ph_test_paper = models.IntegerField("PH试纸(包)", default=0)
    thermometer = models.IntegerField("体温计(个)", default=0)
    blood_pressure_monitor = models.IntegerField("血压计听诊器(套)", default=0)
    jianwei_xiaoshi_tablets = models.IntegerField("健胃消食片(盒)", default=0)
    changyanning_tablets = models.IntegerField("肠炎宁片(盒)", default=0)
    nitroglycerin_tablets = models.IntegerField("硝酸甘油片(盒)", default=0)
    quick_acting_heart_saving_pills = models.IntegerField("速效救心丸(盒)", default=0)
    adrena_hydroch_injection = models.IntegerField("盐酸肾上腺素注射液(盒)", default=0)
    sterile_syringe_needle = models.IntegerField("无菌注射器带针(盒)", default=0)
    gauze_bandage = models.IntegerField("纱布绷带(盒)", default=0)
    gauze_block = models.IntegerField("纱布块(盒)", default=0)
    bandage = models.IntegerField("创口贴(盒)", default=0)
    captopril = models.IntegerField("卡托普利片(盒)", default=0)
    pressure_sensitive_tape = models.IntegerField("压敏胶带(盒)", default=0)
    iodophor = models.IntegerField("碘伏(盒)", default=0)
    robust_cotto_swab = models.IntegerField("稳健棉签(盒)", default=0)
    ambroxol_hyd_injection = models.IntegerField("盐酸氨溴索注射液(支)(2ml：15mg/支)", default=0)
    des = models.TextField(verbose_name="性质", blank=True)
    add_time = models.DateTimeField(verbose_name="创建时间", default=timezone.now)
    modify_time = models.DateTimeField(verbose_name="修改时间", auto_now_add=True)

    def __str__(self):
        return self.code_num