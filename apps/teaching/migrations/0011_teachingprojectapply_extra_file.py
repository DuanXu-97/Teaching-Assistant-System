# Generated by Django 2.0.5 on 2018-06-17 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0010_teachingprojectapply_apply_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachingprojectapply',
            name='extra_file',
            field=models.CharField(default='', max_length=100, verbose_name='文件路径备用域'),
        ),
    ]
