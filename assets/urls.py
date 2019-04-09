#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.conf.urls import url
from assets import views

app_name = 'assets'

urlpatterns = [
    url(r'^testrealpost/', views.zsreal, name='zsreal'),
    url(r'^testmorepost/', views.zsmore, name='zsmore'),
    url('hello01/', views.testmorepost),
    url('hello/', views.testpost),
    url(r'^tyjc/', views.tyjc, name='tyjc'),
    url(r'^zjgzm/', views.zjgzm, name='zjgzm'),
    url(r'^testzcsj/', views.testzcsj, name='testzcsj'),
    url(r'^testclxx/', views.testclxx, name='testclxx'),
    url(r'^testjwd/', views.testjwd, name='testjwd'),
    url(r'^testqd/', views.testqd, name='testqd'),
    url(r'^testqdkz/', views.testqdkz, name='testqdkz'),
    url(r'^testzgdy/', views.testzgdy, name='testzgdy'),
    url(r'^testdcdy/', views.testdcdy, name='testdcdy'),
    url(r'^testwarn/', views.testwarn, name='testwarn'),
    url(r'^report/', views.report, name='report'),
    url(r'^login/', views.login, name='login'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^index/', views.index, name='index'),
    url(r'^formreal/', views.formreal, name='formreal'),
    url(r'^linechart/', views.linechart, name='linechart'),
    url(r'^linechart1/', views.linechart1, name='linechart1'),
    url(r'^ajaxtable/ajax_json/', views.ajax_json, name='ajax_json'),
    url(r'^ajaxtable/', views.ajaxtable, name='ajaxtable'),
    url(r'^ajaxcircle/ajax_data/', views.ajax_data, name='ajax_data'),
    url(r'^ajaxcircle/', views.ajaxcircle, name='ajaxcircle'),
    url(r'^realcircle/real_data/', views.real_data, name='real_data'),
    url(r'^realcircle/', views.realcircle, name='realcircle'),
    url(r'^detail/(?P<asset_id>[0-9]+)/$', views.detail, name="detail"),
    url(r'^$', views.dashboard),
]
