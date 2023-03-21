from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()


    created_at = models.DateTimeField(auto_now_add=True)
    # 생성 시에만, 현재 시간을 저장
    updated_at = models.DateTimeField(auto_now=True)
    # 생성 시 + 수정 시에 현재 시간을 저장
    
    def __str__(self):
        return f'{self.id}번째글 - {self.title}'