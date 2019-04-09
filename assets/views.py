from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
import json
import time
import datetime
from . import models
from . import asset_handler
# Create your views here.
from django.shortcuts import get_object_or_404
from django.core import serializers
#import binascii
from django.core.serializers.json import DjangoJSONEncoder
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

@csrf_exempt
def testmorepost(request):
    if request.method == 'POST':  # 当提交表单时
        dic={}
        # 判断是否传参
        if request.body:
            a = request.body
            b = request.META.get('HTTP_CARNUM')
            #a = b'a'
            #a = binascii.hexlify(a)
            #key = 'keyskeyskeyskeys'
            #key = key.encode('utf-8')
            #mode = AES.MODE_CBC
            #a = decryptnokey()
            a = asset_handler.decryptnokey('keyskeyskeyskeys', 'keyskeyskeyskeys', a)
                    #key = 'keyskeyskeyskeys'
                    #key = key.encode('utf-8')
                    #mode = AES.MODE_CBC
                    #cryptor = AES.new(key, mode, b'keyskeyskeyskeys')
                    #plain_text = cryptor.decrypt(a2b_hex(b'291eaa8cf017960eb0ad5ed373477637'))
            # return plain_text.rstrip('\0')
            #return bytes.decode(plain_text).rstrip('\0')
            #a = bytes.decode(plain_text).rstrip('\0')
            print(a)
            #print('更新成功！')
            a = str(a)
            print(type(a))
            testspeed = a[6:9]
            print(a)
            print(b)
            print(testspeed)
            #testserialnum = a[0:6]
            #testserialnum = int(testserialnum)
            #testspeed = a[6:9]
            #testspeed = float(testspeed)
            ##qb = models.realpost.objects.all()
            #serialnum = models.testcarform.objects.get(serialnum=testserialnum)
            #carname = serialnum.Carname
            #qb = models.morepost(serialnum = serialnum, speed = testspeed, Statevehicle = '01')
            ##qb.serialnum = 100001
            ##qb.speed = 99.9
            #qb.save()
            return HttpResponse(1)
    else:
        return HttpResponse('4')

@csrf_exempt
def testpost(request):
    if request.method == 'POST':  # 当提交表单时
        dic={}
        # 判断是否传参
        if request.body:
            #qb = models.realpost.objects.all()
            a = request.body
            b = request.META.get('HTTP_CARNUM')
            serialnum = models.testcarform.objects.get(serialnum=b)
            sta = a[0:2]
            speed = a[2:6]
            sta = int(sta, 16)
            if sta == 1:
                sta = '01'
            elif sta == 2:
                sta = '02'
            else:
                sta = 'FE'
            speed = int(speed, 16)
            speed = float(speed)/10
            qb = models.realpost02(serialnum = serialnum, speed = speed, Statevehicle = sta)
            #qb.serialnum = 100001
            #qb.speed = 99.9
            qb.save()
            a= request.body
            return HttpResponse(a)
    else:
        return HttpResponse('4')

def zsreal(request):
    carzsreal = models.realpost.objects.all()
    return render(request, 'assets/testrealpost.html', locals())

def zsmore(request):
    carzsmore = models.morepost.objects.all()
    return render(request, 'assets/testmorepost.html', locals())

def tyjc(request):
    carqd = models.testtorque.objects.all()
    tagsdefault = 'cartest000001'
    return render(request, 'assets/tyjc.html', locals())

def zjgzm(request):
    carqd = models.testtorque.objects.all()
    gzm = models.zjgzm.objects.all()
    tagsdefault = 'cartest000001'
    return render(request, 'assets/zjgzm.html', locals())


def testzcsj(request):
    carreal = models.testcarrealtime.objects.all()
    return render(request, 'assets/testzcsj.html', locals())

def testclxx(request):
    carinfor = models.testcarform.objects.all()
    return render(request, 'assets/testclxx.html', locals())

def testjwd(request):
    carreal = models.testcarrealtime.objects.all()
    return render(request, 'assets/testjwd.html', locals())

def testqd(request):
    carqd = models.testtorque.objects.all()
    tagsdefault = 'cartest001'
    return render(request, 'assets/testqd.html', locals())

