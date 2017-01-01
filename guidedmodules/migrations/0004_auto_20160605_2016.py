# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-05 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guidedmodules', '0003_auto_20160603_1828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskanswerhistory',
            name='answered_by_task',
        ),
        migrations.AddField(
            model_name='taskanswerhistory',
            name='answered_by_task',
            field=models.ManyToManyField(blank=True, help_text="A Task or Tasks that supplies the answer for this question (of type 'module' or 'module-set').", related_name='is_answer_to', to='guidedmodules.Task'),
        ),
    ]