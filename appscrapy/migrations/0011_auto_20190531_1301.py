# Generated by Django 2.0.5 on 2019-05-31 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appscrapy', '0010_auto_20190530_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='site',
            field=models.ManyToManyField(related_name='categories', to='appscrapy.Site'),
        ),
        migrations.AddField(
            model_name='site',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
