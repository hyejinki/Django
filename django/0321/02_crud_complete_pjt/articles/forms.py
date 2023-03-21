from django import forms
from .models import Article

# 1. form

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=30)
    content = forms.CharField(widget=forms.Textarea)
    # widget: form 이 지원하는 기본 기능 외의 추가적인 동작을 원할 때 사용

# 2. modelform

class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        # 원하는 필드만 입력 받겠다 tuple or list
        # fields = ('title', 'content', 'author')
        # 전체
        fields = '__all__'

        # 특정 필드 제외하고 입력 받겠다
        # exclude = ('author', )