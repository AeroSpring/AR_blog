from django import template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..models import Comment, Like

register = template.Library()

@register.inclusion_tag('comments/comment_tree.html', takes_context=True)
def render_comments(context, article):
    request = context.get('request')
    # Получаем только корневые комментарии
    root_comments = article.comments.filter(parent__isnull=True)

    paginator = Paginator(root_comments, 2)  # 10 комментариев на страницу

    page_num = request.GET.get('page', 1) if request else 1
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return {
        'page_obj': page_obj,
        'article': article,
        'request': request,
    }

@register.filter
def is_liked_by(comment, user):
    return comment.comment_likes.filter(user=user).exists()
