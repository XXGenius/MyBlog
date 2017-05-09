
from django.forms import ModelForm

from article.models import Comments, Article


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = [ 'comments_text']


class ArticleForm(ModelForm):
    class Meta:
          model= Article
          fields = ['title', 'text', 'img', 'category']
