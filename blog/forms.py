from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Post

class Postform(forms.ModelForm):

    conteudo = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ('title','conteudo','imagem','status')
