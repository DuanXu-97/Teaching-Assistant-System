# Generated by Django 2.0.5 on 2018-06-19 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graduation', '0002_auto_20180618_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduationreporttime',
            name='DeclareBeginTime',
            field=models.DateField(default='2050-01-01'),
        ),
        migrations.AlterField(
            model_name='graduationreporttime',
            name='DeclareEndTime',
            field=models.DateField(default='2050-01-01'),
        ),
        migrations.AlterField(
            model_name='graduationreporttime',
            name='GraduatinoBeginTime',
            field=models.DateField(default='2050-01-01'),
        ),
        migrations.AlterField(
            model_name='graduationreporttime',
            name='GraduationEndTime',
            field=models.DateField(default='2050-01-01'),
        ),
        migrations.AlterField(
            model_name='graduationreporttime',
            name='MidtermBeginTime',
            field=models.DateField(default='2050-01-01'),
        ),
        migrations.AlterField(
            model_name='graduationreporttime',
            name='MidtermEndTime',
            field=models.DateField(default='2050-01-01'),
        ),
        migrations.AlterField(
            model_name='graduationreporttime',
            name='TaskBeginTime',
            field=models.DateField(default='2050-01-01'),
        ),
        migrations.AlterField(
            model_name='graduationreporttime',
            name='TaskEndTime',
            field=models.DateField(default='2050-01-01'),
        ),
    ]
