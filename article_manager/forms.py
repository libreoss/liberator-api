from django.forms import ModelForm

from article_manager.models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
