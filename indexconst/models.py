# coding: utf-8
from django.db import models
from datetime import datetime


class Index(models.Model):
    """
    指数配置
    """
    name = models.CharField(u'指数名称', max_length=1000)
    loadUrl = models.CharField(u'下载链接', max_length=1000)

    class Meta:
        verbose_name = u'指数配置'
        verbose_name_plural = u'[01].指数配置'

    def __unicode__(self):
        """ """
        return u'(%d)%s' % (self.id, self.name)


class IndexConst(models.Model):
    """
    指数成分数据
    """
    index = models.ForeignKey(Index, verbose_name=u'指数')
    date = models.CharField(u'日期', max_length=20)
    code = models.CharField(u'代码', max_length=20)
    weight = models.FloatField(u'权重')
    flashTime = models.DateTimeField("数据更新", default=datetime.now)

    class Meta:
        verbose_name = u'指数成分'
        verbose_name_plural = u'[01].指数成分'


class HS300Const(models.Model):
    """
    沪深300指数成分数据
    """
    flashTime = models.DateTimeField("数据更新", default=datetime.now)
    date = models.CharField(u'日期', max_length=20)
    code = models.CharField(u'代码', max_length=20)
    weight = models.FloatField(u'权重')

    class Meta:
        verbose_name = u'沪深300指数成分'
        verbose_name_plural = u'[01].沪深300指数成分'


class ZZ500Const(models.Model):
    """
    中证500指数成分数据
    """
    flashTime = models.DateTimeField("数据更新", default=datetime.now)
    date = models.CharField(u'日期', max_length=20)
    code = models.CharField(u'代码', max_length=20)
    weight = models.FloatField(u'权重')

    class Meta:
        verbose_name = u'中证500指数成分'
        verbose_name_plural = u'[02].中证500指数成分'
