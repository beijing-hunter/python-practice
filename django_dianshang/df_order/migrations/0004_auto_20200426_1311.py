# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_order', '0003_orderdetailinfo_istrue'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sales',
            options={'verbose_name_plural': '销量查看'},
        ),
    ]
