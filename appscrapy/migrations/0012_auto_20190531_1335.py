# Generated by Django 2.0.5 on 2019-05-31 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appscrapy', '0011_auto_20190531_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='start_url',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='start_url',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
