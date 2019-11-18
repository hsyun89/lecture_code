from django.db import models
from django.conf import settings
# from imagekit.models import ProcessedImageField
# from imagekit.processors import ResizeToFill, Thumbnail

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    image = models.ImageField(blank=True)
    # image = ProcessedImageField(                # Win7 OSError issue 로 Win10 이나 Mac 에서만 해주시는걸로..ㅠㅠ
    #     upload_to = 'articles/images',          # 저장 위치(MEDIA_ROOT/articles/images)
    #     processors = [ResizeToFill(200, 300)],  # 처리할 작업 목록
    #     format = 'jpeg',                        # 저장 포맷
    #     options = {'quality':90},               # 추가 옵션
    # )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)

    def __str__(self):
        return f'{self.id}번 글 - {self.title} : {self.content}'

class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'<Article({self.article_id}) : Comment({self.id})> - {self.content}'