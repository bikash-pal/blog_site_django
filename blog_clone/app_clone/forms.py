from django import forms
from django.db.models import fields 
from .models import Comment,Post

class Postform(forms.ModelForm):
    
    class Meta():
        model=Post
        fields=('author','title','text')
        widgets={
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
        }
class CommentForm(forms.ModelForm):
    class Meta():
        model=Comment
        field=('author','text')
        widgets={
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
        }