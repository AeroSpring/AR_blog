from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Напишите ваш отзыв...'}),
            'rating': forms.Select(attrs={'class': 'rating-select'}),  # можно заменить на звёзды позже
        }
