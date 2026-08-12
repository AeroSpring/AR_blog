from django.db import models
from django.conf import settings
from django.utils import timezone
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet


@register_setting
class ContactSettings(BaseSiteSetting):
    email = models.EmailField(verbose_name="E-mail", blank=True)
    phone = models.CharField(max_length=20, verbose_name="Телефон", blank=True)

    class Meta:
        verbose_name = "Контактная информация"
        verbose_name_plural = "Контактная информация"


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор")
    text = models.TextField(max_length=2000, verbose_name="Текст отзыва")
    rating = models.PositiveSmallIntegerField(
        choices=[(i, f"{i} баллов") for i in range(1, 6)],
        default=5,
        verbose_name="Оценка"
    )
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"Отзыв от {self.user.username} ({self.rating})"


# ----- Услуги (сниппеты) -----
@register_snippet
class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название услуги")
    days_min = models.PositiveIntegerField(verbose_name="Дней (от)")
    days_max = models.PositiveIntegerField(verbose_name="Дней (до)")
    is_active = models.BooleanField(default=True, verbose_name="Активно")

    panels = [
        FieldPanel('name'),
        FieldPanel('days_min'),
        FieldPanel('days_max'),
        FieldPanel('is_active'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ['name']


# ----- Стоимость дня работы (настройки сайта) -----
@register_setting
class CalculatorSettings(BaseSiteSetting):
    cost_per_day = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        verbose_name="Стоимость дня работы",
        default=200000
    )

    panels = [
        FieldPanel('cost_per_day'),
    ]

    class Meta:
        verbose_name = "Настройки калькулятора"
        verbose_name_plural = "Настройки калькулятора"
