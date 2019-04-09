from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Asset(models.Model):
    """    所有资产的共有数据表    """
    asset_type_choice = (
        ('server', '服务器'),
        ('networkdevice', '网络设备'),
        ('storagedevice', '存储设备'),
        ('securitydevice', '安全设备'),
        ('software', '软件资产'),
    )

    asset_status = (
        (0, '在线'),
        (1, '下线'),
        (2, '未知'),
        (3, '故障'),
        (4, '备用'),
        )

    asset_type = models.CharField(choices=asset_type_choice, max_length=64, default='server', verbose_name="资产类型")
    name = models.CharField(max_length=64, unique=True, verbose_name="资产名称")     # 不可重复
    sn = models.CharField(max_length=128, unique=True, verbose_name="资产序列号")  # 不可重复
    business_unit = models.ForeignKey('BusinessUnit', null=True, blank=True, verbose_name='所属业务线', on_delete=models.CASCADE)
    status = models.SmallIntegerField(choices=asset_status, default=0, verbose_name='设备状态')

    manufacturer = models.ForeignKey('Manufacturer', null=True, blank=True, verbose_name='制造商', on_delete=models.CASCADE)
    manage_ip = models.GenericIPAddressField(null=True, blank=True, verbose_name='管理IP')
    tags = models.ManyToManyField('Tag', blank=True, verbose_name='标签')
    admin = models.ForeignKey(User, null=True, blank=True, verbose_name='资产管理员', related_name='admin', on_delete=models.CASCADE)
    idc = models.ForeignKey('IDC', null=True, blank=True, verbose_name='所在机房', on_delete=models.CASCADE)
    contract = models.ForeignKey('Contract', null=True, blank=True, verbose_name='合同', on_delete=models.CASCADE)

    purchase_day = models.DateField(null=True, blank=True, verbose_name="购买日期")
    expire_day = models.DateField(null=True, blank=True, verbose_name="过保日期")
    price = models.FloatField(null=True, blank=True, verbose_name="价格")

    approved_by = models.ForeignKey(User, null=True, blank=True, verbose_name='批准人', related_name='approved_by', on_delete=models.CASCADE)

    memo = models.TextField(null=True, blank=True, verbose_name='备注')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='批准日期')
    m_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')

    def __str__(self):
        return '<%s>  %s' % (self.get_asset_type_display(), self.name)

    class Meta:
        verbose_name = '资产总表'
        verbose_name_plural = "资产总表"
        ordering = ['-c_time']

class Carform(models.Model):
    """    所有资产的共有数据表    """
    Car_VIN = models.CharField(max_length=64, unique=True, verbose_name="车辆VIN编码")     # 不可重复
    Carname = models.CharField(max_length=24, unique=True, verbose_name="汽车型号")     # 不可重复
    License_number = models.CharField(max_length=24, unique=True, verbose_name="车牌号码")  # 不可重复
    Serure_number = models.CharField(max_length=128, verbose_name="数据传输验证码")  # 不可重复
    created_time = models.DateTimeField(auto_now_add=True)  # 车辆入库时间

class Carformtest(models.Model):
    """    所有资产的共有数据表    """
    Car_VIN = models.CharField(max_length=64, unique=True, verbose_name="车辆VIN编码")     # 不可重复
    Carname = models.CharField(max_length=24, unique=False, verbose_name="汽车型号")     # 不可重复
    Carnickname = models.CharField(max_length=24, unique=False, verbose_name="汽车名称")     # 不可重复
    License_number = models.CharField(max_length=24, unique=True, verbose_name="车牌号码")  # 不可重复
    Serure_number = models.CharField(max_length=128, verbose_name="数据传输验证码")  # 不可重复
    created_time = models.DateTimeField(auto_now_add=True)  # 车辆入库时间

class Motor(models.Model):
    """    所有资产的共有数据表    """
    Carformtest = models.ForeignKey('Carformtest', null=True, blank=True, verbose_name='汽车名称', on_delete=models.CASCADE)
    Totalmileage = models.FloatField(max_length=48, unique=False, verbose_name="电机转矩")     # 不可重复
    totalvoltage = models.FloatField(max_length=48, unique=False, verbose_name="电机转速")     # 不可重复
    totalcurrent = models.FloatField(max_length=48, unique=False, verbose_name="电机母线电压")     # 不可重复
    Totalmileage = models.FloatField(max_length=48, unique=False, verbose_name="电机母线电流")     # 不可重复

    local_time = models.DateTimeField(auto_now_add=False)  # 车辆数据生成时间
    created_time = models.DateTimeField(auto_now_add=True)  # 车辆数据入库时间

