
from django import forms
from .models import Note, BulletinBoardPost

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'tags']  # Include tags

class BulletinBoardPostForm(forms.ModelForm):
    class Meta:
        model = BulletinBoardPost
        fields = ['title', 'content']
