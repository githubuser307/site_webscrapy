# Generated by Django 2.0.5 on 2019-05-30 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appscrapy', '0006_auto_20190530_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(db_index=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(db_index=True, max_length=150)),
            ],
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='site',
        ),
        migrations.AddField(
            model_name='jobs',
            name='site',
            field=models.ManyToManyField(related_name='jobs', to='appscrapy.Site'),
        ),
    ]
