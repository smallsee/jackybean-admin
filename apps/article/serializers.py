# -*- coding: utf-8 -*-
__author__ = 'xiaohai'

from rest_framework import serializers


from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"

