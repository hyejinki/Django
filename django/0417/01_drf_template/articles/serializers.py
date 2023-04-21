from rest_framework import serializers
from .models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)


class ArticleListSerializer(serializers.ModelSerializer):
    # Comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    class Meta:
        model = Article
        # fields = ('id', 'title', 'content')
        fields = '__all__'

    # Model에 없는 필드를 자유롭게 추가
    #  -> 모델이 가진 데이터에 따라 다른 필드를 추가하거나, 데이터를 변경하고 싶을 때
    def to_representations(self, instance):    
        rep = super().to_representations(instance)

        # comment_count 를 추가
        rep['comments_count'] = instance.comment_set.count()
        #출력할때만 아래 데이터를 추가해줌
        rep['type'] = 'test'
        return rep
