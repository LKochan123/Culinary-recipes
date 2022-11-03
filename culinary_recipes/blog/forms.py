from xml.etree.ElementInclude import include
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {
            "text": "Zostaw komentarz"
        }
        error_messages = {
            "text": {
                "max_length": 'Komentarz nie może mieć więcej niż 500 znaków.'
            }
        }
