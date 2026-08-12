from wagtail import hooks
from wagtail.images.formats import Format, register_image_format
from django.utils.html import format_html
import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineStyleElementHandler
from draftjs_exporter.dom import DOM


@hooks.register('register_image_formats')
def override_fullwidth():
    # Удаляем старый fullwidth
    from wagtail.images.formats import image_formats
    image_formats.pop('fullwidth', None)
    
    # Создаём новый fullwidth с высоким качеством
    class HighQualityFullwidth(Format):
        def image_to_html(self, image, alt_text, extra_attributes=None):
            rendition = image.get_rendition('width-800|jpegquality-100')
            return rendition.img_tag(extra_attributes)
    
    register_image_format(
        HighQualityFullwidth('fullwidth', 'Full width', 'richtext-image', 'width-800|jpegquality-100')
    )


# Функция-декоратор, которая гарантирует 100% валидный HTML при сохранении в БД
def red_text_decorator(props):
    return DOM.create_element('span', {
        'style': 'color: #ff0000;'
    }, props['children'])

@hooks.register('register_rich_text_features')
def register_red_text_feature(features):
    feature_name_red = 'red_text'
    type_red = 'RED_TEXT'
    control_red = {
        'type': type_red,
        'label': 'Красный',
        'description': 'Окрасить выделенный текст в красный цвет',
        'style': {'color': '#ff0000'},
    }
    features.register_editor_plugin(
        'draftail', feature_name_red, draftail_features.InlineStyleFeature(control_red)
    )

    db_conversion_red = {
        'from_database_format': {
            'span[style="color:#ff0000"]': InlineStyleElementHandler(type_red),
            'span[style="color: #ff0000;"]': InlineStyleElementHandler(type_red)
        },
        'to_database_format': {
            'style_map': {
                type_red: red_text_decorator
            }
        },
    }
    features.register_converter_rule('contentstate', feature_name_red, db_conversion_red)
    features.default_features.append('red_text')


# Функция-декоратор, которая гарантирует 100% валидный HTML при сохранении в БД
def green_text_decorator(props):
    return DOM.create_element('span', {
        'style': 'color: #008800;'
    }, props['children'])

@hooks.register('register_rich_text_features')
def register_green_text_feature(features):
    feature_name_green = 'green_text'
    type_green = 'GREEN_TEXT'
    control_green = {
        'type': type_green,
        'label': 'Зеленый',
        'description': 'Окрасить выделенный текст в зеленый цвет',
        'style': {'color': '#008800'},
    }
    features.register_editor_plugin(
        'draftail', feature_name_green, draftail_features.InlineStyleFeature(control_green)
    )

    db_conversion_green = {
        'from_database_format': {
            'span[style="color:#008800"]': InlineStyleElementHandler(type_green),
            'span[style="color: #008800;"]': InlineStyleElementHandler(type_green)
        },
        'to_database_format': {
            'style_map': {
                type_green: green_text_decorator
            }
        },
    }
    features.register_converter_rule('contentstate', feature_name_green, db_conversion_green)
    features.default_features.append('green_text')


# Функция-декоратор, которая гарантирует 100% валидный HTML при сохранении в БД
def blue_text_decorator(props):
    return DOM.create_element('span', {
        'style': 'color: #1d4ed8;'
    }, props['children'])

@hooks.register('register_rich_text_features')
def register_blue_text_feature(features):
    feature_name_blue = 'blue_text'
    type_blue = 'BLUE_TEXT'
    control_blue = {
        'type': type_blue,
        'label': 'Синий',
        'description': 'Окрасить выделенный текст в синий цвет',
        'style': {'color': '#1d4ed8'},
    }
    features.register_editor_plugin(
        'draftail', feature_name_blue, draftail_features.InlineStyleFeature(control_blue)
    )

    db_conversion_blue = {
        'from_database_format': {
            'span[style="color:#1d4ed8"]': InlineStyleElementHandler(type_blue),
            'span[style="color: #1d4ed8;"]': InlineStyleElementHandler(type_blue)
        },
        'to_database_format': {
            'style_map': {
                type_blue: blue_text_decorator
            }
        },
    }
    features.register_converter_rule('contentstate', feature_name_blue, db_conversion_blue)
    # ВОТ ЭТА СТРОКА: автоматически добавляет синий цвет ко всем стандартным кнопкам сайта
    features.default_features.append('blue_text')


# Функция-декоратор, которая гарантирует 100% валидный HTML при сохранении в БД
def gray_text_decorator(props):
    return DOM.create_element('span', {
        'style': 'color: #666666;'
    }, props['children'])

@hooks.register('register_rich_text_features')
def register_gray_text_feature(features):
    feature_name_gray = 'gray_text'
    type_gray = 'GRAY_TEXT'
    control_gray = {
        'type': type_gray,
        'label': 'Серый',
        'description': 'Окрасить выделенный текст в серый цвет',
        'style': {'color': '#666666'},
    }
    features.register_editor_plugin(
        'draftail', feature_name_gray, draftail_features.InlineStyleFeature(control_gray)
    )
    
    db_conversion_grey = {
        'from_database_format': {
            'span[style="color:#666666"]': InlineStyleElementHandler(type_gray),
            'span[style="color: #666666;"]': InlineStyleElementHandler(type_gray)
        },
        'to_database_format': {
            'style_map': {
                type_gray: gray_text_decorator  # Ваш декоратор для серого текста
            }
        },
    }
    features.register_converter_rule('contentstate', feature_name_gray, db_conversion_grey)
    features.default_features.append('gray_text')


