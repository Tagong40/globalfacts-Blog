# Generated by Django 3.1.4 on 2020-12-19 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('article', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('category', models.ManyToManyField(null=True, to='blog.Category')),
            ],
        ),
    ]
