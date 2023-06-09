from django.db import models
from pages.models import Page


class SeoModels(models.Model):
    seo_is_index = models.BooleanField('Индексировать страницу?', default=False)
    seo_title = models.CharField('Название', max_length=255)
    seo_description = models.TextField('Описание')
    seo_keywords = models.CharField('Тэги - ключи', blank=True, null=True, max_length=500)

    class Meta:
        abstract = True


class DateModels(models.Model):
    created_at = models.DateTimeField('Дата добавления', auto_now_add=True)
    last_modified = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        abstract = True


class PageAbstracts(models.Model):
    title = models.CharField('Название', max_length=150, blank=True, null=True, unique=True)
    page_id = models.ForeignKey('Page', blank=True, null=True, on_delete=models.CASCADE, verbose_name='page_header')
    order = models.IntegerField('Порядок', default=1, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.title} | {self.order}'