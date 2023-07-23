# 커스텀 필터를 만들 것
# content를 받아와 해시태그만 a태그로 변경
from django import template
from articles.models import Hashtag
from django.shortcuts import resolve_url
from django.utils.safestring import mark_safe

register = template.Library()

# 내가 만든 커스텀 함수
# value: content가 넘어옴
# arg: 뒤에 작성한 내용
@register.filter
def set_hashtag(value):
    contents = value.replace('\r\n', ' ').split(' ')
    for i in range(len(contents)):
        if contents[i].startswith('#'):
            hashtag = contents[i][1:]
            # #으로 시작하는 모든 단어는 무조건 해시태그다!!!
            try:
                hashtag_obj = Hashtag.objects.get(content=hashtag)
                contents[i] = f'<a href="{resolve_url("articles:hashtag", hashtag_obj.pk)}">#{hashtag}</a>'
            except Hashtag.DoesNotExist:
                pass
    return mark_safe(' '.join(contents))

# 커스텀 함수를 filter에 등록
# 데코레이터 대신
# register.filter('set_hashtag', set_hashtag)