class Motortest(models.Model):
    """    所有资产的共有数据表    """
    Carformtest = models.ForeignKey('Carformtest', null=True, blank=True, verbose_name='汽车名称', on_delete=models.CASCADE)
    torque = models.FloatField(max_length=48, unique=False, verbose_name="电机转矩")     # 不可重复
    torquespeed = models.FloatField(max_length=48, unique=False, verbose_name="电机转速")     # 不可重复
    torquecurrent = models.FloatField(max_length=48, unique=False, verbose_name="电机母线电压")     # 不可重复
    torquemileage = models.FloatField(max_length=48, unique=False, verbose_name="电机母线电流")     # 不可重复

    local_time = models.DateTimeField(auto_now_add=False)  # 车辆数据生成时间
    created_time = models.DateTimeField(auto_now_add=True)  # 车辆数据入库时间

class Motortest1(models.Model):
    """    所有资产的共有数据表    """
    Carformtest = models.ForeignKey('Carformtest', null=True, blank=True, verbose_name='汽车名称', on_delete=models.CASCADE)
    torque = models.FloatField(max_length=48, unique=False, verbose_name="电机转矩")     # 不可重复
    torquespeed = models.FloatField(max_length=48, unique=False, verbose_name="电机转速")     # 不可重复
    torquecurrent = models.FloatField(max_length=48, unique=False, verbose_name="电机母线电压")     # 不可重复
    torquemileage = models.FloatField(max_length=48, unique=False, verbose_name="电机母线电流")     # 不可重复

    time = models.BigIntegerField(default=0, verbose_name='数据产生时间')
    created_time = models.DateTimeField(auto_now_add=True)  # 车辆数据入库时间
class Carrealtimetest(models.Model):
    """    所有资产的共有数据表    """
    Statevehicle_status = (
        ('0', '启动'),
        ('1', '熄火'),
        ('2', '其他'),
        )

    Chargingstatus_status = (
        ('0', '停车充电'),
        ('1', '行驶充电'),
        ('2', '未充电'),
        ('3', '充电完成'),
        )
    DC_DC_status = (
        ('0', '工作'),
        ('1', '断开'),
        )
    Carnickname = models.OneToOneField('Carformtest', null=True, blank=True, verbose_name='汽车名称', on_delete=models.CASCADE)

    Statevehicle = models.CharField(choices=Statevehicle_status, max_length=24, unique=False, verbose_name="车辆状态")     # 不可重复
    Chargingstatus = models.CharField(choices=Chargingstatus_status, max_length=24, unique=False, verbose_name="充电状态")     # 不可重复
    speed = models.FloatField(max_length=48, unique=False, verbose_name="车速")     # 不可重复
    Totalmileage = models.FloatField(max_length=24, unique=False, verbose_name="累计行程")     # 不可重复
    totalvoltage = models.FloatField(max_length=24, unique=False, verbose_name="总电压")     # 不可重复
    totalcurrent = models.FloatField(max_length=24, unique=False, verbose_name="总电流")     # 不可重复
    SOC = models.CharField(max_length=24, unique=False, verbose_name="SOC")     # 不可重复
    DC_DC = models.CharField(choices=DC_DC_status, max_length=24, unique=False, verbose_name="DC/DC状态")     # 不可重复
    gear = models.CharField(max_length=24, unique=False, verbose_name="档位")     # 不可重复
    resistance = models.CharField(max_length=24, unique=False, verbose_name="绝缘电阻")     # 不可重复
    Accelerator = models.CharField(max_length=24, unique=False, verbose_name="加速踏板行程值")     # 不可重复
    brake = models.CharField(max_length=24, unique=False, verbose_name="制动踏板形成值")     # 不可重复
    local_time = models.DateTimeField(auto_now_add=False)  # 车辆数据生成时间
    created_time = models.DateTimeField(auto_now_add=True)  # 车辆数据入库时间

