# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-18 17:01
from __future__ import unicode_literals

import DjangoUeditor.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='文章名')),
                ('desc', models.CharField(max_length=300, verbose_name='文章描述')),
                ('detail', DjangoUeditor.models.UEditorField(default='', verbose_name='文章详情')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏人数')),
                ('image', models.ImageField(max_length=300, upload_to='article/%Y/%m', verbose_name='封面图')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击数')),
                ('tag', models.CharField(choices=[('jl', '交流'), ('dhzx', '动画资讯'), ('qtzx', '其他咨询'), ('fdsw', 'fd事务')], default='jl', max_length=50, verbose_name='本子类型')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
    ]
