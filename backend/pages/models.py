from django.db import models

from backend.abstarct_models import SeoModels, DateModels, PageAbstracts
from django_resized import ResizedImageField


class Settings(DateModels):
    header_id = models.ForeignKey('Header', blank=True, null=True, on_delete=models.CASCADE,
                                  verbose_name='settings_header')
    body_id = models.ForeignKey('Body', blank=True, null=True, on_delete=models.CASCADE, verbose_name='settings_body')
    footer_id = models.ForeignKey('Footer', blank=True, null=True, on_delete=models.CASCADE,
                                  verbose_name='settings_footer')

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'


class Header(PageAbstracts):
    class Meta:
        verbose_name = 'Header'
        verbose_name_plural = 'Header'


class Body(PageAbstracts):
    class Meta:
        verbose_name = 'Header'
        verbose_name_plural = 'Header'


class Footer(PageAbstracts):
    class Meta:
        verbose_name = 'Header'
        verbose_name_plural = 'Header'


class Page(SeoModels, DateModels):
    image_id = models.ManyToManyField('ImagePage')
    pass


class ImagePage(models.Model):
    image = ResizedImageField(size=[500, 300], upload_to='image_page', blank=True, null=True)
