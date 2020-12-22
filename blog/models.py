from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from tinymce.models import HTMLField

STATUS = (
    ('Publish', 'Publish'),
    ('Unpublish', 'Unpublish'),
)


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    profile = models.ImageField(null=True)
    about = models.TextField(null=True, default="About Author")

    def __str__(self):
        return self.user.username

class Tag(models.Model):
    title = models.CharField(max_length=900)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=900)
    slug = models.SlugField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("category", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=500, null=True)
    slug = models.SlugField(null=True, unique=True, blank=True, max_length=500000000000000000000000000000000000)
    image = models.ImageField(null=True)
    article = HTMLField('Content')
    category = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
    header = models.BooleanField(default=False, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(choices=STATUS, max_length=50, null=True, default='Unpublish')
    date = models.DateTimeField(auto_now_add=True, null=True)
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation', null=True)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})
    


    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title + self.address)
    #     return super(Post, self).save(*args, **kwargs)


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_post_receiver, sender=Post)
    


class commet(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=60,null=True)
    email = models.EmailField(null=True)
    message = models.TextField(null=True)
    status = models.BooleanField(default=False, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

