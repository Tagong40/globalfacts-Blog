# Generated by Django 3.1.4 on 2020-12-21 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20201221_0218'),
    ]

    operations = [
        migrations.AddField(
            model_name='commet',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='commet',
            name='status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