class Server(models.Model):
    """服务器设备"""
    sub_asset_type_choice = (
        (0, 'PC服务器'),
        (1, '刀片机'),
        (2, '小型机'),
    )

    created_by_choice = (
        ('auto', '自动添加'),
        ('manual', '手工录入'),
    )

    asset = models.OneToOneField('Asset', on_delete=models.CASCADE)  # 非常关键的一对一关联！
    sub_asset_type = models.SmallIntegerField(choices=sub_asset_type_choice, default=0, verbose_name="服务器类型")
    created_by = models.CharField(choices=created_by_choice, max_length=32, default='auto', verbose_name="添加方式")
    hosted_on = models.ForeignKey('self', related_name='hosted_on_server',
                                  blank=True, null=True, verbose_name="宿主机", on_delete=models.CASCADE)  # 虚拟机专用字段
    model = models.CharField(max_length=128, null=True, blank=True, verbose_name='服务器型号')
    raid_type = models.CharField(max_length=512, blank=True, null=True, verbose_name='Raid类型')

    os_type = models.CharField('操作系统类型', max_length=64, blank=True, null=True)
    os_distribution = models.CharField('发行版本', max_length=64, blank=True, null=True)
    os_release = models.CharField('操作系统版本', max_length=64, blank=True, null=True)

    def __str__(self):
        return '%s--%s--%s <sn:%s>' % (self.asset.name, self.get_sub_asset_type_display(), self.model, self.asset.sn)

    class Meta:
        verbose_name = '服务器'
        verbose_name_plural = "服务器"


class SecurityDevice(models.Model):
    """安全设备"""
    sub_asset_type_choice = (
        (0, '防火墙'),
        (1, '入侵检测设备'),
        (2, '互联网网关'),
        (4, '运维审计系统'),
    )

    asset = models.OneToOneField('Asset', on_delete=models.CASCADE)
    sub_asset_type = models.SmallIntegerField(choices=sub_asset_type_choice, default=0, verbose_name="安全设备类型")

    def __str__(self):
        return self.asset.name + "--" + self.get_sub_asset_type_display() + " id:%s" % self.id

    class Meta:
        verbose_name = '安全设备'
        verbose_name_plural = "安全设备"


class StorageDevice(models.Model):
    """存储设备"""
    sub_asset_type_choice = (
        (0, '磁盘阵列'),
        (1, '网络存储器'),
        (2, '磁带库'),
        (4, '磁带机'),
    )

    asset = models.OneToOneField('Asset', on_delete=models.CASCADE)
    sub_asset_type = models.SmallIntegerField(choices=sub_asset_type_choice, default=0, verbose_name="存储设备类型")

    def __str__(self):
        return self.asset.name + "--" + self.get_sub_asset_type_display() + " id:%s" % self.id

    class Meta:
        verbose_name = '存储设备'
        verbose_name_plural = "存储设备"


class NetworkDevice(models.Model):
    """网络设备"""
    sub_asset_type_choice = (
        (0, '路由器'),
        (1, '交换机'),
        (2, '负载均衡'),
        (4, 'VPN设备'),
    )

    asset = models.OneToOneField('Asset', on_delete=models.CASCADE)
    sub_asset_type = models.SmallIntegerField(choices=sub_asset_type_choice, default=0, verbose_name="网络设备类型")

    vlan_ip = models.GenericIPAddressField(blank=True, null=True, verbose_name="VLanIP")
    intranet_ip = models.GenericIPAddressField(blank=True, null=True, verbose_name="内网IP")

    model = models.CharField(max_length=128, null=True, blank=True, verbose_name="网络设备型号")
    firmware = models.CharField(max_length=128, blank=True, null=True, verbose_name="设备固件版本")
    port_num = models.SmallIntegerField(null=True, blank=True, verbose_name="端口个数")
    device_detail = models.TextField(null=True, blank=True, verbose_name="详细配置")

    def __str__(self):
        return '%s--%s--%s <sn:%s>' % (self.asset.name, self.get_sub_asset_type_display(), self.model, self.asset.sn)

    class Meta:
        verbose_name = '网络设备'
        verbose_name_plural = "网络设备"


class Software(models.Model):
    """
    只保存付费购买的软件
    """
    sub_asset_type_choice = (
        (0, '操作系统'),
        (1, '办公\开发软件'),
        (2, '业务软件'),
    )

    sub_asset_type = models.SmallIntegerField(choices=sub_asset_type_choice, default=0, verbose_name="软件类型")
    license_num = models.IntegerField(default=1, verbose_name="授权数量")
    version = models.CharField(max_length=64, unique=True, help_text='例如: CentOS release 6.7 (Final)',
                               verbose_name='软件/系统版本')

    def __str__(self):
        return '%s--%s' % (self.get_sub_asset_type_display(), self.version)

    class Meta:
        verbose_name = '软件/系统'
        verbose_name_plural = "软件/系统"


