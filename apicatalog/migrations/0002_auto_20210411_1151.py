# Generated by Django 3.1.6 on 2021-04-11 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apicatalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.CharField(default='', max_length=256),
        ),
    ]