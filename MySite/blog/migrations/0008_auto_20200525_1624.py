# Generated by Django 3.0.6 on 2020-05-25 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='temp.jpg', upload_to='', verbose_name='Путь к картинке'),
        ),
    ]