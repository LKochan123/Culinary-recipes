from xml.etree.ElementInclude import include
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "nickname": "Twój nick:",
            "text": "Zostaw komentarz"
        }
        error_messages = {
            "nickname": {
                "required": 'Musisz podać swoją nazwe użytkownika.',
                "max_length": 'Twoja nazwa nie może mieć więcej niż 30 znaków.'
            },
            "text": {
                "max_length": 'Komentarz nie może mieć więcej niż 200 znaków.'
            }
        }
