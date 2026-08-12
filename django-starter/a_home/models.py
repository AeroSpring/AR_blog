from django.db import models
from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.fields import RichTextField
from modelcluster.fields import ParentalKey

class HomePage(Page):
    # Поля для дополнительного контента (можно оставить для других целей)
    # Основные блоки будут через InlinePanel
    subheading = models.CharField(max_length=255, blank=True, verbose_name="Подзаголовок")
    # ...

    content_panels = Page.content_panels + [
        FieldPanel('subheading'),
        InlinePanel('blocks', label="Блоки на главной"),
    ]

    class Meta:
        verbose_name = "Главная страница"
        verbose_name_plural = "Главные страницы"

class HomeBlock(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='blocks')
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    text = RichTextField(verbose_name="Текст", blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Изображение"
    )
    # Можно добавить иконку или цвет, если нужно

    panels = [
        FieldPanel('title'),
        FieldPanel('text'),
        FieldPanel('image'),
    ]

    class Meta:
        ordering = ['sort_order']
        verbose_name = "Блок"
        verbose_name_plural = "Блоки"