class CPU(models.Model):
    """CPU组件"""

    asset = models.OneToOneField('Asset', on_delete=models.CASCADE)  # 设备上的cpu肯定都是一样的，所以不需要建立多个cpu数据，一条就可以，因此使用一对一。
    cpu_model = models.CharField('CPU型号', max_length=128, blank=True, null=True)
    cpu_count = models.PositiveSmallIntegerField('物理CPU个数', default=1)
    cpu_core_count = models.PositiveSmallIntegerField('CPU核数', default=1)

    def __str__(self):
        return self.asset.name + ":   " + self.cpu_model

    class Meta:
        verbose_name = 'CPU'
        verbose_name_plural = "CPU"


class RAM(models.Model):
    """内存组件"""

    asset = models.ForeignKey('Asset', on_delete=models.CASCADE)  # 只能通过外键关联Asset。否则不能同时关联服务器、网络设备等等。
    sn = models.CharField('SN号', max_length=128, blank=True, null=True)
    model = models.CharField('内存型号', max_length=128, blank=True, null=True)
    manufacturer = models.CharField('内存制造商', max_length=128, blank=True, null=True)
    slot = models.CharField('插槽', max_length=64)
    capacity = models.IntegerField('内存大小(GB)', blank=True, null=True)

    def __str__(self):
        return '%s: %s: %s: %s' % (self.asset.name, self.model, self.slot, self.capacity)

    class Meta:
        verbose_name = '内存'
        verbose_name_plural = "内存"
        unique_together = ('asset', 'slot')  # 同一资产下的内存，根据插槽的不同，必须唯一


class Disk(models.Model):
    """存储设备"""

    disk_interface_type_choice = (
        ('SATA', 'SATA'),
        ('SAS', 'SAS'),
        ('SCSI', 'SCSI'),
        ('SSD', 'SSD'),
        ('unknown', 'unknown'),
    )

    asset = models.ForeignKey('Asset', on_delete=models.CASCADE)
    sn = models.CharField('硬盘SN号', max_length=128)
    slot = models.CharField('所在插槽位', max_length=64, blank=True, null=True)
    model = models.CharField('磁盘型号', max_length=128, blank=True, null=True)
    manufacturer = models.CharField('磁盘制造商', max_length=128, blank=True, null=True)
    capacity = models.FloatField('磁盘容量(GB)', blank=True, null=True)
    interface_type = models.CharField('接口类型', max_length=16, choices=disk_interface_type_choice, default='unknown')

    def __str__(self):
        return '%s:  %s:  %s:  %sGB' % (self.asset.name, self.model, self.slot, self.capacity)

    class Meta:
        verbose_name = '硬盘'
        verbose_name_plural = "硬盘"
        unique_together = ('asset', 'sn')


class NIC(models.Model):
    """网卡组件"""

    asset = models.ForeignKey('Asset', on_delete=models.CASCADE)  # 注意要用外键
    name = models.CharField('网卡名称', max_length=64, blank=True, null=True)
    model = models.CharField('网卡型号', max_length=128)
    mac = models.CharField('MAC地址', max_length=64)  # 虚拟机有可能会出现同样的mac地址
    ip_address = models.GenericIPAddressField('IP地址', blank=True, null=True)
    net_mask = models.CharField('掩码', max_length=64, blank=True, null=True)
    bonding = models.CharField('绑定地址', max_length=64, blank=True, null=True)

    def __str__(self):
        return '%s:  %s:  %s' % (self.asset.name, self.model, self.mac)

    class Meta:
        verbose_name = '网卡'
        verbose_name_plural = "网卡"
        unique_together = ('asset', 'model', 'mac')  # 资产、型号和mac必须联合唯一。防止虚拟机中的特殊情况发生错误。


