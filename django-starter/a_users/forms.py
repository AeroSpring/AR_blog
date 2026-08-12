from django.forms import ModelForm
from django import forms
from .models import CustomUser

class ProfileForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_image', 'displayname', 'info']
        widgets = {
            'profile_image': forms.FileInput(),
            'displayname' : forms.TextInput(attrs={'placeholder': 'Add display name'}),
            'info' : forms.Textarea(attrs={'rows':3, 'placeholder': 'Add information'})
        }
        
        
class EmailForm(ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['email']