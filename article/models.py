from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20 , verbose_name='Название категории')
    

    class Meta:
        db_table = "Category"
        verbose_name_plural= 'Категория'
        verbose_name= 'Категория'
    

    def __str__(self):
        return '%s' % self.name

class Article(models.Model):  #модель статьи
    class Meta():
        db_table = "Article"

    title = models.CharField(max_length=200 , verbose_name='Заголовок') #загаловок статьи
    text = models.TextField(verbose_name='Текст') #наполнение/текст
    date = models.DateTimeField(auto_now=True,verbose_name='Дата публикации') #дата публикации
    img = models.ImageField(('Картинка'),upload_to='images/', blank=True)
    likes = models.IntegerField(default=0) #лайки/рейтинг статей
    user = models.ForeignKey(User, null=True) 
    category = models.ForeignKey(Category)

class Comments(models.Model): #Модель комментариев
    class Meta():
        db_table = 'Comments'

    comments_text = models.TextField(verbose_name='Текст комментария:')
    comments_article = models.ForeignKey(Article) #каждый коммментарий присвается определённой статье
    username_comments = models.ForeignKey(User) #один комент один юзер
    date = models.DateTimeField(auto_now = True)


