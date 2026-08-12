from wagtail.images.formats import Format, register_image_format
from django.utils.html import format_html

class MaxQualityFormat(Format):
    def image_to_html(self, image, alt_text, extra_attributes=None):
        # Получаем оригинальное изображение (без изменения размера и сжатия)
        # Если нужно изменить размер, но с высоким качеством, можно использовать
        # image.get_rendition('width-800|jpegquality-100')
        rendition = image.get_rendition('original')
        return rendition.img_tag(extra_attributes)

# Регистрируем новый формат с именем 'max_quality'
register_image_format(
    MaxQualityFormat('max_quality', 'Максимальное качество', 'richtext-image', 'original')
)