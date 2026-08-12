from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.urls import reverse
from .models import Comment, Like
from .forms import CommentForm, EditCommentForm
from wagtail.models import Page

from django.template.loader import get_template

from django.http import HttpResponse
from django.template.loader import render_to_string


@login_required
def add_comment(request, article_id):
    article = get_object_or_404(Page, id=article_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            parent_id = form.cleaned_data.get('parent_id')
            if parent_id:
                comment.parent = get_object_or_404(Comment, id=parent_id)
            comment.save()
    # После сохранения редиректим обратно на страницу статьи
    return redirect(article.url)


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.author != request.user:
        return HttpResponseForbidden("Вы не можете редактировать этот комментарий.")

    if request.method == 'POST':
        form = EditCommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            # Редирект на статью с сохранением страницы
            page = request.GET.get('page', 1)
            return redirect(f"{comment.article.url}?page={page}")
    else:
        form = EditCommentForm(instance=comment)

    # ВАЖНО: передаём request в контекст, чтобы он был доступен в base.html
    return render(request, 'comments/edit_comment.html', {
        'form': form,
        'comment': comment,
        'request': request,   # ← явно добавляем
    })


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    if comment.author != request.user:
        return HttpResponseForbidden("Вы не можете удалить этот комментарий.")
    
    if request.method == 'POST':
        # Удаляем комментарий (каскадно удалятся и все ответы, если они есть)
        article_url = comment.article.url
        page = request.GET.get('page', 1)
        comment.delete()
        return redirect(f"{article_url}?page={page}")
    
    return render(request, 'comments/delete_comment.html', {
        'comment': comment,
    })


@login_required
def toggle_like(request, comment_id):
    print("===== toggle_like called, comment_id:", comment_id)  # отладка
    comment = get_object_or_404(Comment, id=comment_id)
    page = request.GET.get('page', 1)
    
    if comment.author == request.user:
        return redirect(f"{comment.article.url}?page={page}")
    
    like, created = Like.objects.get_or_create(user=request.user, comment=comment)
    if not created:
        like.delete()
    return redirect(f"{comment.article.url}?page={page}")


