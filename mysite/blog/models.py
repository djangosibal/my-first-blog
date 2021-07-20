from django.db import models
from django.conf import settings
from django.utils import timezone


#캐릭터
class Post(models.Model):
    #패시브
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #글쓴이 다른 모델에 대한 링크를 의미합니다.
    title = models.CharField(max_length=200)# 글자 수가 제한된 텍스트를 정의할 때 사용합니다. 글 제목같이 짧은 문자열 정보를 저장할 때 사용합니다.
    text = models.TextField()#글자 수에 제한이 없는 긴 텍스트를 위한 속성입니다
    created_date = models.DateTimeField(default=timezone.now) #작성일자
    published_date = models.DateTimeField(blank=True, null=True)
    #발행일자

    # 스킬
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()
    
    def __str__(self):
        return self.text