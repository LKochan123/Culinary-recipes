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
