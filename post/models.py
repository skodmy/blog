from django.db import models
from tinymce.models import HTMLField


class Tag(models.Model):
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Post(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(blank=True, null=True)
    content = HTMLField()
    date_and_time = models.DateTimeField(auto_now=True)

    def get_posts_by_tag(self, name):
        pass

    @property
    def description(self):
        return "{}...".format(self.content[:100].replace('<p>', '').replace('</p>', ''))

    def __str__(self):
        return "{} from {}".format(self.title, self.category.name)