class IDC(models.Model):
    """机房"""
    name = models.CharField(max_length=64, unique=True, verbose_name="机房名称")
    memo = models.CharField(max_length=128, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '机房'
        verbose_name_plural = "机房"


class Manufacturer(models.Model):
    """厂商"""

    name = models.CharField('厂商名称', max_length=64, unique=True)
    telephone = models.CharField('支持电话', max_length=30, blank=True, null=True)
    memo = models.CharField('备注', max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '厂商'
        verbose_name_plural = "厂商"


class BusinessUnit(models.Model):
    """业务线"""

    parent_unit = models.ForeignKey('self', blank=True, null=True, related_name='parent_level', on_delete=models.CASCADE)
    name = models.CharField('业务线', max_length=64, unique=True)
    memo = models.CharField('备注', max_length=64, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '业务线'
        verbose_name_plural = "业务线"


class Contract(models.Model):
    """合同"""

    sn = models.CharField('合同号', max_length=128, unique=True)
    name = models.CharField('合同名称', max_length=64)
    memo = models.TextField('备注', blank=True, null=True)
    price = models.IntegerField('合同金额')
    detail = models.TextField('合同详细', blank=True, null=True)
    start_day = models.DateField('开始日期', blank=True, null=True)
    end_day = models.DateField('失效日期', blank=True, null=True)
    license_num = models.IntegerField('license数量', blank=True, null=True)
    c_day = models.DateField('创建日期', auto_now_add=True)
    m_day = models.DateField('修改日期', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '合同'
        verbose_name_plural = "合同"


class Tag(models.Model):
    """标签"""
    name = models.CharField('标签名', max_length=32, unique=True)
    c_day = models.DateField('创建日期', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = "标签"


class EventLog(models.Model):
    """
    日志.
    在关联对象被删除的时候，不能一并删除，需保留日志。
    因此，on_delete=models.SET_NULL
    """

    name = models.CharField('事件名称', max_length=128)
    event_type_choice = (
        (0, '其它'),
        (1, '硬件变更'),
        (2, '新增配件'),
        (3, '设备下线'),
        (4, '设备上线'),
        (5, '定期维护'),
        (6, '业务上线\更新\变更'),
    )
    asset = models.ForeignKey('Asset', blank=True, null=True, on_delete=models.SET_NULL)  # 当资产审批成功时有这项数据
    new_asset = models.ForeignKey('NewAssetApprovalZone', blank=True, null=True, on_delete=models.SET_NULL)  # 当资产审批失败时有这项数据
    event_type = models.SmallIntegerField('事件类型', choices=event_type_choice, default=4)
    component = models.CharField('事件子项', max_length=256, blank=True, null=True)
    detail = models.TextField('事件详情')
    date = models.DateTimeField('事件时间', auto_now_add=True)
    User = models.ForeignKey(User, blank=True, null=True, verbose_name='事件执行人', on_delete=models.SET_NULL)  # 自动更新资产数据时没有执行人
    memo = models.TextField('备注', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '事件纪录'
        verbose_name_plural = "事件纪录"


class NewAssetApprovalZone(models.Model):
    """新资产待审批区"""

    sn = models.CharField('资产SN号', max_length=128, unique=True)  # 此字段必填
    asset_type_choice = (
        ('server', '服务器'),
        ('networkdevice', '网络设备'),
        ('storagedevice', '存储设备'),
        ('securitydevice', '安全设备'),
        ('software', '软件资产'),
    )
    asset_type = models.CharField(choices=asset_type_choice, default='server', max_length=64, blank=True, null=True,
                                  verbose_name='资产类型')

    manufacturer = models.CharField(max_length=64, blank=True, null=True, verbose_name='生产厂商')
    model = models.CharField(max_length=128, blank=True, null=True, verbose_name='型号')
    ram_size = models.PositiveIntegerField(blank=True, null=True, verbose_name='内存大小')
    cpu_model = models.CharField(max_length=128, blank=True, null=True, verbose_name='CPU型号')
    cpu_count = models.PositiveSmallIntegerField(blank=True, null=True)
    cpu_core_count = models.PositiveSmallIntegerField(blank=True, null=True)
    os_distribution = models.CharField(max_length=64, blank=True, null=True)
    os_type = models.CharField(max_length=64, blank=True, null=True)
    os_release = models.CharField(max_length=64, blank=True, null=True)

    data = models.TextField('资产数据')  # 此字段必填

    c_time = models.DateTimeField('汇报日期', auto_now_add=True)
    m_time = models.DateTimeField('数据更新日期', auto_now=True)
    approved = models.BooleanField('是否批准', default=False)

    def __str__(self):
        return self.sn

    class Meta:
        verbose_name = '新上线待批准资产'
        verbose_name_plural = "新上线待批准资产"
        ordering = ['-c_time']

class testcarform(models.Model):
    """    所有资产的共有数据表    """
    CarVIN = models.CharField(max_length=64, unique=True, verbose_name="车辆VIN编码")     # 不可重复
    Carname = models.CharField(max_length=24, unique=True, verbose_name="车辆名称")     # 不可重复
    Licensenumber = models.CharField(max_length=24, unique=True, verbose_name="车牌号码")  # 不可重复
    serialnum = models.CharField(primary_key=True, max_length=24, unique=True, verbose_name="内部编号")     # 不可重复
    Serurenumber = models.CharField(max_length=128, verbose_name="数据传输验证码")  # 不可重复
    createdtime = models.DateTimeField(auto_now_add=True)  # 车辆入库时间

class testcarrealtime(models.Model):
    """    所有资产的共有数据表    """
    Statevehicle_status = (
        ('01', '启动'),
        ('02', '熄火'),
        ('03', '其他'),
        ('FE', '异常'),
        )

    Chargingstatus_status = (
        ('01', '停车充电'),
        ('02', '行驶充电'),
        ('03', '未充电'),
        ('04', '充电完成'),
        ('FE', '异常'),
        )
    mode_status = (
        ('01', '纯电'),
        ('02', '混动'),
        ('03', '燃油'),
        ('FE', '异常'),
        )
    DCDC_status = (
        ('01', '工作'),
        ('02', '断开'),
        ('FE', '异常'),
        )
    gear_status = (
        ('01', 'P挡'),
        ('02', 'D挡'),
        ('03', 'R挡'),
        ('FE', '其他'),
        )
    brake_status = (
        ('01', '踩下'),
        ('02', '空'),
        ('FE', '其他'),
        )
    serialnum = models.OneToOneField('testcarform', unique=True, null=True, blank=True, verbose_name='内部编号', on_delete=models.CASCADE)
    Statevehicle = models.CharField(choices=Statevehicle_status, max_length=24, unique=False, verbose_name="车辆状态")     # 不可重复
    Chargingstatus = models.CharField(choices=Chargingstatus_status, max_length=24, unique=False, verbose_name="充电状态")     # 不可重复
    carmode = models.CharField(choices=mode_status, max_length=24, unique=False, verbose_name="运行模式")     # 不可重复
    speed = models.FloatField(max_length=48, unique=False, verbose_name="车速")     # 不可重复
    Totalmileage = models.FloatField(max_length=24, unique=False, verbose_name="累计行程")     # 不可重复
    totalvoltage = models.FloatField(max_length=24, unique=False, verbose_name="总电压")     # 不可重复
    totalcurrent = models.FloatField(max_length=24, unique=False, verbose_name="总电流")     # 不可重复
    SOC = models.CharField(max_length=24, unique=False, verbose_name="SOC")     # 不可重复
    DCDC = models.CharField(choices=DCDC_status, max_length=24, unique=False, verbose_name="DC/DC状态")     # 不可重复
    gear = models.CharField(choices=gear_status, max_length=24, unique=False, verbose_name="档位")     # 不可重复
    resistance = models.CharField(max_length=24, unique=False, verbose_name="绝缘电阻")     # 不可重复
    Accelerator = models.CharField(max_length=24, unique=False, verbose_name="加速踏板行程值")     # 不可重复
    brake = models.CharField(choices=brake_status, max_length=24, unique=False, verbose_name="制动踏板形成值")     # 不可重复
    local_time = models.DateTimeField(auto_now_add=False)  # 车辆数据生成时间
    created_time = models.DateTimeField(auto_now_add=True)  # 车辆数据入库时间
    latitude = models.FloatField(max_length=48, unique=False, null=True, blank=True, verbose_name="纬度")     # 不可重复
    longitude = models.FloatField(max_length=48, unique=False, null=True, blank=True, verbose_name="经度")     # 不可重复

class testtorque(models.Model):
    condition_status = (
        ('01', '耗电'),
        ('02', '发电'),
        ('03', '关闭'),
        ('04', '准备'),
        ('FE', '异常'),
        )
    serialnum = models.OneToOneField('testcarform', unique=False, null=True, blank=True, verbose_name='内部编号', on_delete=models.CASCADE)
    condition = models.CharField(choices=condition_status, max_length=24, unique=False, verbose_name="驱动电机状态")     # 不可重复
    torquespeed = models.CharField(max_length=24, unique=False, verbose_name="驱动电机转速")     # 不可重复     # 不可重复
    torque = models.CharField(max_length=24, unique=False, verbose_name="驱动电机转矩")     # 不可重复
    torquetem = models.CharField(max_length=24, unique=False, verbose_name="驱动电机温度")     # 不可重复
    local_time = models.DateTimeField(auto_now_add=False)  # 车辆数据生成时间
    created_time = models.DateTimeField(auto_now_add=True)  # 车辆数据入库时间

class testtorquecontrol(models.Model):
    serialnum = models.OneToOneField('testcarform', unique=False, null=True, blank=True, verbose_name='内部编号', on_delete=models.CASCADE)
    controltem = models.CharField(max_length=24, unique=False, verbose_name="驱动电机控制器温度")     # 不可重复     # 不可重复
    controlV = models.FloatField(max_length=24, unique=False, verbose_name="电机控制器输入电压")     # 不可重复
    controlA =models.FloatField(max_length=24, unique=False, verbose_name="电机控制器直流母线电流")     # 不可重复
    local_time = models.DateTimeField(auto_now_add=False)  # 车辆数据生成时间
    created_time = models.DateTimeField(auto_now_add=True)  # 车辆数据入库时间

class testbigv(models.Model):
    serialnum = models.ForeignKey('testcarform', unique=False, null=True, blank=True, verbose_name='内部编号', on_delete=models.CASCADE)
    systemnum = models.CharField(max_length=24, unique=False, verbose_name="最高电压电池子系统号")     # 不可重复     # 不可重复
    bigbattery = models.CharField(max_length=24, unique=False, verbose_name="最高电压电池单体代号")     # 不可重复
    bigv =models.FloatField(max_length=24, unique=False, verbose_name="电池单体电压最高值")     # 不可重复
    local_time = models.DateTimeField(auto_now_add=False)  # 车辆数据生成时间
    created_time = models.DateTimeField(auto_now_add=True)  # 车辆数据入库时间

class testbattery(models.Model):
    serialnum = models.ForeignKey('testcarform', unique=False, null=True, blank=True, verbose_name='内部编号', on_delete=models.CASCADE)
    systemv = models.FloatField(max_length=24, unique=False, verbose_name="可充电储能装置电压")     # 不可重复     # 不可重复
    systema = models.FloatField(max_length=24, unique=False, verbose_name="可充电储能装置电流")     # 不可重复
    batterynum = models.CharField(max_length=24, unique=False, verbose_name="单体电池总数")     # 不可重复
    battery01 =models.FloatField(max_length=24, unique=False, verbose_name="单体电池电压")     # 不可重复
    battery02 =models.FloatField(max_length=24, unique=False, verbose_name="单体电池电压")     # 不可重复
    battery03 =models.FloatField(max_length=24, unique=False, verbose_name="单体电池电压")     # 不可重复
    battery04 =models.FloatField(max_length=24, unique=False, verbose_name="单体电池电压")     # 不可重复
    battery05 =models.FloatField(max_length=24, unique=False, verbose_name="单体电池电压")     # 不可重复
    battery06 =models.FloatField(max_length=24, unique=False, verbose_name="单体电池电压")     # 不可重复
    battery07 =models.FloatField(max_length=24, unique=False, verbose_name="单体电池电压")     # 不可重复
    battery08 =models.FloatField(max_length=24, unique=False, verbose_name="单体电池电压")     # 不可重复
    battery09 =models.FloatField(max_length=24, unique=False, verbose_name="单体电池电压")     # 不可重复
    battery10 =models.FloatField(max_length=24, unique=False, verbose_name="单体电池电压")     # 不可重复
    battery11 =models.FloatField(max_length=24, unique=False, verbose_name="单体电池电压")     # 不可重复
    battery12 =models.FloatField(max_length=24, unique=False, verbose_name="单体电池电压")     # 不可重复
    battery13 =models.FloatField(max_length=24, unique=False, verbose_name="单体电池电压")     # 不可重复
    local_time = models.DateTimeField(auto_now_add=False)  # 车辆数据生成时间
    created_time = models.DateTimeField(auto_now_add=True)  # 车辆数据入库时间

class testwarn(models.Model):
    warnhigh_status = (
        ('01', '1级故障'),
        ('02', '2级故障'),
        ('04', '3级故障'),
        ('03', '正常'),
        ('FE', '异常'),
        )
    warn_status = (
        ('01', '报警'),
        ('02', '正常'),
        ('FE', '异常'),
        )
    serialnum = models.OneToOneField('testcarform', unique=False, null=True, blank=True, verbose_name='内部编号', on_delete=models.CASCADE)
    warnhigh = models.CharField(choices=warnhigh_status, max_length=24, unique=False, verbose_name="最高报警等级")     # 不可重复
    warn001 = models.CharField(choices=warn_status, max_length=24, unique=False, verbose_name="温度差异报警")     # 不可重复     # 不可重复
    warn002 = models.CharField(choices=warn_status, max_length=24, unique=False, verbose_name="电池高温报警")
    warn003 = models.CharField(choices=warn_status, max_length=24, unique=False, verbose_name="车载储能装置类型过压报警")     # 不可重复     # 不可重复
    warn004 = models.CharField(choices=warn_status, max_length=24, unique=False, verbose_name="车载储能装置类型欠压报警")
    warn005 = models.CharField(choices=warn_status, max_length=24, unique=False, verbose_name="SOC低报警")     # 不可重复     # 不可重复
    warn006 = models.CharField(choices=warn_status, max_length=24, unique=False, verbose_name="单体电池过压报警")
    warn007 = models.CharField(choices=warn_status, max_length=24, unique=False, verbose_name="单体电池欠压报警")     # 不可重复     # 不可重复
    warn008 = models.CharField(choices=warn_status, max_length=24, unique=False, verbose_name="SOC过高报警")
    warn009 = models.CharField(choices=warn_status, max_length=24, unique=False, verbose_name="SOC跳变报警")     # 不可重复     # 不可重复
    warn010 = models.CharField(choices=warn_status, max_length=24, unique=False, verbose_name="可充电储能系统不匹配报警")
    warn011 = models.CharField(choices=warn_status, max_length=24, unique=False, verbose_name="电池单体一致性报警")     # 不可重复     # 不可重复
    warn012 = models.CharField(choices=warn_status, max_length=24, unique=False, verbose_name="绝缘报警")
    warn013 = models.CharField(choices=warn_status, max_length=24, unique=False, verbose_name="DC-DC温度报警")     # 不可重复     # 不可重复
    warn014 = models.CharField(choices=warn_status, max_length=24, unique=False, verbose_name="制动系统报警")
    warn015 = models.CharField(choices=warn_status, max_length=24, unique=False, verbose_name="DC-DC状态报警")     # 不可重复     # 不可重复
    warn016 = models.CharField(choices=warn_status, max_length=24, unique=False, verbose_name="驱动电机控制器温度报警")
    warn017 = models.CharField(choices=warn_status, max_length=24, unique=False, verbose_name="高压互锁状态报警")
    warn018 = models.CharField(choices=warn_status, max_length=24, unique=False, verbose_name="驱动电机温度报警")     # 不可重复     # 不可重复
    warn019 = models.CharField(choices=warn_status, max_length=24, unique=False, verbose_name="车载储能装置类型过充")
    local_time = models.DateTimeField(auto_now_add=False)  # 车辆数据生成时间
    created_time = models.DateTimeField(auto_now_add=True)  # 车辆数据入库时间


class zjgzm(models.Model):
    DTC = models.CharField(max_length=24, unique=True, verbose_name="故障代码")     # 不可重复     # 不可重复
    DTC_explain = models.CharField(max_length=256, unique=False, verbose_name="故障代码信息")     # 不可重复
    local_time = models.DateTimeField(auto_now_add=False)  # 车辆数据生成时间
    created_time = models.DateTimeField(auto_now_add=True)  # 车辆数据入库时间

class realpost(models.Model):
    """    所有资产的共有数据表    """
    Statevehicle_status = (
        ('01', '启动'),
        ('02', '熄火'),
        ('03', '其他'),
        ('FE', '异常'),
        )

    serialnum = models.OneToOneField('testcarform', null=True, unique=True, blank=True, verbose_name='内部编号', on_delete=models.CASCADE)
    speed = models.FloatField(max_length=48, unique=False, verbose_name="车速")     # 不可重复

class morepost(models.Model):
    """    所有资产的共有数据表    """
    Statevehicle_status = (
        ('01', '启动'),
        ('02', '熄火'),
        ('03', '其他'),
        ('FE', '异常'),
        )

    serialnum = models.ForeignKey('testcarform', unique=False, null=True, blank=True, verbose_name='内部编号', on_delete=models.CASCADE)
    Statevehicle = models.CharField(choices=Statevehicle_status, max_length=24, unique=False, verbose_name="车辆状态")     # 不可重复
    speed = models.FloatField(max_length=48, unique=False, verbose_name="车速")     # 不可重复

class realpost01(models.Model):
    """    所有资产的共有数据表    """
    Statevehicle_status = (
        ('01', '启动'),
        ('02', '熄火'),
        ('03', '其他'),
        ('FE', '异常'),
        )

    serialnum = models.OneToOneField('testcarform', primary_key=True, unique=True, blank=True, verbose_name='内部编号', on_delete=models.CASCADE)
    speed = models.FloatField(max_length=48, unique=False, verbose_name="车速")     # 不可重复
    Statevehicle = models.CharField(choices=Statevehicle_status, max_length=24, unique=False, verbose_name="车辆状态")     # 不可重复

class realpost02(models.Model):
    """    所有资产的共有数据表    """
    Statevehicle_status = (
        ('01', '启动'),
        ('02', '熄火'),
        ('03', '其他'),
        ('FE', '异常'),
        )

    serialnum = models.OneToOneField('testcarform', primary_key=True, unique=True, blank=True, verbose_name='内部编号', on_delete=models.CASCADE)
    speed = models.FloatField(max_length=48, unique=False, verbose_name="车速")     # 不可重复
    Statevehicle = models.CharField(choices=Statevehicle_status, max_length=24, unique=False, verbose_name="车辆状态")     # 不可重复