def testqdkz(request):
    carqdkz = models.testtorquecontrol.objects.all()
    return render(request, 'assets/testqdkz.html', locals())

def testzgdy(request):
    carzgdy = models.testbigv.objects.filter(serialnum_id=100001)
    carinfor = models.testcarform.objects.all()
    tagsdefault = 'cartest000001'
    return render(request, 'assets/testzgdy.html', locals())

def testdcdy(request):
    cardcdy = models.testbattery.objects.filter(serialnum_id=100001)
    carinfor = models.testcarform.objects.all()
    tagsdefault = 'cartest000001'
    return render(request, 'assets/testdcdy.html', locals())

def testwarn(request):
    cardcdy = models.testwarn.objects.all().order_by('serialnum_id')
    carinfor = models.testcarform.objects.all()
    tagsdefault = 'cartest000001'
    return render(request, 'assets/testwarn.html', locals())

def index(request):
    assets = models.Asset.objects.all()
    return render(request, 'assets/index.html', locals())

def login(request):
    return render(request, 'assets/login.html')

def formreal(request):
    carreal = models.Carrealtimetest.objects.all()
    tagsdefault = 'cartest001'
    return render(request, 'assets/formreal.html', locals())

def linechart(request):
    moto = models.Motortest.objects.filter(Carformtest = 1).values_list('local_time', 'torquespeed').order_by('local_time')
    moto_dict = dict(moto)
    x_time = list(moto_dict)
    for i in range(len(x_time)):
        x_time[i] = x_time[i].strftime("%Y-%m-%d %H:%M:%S")
    y_data = list(moto_dict.values())
    return render(request, 'assets/linechart.html', locals())

def linechart1(request):
    moto = models.Motortest1.objects.filter(Carformtest = 1).values_list('time', 'torquespeed').order_by('time')
    moto_dict = dict(moto)
    x_time = list(moto_dict)
    y_data = list(moto_dict.values())
    return render(request, 'assets/linechart1.html', locals())

def dashboard(request):
    total = models.Asset.objects.count()
    upline = models.Asset.objects.filter(status=0).count()
    offline = models.Asset.objects.filter(status=1).count()
    unknown = models.Asset.objects.filter(status=2).count()
    breakdown = models.Asset.objects.filter(status=3).count()
    backup = models.Asset.objects.filter(status=4).count()
    up_rate = round(upline/total*100)
    o_rate = round(offline/total*100)
    un_rate = round(unknown/total*100)
    bd_rate = round(breakdown/total*100)
    bu_rate = round(backup/total*100)
    server_number = models.Server.objects.count()
    networkdevice_number = models.NetworkDevice.objects.count()
    storagedevice_number = models.StorageDevice.objects.count()
    securitydevice_number = models.SecurityDevice.objects.count()
    software_number = models.Software.objects.count()

    return render(request, 'assets/dashboard.html', locals())

@csrf_exempt
def ajaxtable(request):
    return render(request, 'assets/ajaxtable.html')

@csrf_exempt
def ajax_json(request):
    rsp = {"draw":2,"recordsTotal":11,"recordsFiltered":11,"data":[{"id":1,"firstName":"Troy","lastName":"Young"},{"id":2,"firstName":"Alice","lastName":"LL"},{"id":3,"firstName":"Larry","lastName":"Bird"},]}
    return HttpResponse(json.dumps(rsp), content_type="application/json")

@csrf_exempt
def ajaxcircle(request):
    return render(request, 'assets/ajaxcircle.html')

@csrf_exempt
def ajax_data(request):
    rsp = {"data": [{"id": 1, "firstName": "Troy", "lastName": "Young"}, {"id": 2, "firstName": "Alice", "lastName": "LL"}, {"id": 3, "firstName": "Larry", "lastName": "Bird"}]}
    return HttpResponse(json.dumps(rsp), content_type="application/json")

@csrf_exempt
def realcircle(request):
    return render(request, 'assets/realcircle.html')

