from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    CAT = (
        ('tanks', 'Танки'),
        ('healers', 'Хилы'),
        ('dealer', 'Торговцы'),
        ('smiths', 'Кузнецы'),
        ('tanners', 'Кожевники'),
        ('gild_masters', 'Гилдмастеры'),
        ('damage_dealers', 'ДД'),
        ('potion_makers', 'Зельевары'),
        ('spell_masters', 'Мастера заклинаний')
    )
    category = models.CharField(max_length=15, choices=CAT,verbose_name='Категория')
    dateCreation = models.DateTimeField(auto_now_add= True)
    title = models.CharField(max_length=256, verbose_name='Название')
    text = RichTextField()


class Response(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст')
    status = models.BooleanField(default=False)
    dateCreation = models.DateTimeField(auto_now_add=True)