from django.db import models
import json
import json

#Класс статьи
class Article(models.Model):
    #Поле название статьи
    title = models.CharField('Article name', max_length = 200 )

    #Поле текста статьи
    text = models.TextField('Article text') 

    #Поле ссылки на картинку к статье в интернете 
    img_url = models.URLField('picture png', max_length = 250)	

class Users(models.Model):
    #Поле название статьи
    ip = models.CharField(max_length=16)
    contents = models.JSONField(null = True)

class Content(models.Model):
    #Поле название статьи
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    content = models.JSONField()

#Класс комментариев
class Comment(models.Model):

    # Наследование  от статьи
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    #Поле никнейма комментатора
    username = models.CharField('Author nickname', max_length = 50)

    #Поле текста комментария
    text = models.TextField('Comment text', max_length = 350)

    #Поле аватарта комментатора с пакой куда складываются изображения
    avatar = models.ImageField(upload_to='images/')

