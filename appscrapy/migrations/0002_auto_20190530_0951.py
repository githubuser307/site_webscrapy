# Generated by Django 2.0.5 on 2019-05-30 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appscrapy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='date_end',
            field=models.DateTimeField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='date_start',
            field=models.DateTimeField(blank=True, default=None),
        ),
    ]