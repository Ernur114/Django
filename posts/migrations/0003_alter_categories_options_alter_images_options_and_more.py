# Generated by Django 5.1.7 on 2025-04-14 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_categories'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'ordering': ('id',), 'verbose_name': 'категория', 'verbose_name_plural': 'категории'},
        ),
        migrations.AlterModelOptions(
            name='images',
            options={'ordering': ('id',), 'verbose_name': 'изображение', 'verbose_name_plural': 'изображения'},
        ),
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ('id',), 'verbose_name': 'пост', 'verbose_name_plural': 'посты'},
        ),
        migrations.AlterField(
            model_name='categories',
            name='post',
            field=models.ManyToManyField(blank=True, related_name='categories', to='posts.posts', verbose_name='пост'),
        ),
    ]
