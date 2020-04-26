# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='uaddress',
            field=models.CharField(verbose_name='收件地址', max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uphone',
            field=models.CharField(verbose_name='收件人电话', max_length=11, default=''),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='ushow',
            field=models.CharField(verbose_name='收件人名字', max_length=20, default=''),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uyoubian',
            field=models.CharField(verbose_name='收件邮编', max_length=6, default=''),
        ),
    ]
