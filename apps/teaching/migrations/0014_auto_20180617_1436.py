# Generated by Django 2.0.5 on 2018-06-17 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0013_achievementsrecord_fundsrecord'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='achievementsrecord',
            name='TPA_belong',
        ),
        migrations.RemoveField(
            model_name='fundsrecord',
            name='TPA_belong',
        ),
        migrations.AddField(
            model_name='teachingprojectapply',
            name='achievements_record',
            field=models.TextField(default='', max_length=1000, verbose_name='成果记录'),
        ),
        migrations.AddField(
            model_name='teachingprojectapply',
            name='funds_record',
            field=models.TextField(default='', max_length=1000, verbose_name='经费使用记录'),
        ),
        migrations.DeleteModel(
            name='AchievementsRecord',
        ),
        migrations.DeleteModel(
            name='FundsRecord',
        ),
    ]
