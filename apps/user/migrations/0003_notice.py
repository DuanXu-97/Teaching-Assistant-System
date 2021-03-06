# Generated by Django 2.0.5 on 2018-06-19 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20180529_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50, verbose_name='标题')),
                ('content', models.TextField(default='', max_length=1000, verbose_name='发布内容')),
                ('publishTime', models.DateField(auto_now_add=True, null=True, verbose_name='发布时间')),
            ],
        ),
    ]
