# -*- coding: utf-8 -*-
__author__ = 'bobby'

import django_filters
from django.db.models import Q

from .models import Article


class ArticleFilter(django_filters.rest_framework.FilterSet):
    """
    文章的过滤类
    """
    seemin = django_filters.NumberFilter(name='click_nums', help_text="最低观看", lookup_expr='gte')
    seemax = django_filters.NumberFilter(name='click_nums', help_text="最高价格", lookup_expr='lte')
    favmin = django_filters.NumberFilter(name='fav_nums', help_text="最低收藏", lookup_expr='gte')
    favmax = django_filters.NumberFilter(name='fav_nums', help_text="最高收藏", lookup_expr='lte')


    class Meta:
        model = Article
        fields = ['seemin', 'seemax', 'favmin', 'favmax']