@csrf_exempt
def real_data(request):
    real_data = {}
    real_list = models.Carrealtimetest.objects.all().values()
    real_data['data'] = list(real_list)
    return HttpResponse(json.dumps(real_data, ensure_ascii=False, cls=DjangoJSONEncoder), content_type="application/json")

def detail(request, asset_id):
    """
    以显示服务器类型资产详细为例，安全设备、存储设备、网络设备等参照此例。
    :param request:
    :param asset_id:
    :return:
    """
    asset = get_object_or_404(models.Asset, id=asset_id)
    return render(request, 'assets/detail.html', locals())


@csrf_exempt
def report(request):
    """
    通过csrf_exempt装饰器，跳过Django的csrf安全机制，让post的数据能被接收，但这又会带来新的安全问题。
    可以在客户端，使用自定义的认证token，进行身份验证。这部分工作，请根据实际情况，自己进行。
    :param request:
    :return:
    """
    if request.method == "POST":
        asset_data = request.POST.get('asset_data')
        data = json.loads(asset_data)
        # 各种数据检查，请自行添加和完善！
        if not data:
            return HttpResponse("没有数据！")
        if not issubclass(dict, type(data)):
            return HttpResponse("数据必须为字典格式！")
        # 是否携带了关键的sn号
        sn = data.get('sn', None)
        if sn:
            # 进入审批流程
            # 首先判断是否在上线资产中存在该sn
            asset_obj = models.Asset.objects.filter(sn=sn)
            if asset_obj:
                # 进入已上线资产的数据更新流程
                update_asset = asset_handler.UpdateAsset(request, asset_obj[0], data)
                return HttpResponse("资产数据已经更新！")
            else:   # 如果已上线资产中没有，那么说明是未批准资产，进入新资产待审批区，更新或者创建资产。
                obj = asset_handler.NewAsset(request, data)
                response = obj.add_to_new_assets_zone()
                return HttpResponse(response)
        else:
            return HttpResponse("没有资产sn序列号，请检查数据！")

@csrf_exempt
def report_0(request):
    """
    通过csrf_exempt装饰器，跳过Django的csrf安全机制，让post的数据能被接收，但这又会带来新的安全问题。
    可以在客户端，使用自定义的认证token，进行身份验证。这部分工作，请根据实际情况，自己进行。
    :param request:
    :return:
    """
    if request.method == "POST":
        asset_data = request.POST.get('asset_data')
        data = json.loads(asset_data)
        # 各种数据检查，请自行添加和完善！
        if not data:
            return HttpResponse("没有数据！")
        if not issubclass(dict, type(data)):
            return HttpResponse("数据必须为字典格式！")
        # 是否携带了关键的sn号
        sn = data.get('sn', None)
        if sn:
            # 进入审批流程
            # 首先判断是否在上线资产中存在该sn
            asset_obj = models.Asset.objects.filter(sn=sn)
            if asset_obj:
                # 进入已上线资产的数据更新流程
                update_asset = asset_handler.UpdateAsset(request, asset_obj[0], data)
                return HttpResponse("资产数据已经更新！")
            else:   # 如果已上线资产中没有，那么说明是未批准资产，进入新资产待审批区，更新或者创建资产。
                obj = asset_handler.NewAsset(request, data)
                response = obj.add_to_new_assets_zone()
                return HttpResponse(response)
        else:
            return HttpResponse("没有资产sn序列号，请检查数据！")

class decryptnokey(object):
    #def __init__(self, key, iv, text):
    def __init__(self):
        key = 'keyskeyskeyskeys'
        self.key = key.encode('utf-8')
        self.mode = AES.MODE_CBC
        self.a = '10000100001'
    #def decrypt(self):
        cryptor = AES.new(self.key, self.mode, b'keyskeyskeyskeys')
        plain_text = cryptor.decrypt(a2b_hex(b'291eaa8cf017960eb0ad5ed373477637'))
        # return plain_text.rstrip('\0')
        #return bytes.decode(plain_text).rstrip('\0')
        a = bytes.decode(plain_text).rstrip('\0')
        print(a)
        print('更新成功！')
    def decrypt(self):
        a = '10000100001'
    def __str__(self):
        return self.a