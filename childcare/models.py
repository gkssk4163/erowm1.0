# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from accounting.models import Business

# Create your models here.

class Record(models.Model):
    business = models.ForeignKey('accounting.Business', on_delete=models.CASCADE)
    operation = models.CharField(max_length=14)
    year = models.CharField(max_length=4)
    gubun = models.CharField(max_length=2, null=True, blank=True)
    data = models.TextField()
    result_code = models.TextField()
    result_msg = models.TextField()
    regdatetime = models.DateTimeField(default=datetime.now)

    def __str__(self):
        if self.operation == "acRptMonthSum":
            return "%s - %s년 %s월 회계보고" % (self.business, self.year, self.gubun)
        elif self.operation == "acRptBudget":
            if self.gubun == "0":
                return "%s - %s년 본예산보고" % (self.business, self.year)
            else:
                return "%s - %s년 %s차 예산보고" % (self.business, self.year, self.gubun)
        else:
            return "%s - %s년 결산보고" % (self.business, self.year)
