from django import forms
from .models import Post
import json
import os

class PostAdminForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        json_path = os.path.join(os.path.dirname(__file__), 'iran_all_provinces.json')
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        provinces = [(p['province'], p['province']) for p in data]
        self.fields['province'].widget = forms.Select(choices=provinces)


