from django import forms
from .models import Post

class PostAdminForm(forms.ModelForm):
    images = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
        required=False,
        label="آپلود تصاویر"
    )

    class Meta:
        model = Post
        fields = '__all__'
