# Generated by Django 3.1.4 on 2022-01-15 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220115_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='image',
            field=models.ImageField(blank=True, help_text='150x150px', upload_to='images/', verbose_name='Ссылка картинки'),
        ),
    ]
