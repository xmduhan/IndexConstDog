#!/usr/bin/env python
# encoding: utf-8

from __future__ import division
from subprocess import call
import pandas as pd
from indexconst.models import Index, IndexConst


def flashIndexConst(index):
    """
    更新指数的成分数据
    """
    #  获取链接信息
    filename = 'weight.xls'
    url = index.loadUrl

    # 下载文件
    call(['rm', filename])
    result = call(['wget', url, '-O', filename])
    if result != 0:
        raise Exception(u'下载文件失败')
    print u'|--文件下载成功...'

    # 读取文件并转化格式
    df = pd.io.excel.read_excel(filename)
    df = df[['Date', 'Constituent Code', 'Weight(%)']]
    df.columns = ['date', 'code', 'weight']
    df['code'] = df.code.apply(lambda x: str(x).zfill(6))
    df['weight'] = df['weight'] / 100
    print u'|--数据格式转化完成...'

    # 保存到参数表
    for i, row in df.iterrows():
        date = row['date']
        code = row['code']
        weight = row['weight']
        IndexConst(index=index, date=date, code=code, weight=weight).save()
    print u'|--保存在数据库完成...'


def run():
    """
    更新所有指数数据
    """
    for index in Index.objects.all():
        print u'%s:开始更新' % index.name
        try:
            flashIndexConst(index)
            print u'%s:更新完成' % index.name
        except:
            print u'%s:出错...' % index.name
