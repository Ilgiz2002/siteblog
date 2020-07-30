from django.db import models

class Category(models.Model):
    title = models.CharField('Название', max_length=255)
    slug = models.SlugField('URL', max_length=255, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField('Название', max_length=50)
    slug = models.SlugField('URL', max_length=50, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']

class Post(models.Model):
    title = models.CharField('Название', max_length=255)
    slug = models.SlugField('URL', max_length=255, unique=True)
    author = models.CharField('Автор', max_length=100)
    content = models.TextField('Контент', blank=True)
    created_at = models.DateTimeField('Опубликовано', auto_now_add=True)
    photo = models.ImageField('Фото', upload_to='photos/%Y/%m/%d/', blank=True)
    views = models.IntegerField('Кол-во просмотров', default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья(ю)'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']


