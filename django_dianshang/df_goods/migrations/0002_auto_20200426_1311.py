# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='gpic',
            field=models.ImageField(verbose_name='图片', upload_to='df_goods'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gunit',
            field=models.CharField(verbose_name='单位', max_length=20, default='500g'),
        ),
    ]
