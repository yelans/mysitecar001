from django.contrib import admin
# Register your models here.
from assets import models
from . import asset_handler
from .models import Carform,Carformtest,Carrealtimetest,Motor,Motortest,Motortest1,testcarform,testcarrealtime,testtorque,testtorquecontrol,testbigv,testbattery,testwarn,zjgzm\
                                                    ,realpost,morepost,realpost01,realpost02

class NewAssetAdmin(admin.ModelAdmin):
    list_display = ['asset_type', 'sn', 'model', 'manufacturer', 'c_time', 'm_time']
    list_filter = ['asset_type', 'manufacturer', 'c_time']
    search_fields = ('sn',)

    actions = ['approve_selected_new_assets']

    def approve_selected_new_assets(self, request, queryset):
        # 获得被打钩的checkbox对应的资产
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        success_upline_number = 0
        for asset_id in selected:
            obj = asset_handler.ApproveAsset(request, asset_id)
            ret = obj.asset_upline()
            if ret:
                success_upline_number += 1
        # 顶部绿色提示信息
        self.message_user(request, "成功批准  %s  条新资产上线！" % success_upline_number)
    approve_selected_new_assets.short_description = "批准选择的新资产"

@admin.register(realpost02)
class realpost02Admin(admin.ModelAdmin):
    list_display = ['serialnum', 'speed', 'Statevehicle']

@admin.register(realpost01)
class realpost01Admin(admin.ModelAdmin):
    list_display = ['serialnum', 'speed', 'Statevehicle']

@admin.register(realpost)
class realpostAdmin(admin.ModelAdmin):
    list_display = ['serialnum', 'speed']

@admin.register(morepost)
class morepostAdmin(admin.ModelAdmin):
    list_display = ['serialnum', 'speed']

class AssetAdmin(admin.ModelAdmin):
    list_display = ['asset_type', 'name', 'status', 'approved_by', 'c_time', "m_time"]

@admin.register(zjgzm)
class zjgzmAdmin(admin.ModelAdmin):
    list_display = ('id', 'DTC', 'DTC_explain', 'local_time')

@admin.register(Carform)
class CarformAdmin(admin.ModelAdmin):
    list_display = ('id', 'Car_VIN', 'Carname', 'License_number', 'Serure_number', 'created_time')

@admin.register(Carformtest)
class CarformtestAdmin(admin.ModelAdmin):
    list_display = ('id', 'Car_VIN', 'Carname', 'Carnickname', 'License_number', 'Serure_number', 'created_time')

@admin.register(Carrealtimetest)
class CarrealtimetestAdmin(admin.ModelAdmin):
    list_display = ('id', 'Carnickname', 'Statevehicle', 'Chargingstatus', 'speed', 'Totalmileage', 'totalvoltage', \
                    'totalcurrent', 'SOC', 'DC_DC', 'gear', 'resistance', 'Accelerator', 'brake', 'local_time', 'created_time')

@admin.register(Motor)
class MotorAdmin(admin.ModelAdmin):
    list_display = ('id', 'Carformtest', 'Totalmileage', 'totalvoltage', 'totalcurrent', 'Totalmileage', 'local_time', 'created_time')

@admin.register(Motortest)
class MotortestAdmin(admin.ModelAdmin):
    list_display = ('id', 'Carformtest', 'torque', 'torquespeed', 'torquecurrent', 'torquemileage', 'local_time', 'created_time')

@admin.register(Motortest1)
class Motortest1Admin(admin.ModelAdmin):
    list_display = ('id', 'Carformtest', 'torque', 'torquespeed', 'torquecurrent', 'torquemileage', 'time', 'created_time')

@admin.register(testcarform)
class testcarformAdmin(admin.ModelAdmin):
    list_display = ('CarVIN', 'Carname', 'Licensenumber', 'serialnum', 'Serurenumber', 'createdtime')

@admin.register(testcarrealtime)
class testcarrealtimeAdmin(admin.ModelAdmin):
    list_display = ('serialnum', 'Statevehicle', 'Chargingstatus', 'carmode', 'speed', 'Totalmileage', \
                    'totalvoltage', 'totalcurrent', 'SOC', 'DCDC', 'gear', 'resistance', \
                    'Accelerator', 'brake', 'local_time', 'created_time', 'latitude', 'longitude' )

@admin.register(testtorque)
class testtorqueAdmin(admin.ModelAdmin):
    list_display = ('serialnum', 'condition', 'torquespeed', 'torque', 'torquetem', 'local_time')

@admin.register(testtorquecontrol)
class testtorquecontrolAdmin(admin.ModelAdmin):
    list_display = ('serialnum', 'controltem', 'controlV', 'controlA', 'local_time')

@admin.register(testbigv)
class testbigvAdmin(admin.ModelAdmin):
    list_display = ('serialnum', 'systemnum', 'bigbattery', 'bigv', 'local_time')

@admin.register(testbattery)
class testbatteryAdmin(admin.ModelAdmin):
    list_display = ('serialnum', 'systemv', 'systema', 'batterynum', 'battery01', 'battery02', 'battery03', \
                    'battery04', 'battery05', 'battery06', 'battery07', 'battery08', 'battery09', 'battery10', \
                    'battery11', 'battery12', 'battery13', 'local_time')

@admin.register(testwarn)
class testwarnAdmin(admin.ModelAdmin):
    list_display = ('serialnum', 'warnhigh', 'warn001', 'warn002', 'warn003', 'warn004', 'warn005', \
                    'warn006', 'warn007', 'warn008', 'warn009', 'warn010', 'warn011', 'warn012', \
                    'warn013', 'warn014', 'warn015', 'warn016', 'warn017', 'warn018', 'warn019', 'local_time')

admin.site.register(models.Asset, AssetAdmin)
admin.site.register(models.Server)
admin.site.register(models.StorageDevice)
admin.site.register(models.SecurityDevice)
admin.site.register(models.BusinessUnit)
admin.site.register(models.Contract)
admin.site.register(models.CPU)
admin.site.register(models.Disk)
admin.site.register(models.EventLog)
admin.site.register(models.IDC)
admin.site.register(models.Manufacturer)
admin.site.register(models.NetworkDevice)
admin.site.register(models.NIC)
admin.site.register(models.RAM)
admin.site.register(models.Software)
admin.site.register(models.Tag)
admin.site.register(models.NewAssetApprovalZone, NewAssetAdmin)
