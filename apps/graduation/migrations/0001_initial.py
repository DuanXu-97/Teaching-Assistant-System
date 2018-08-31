# Generated by Django 2.0.5 on 2018-06-18 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_auto_20180529_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='GraduationPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='无题目', max_length=20)),
                ('SelectionReport', models.FileField(null=True, upload_to='')),
                ('TaskReport', models.FileField(null=True, upload_to='')),
                ('MidtermReport', models.FileField(null=True, upload_to='')),
                ('GraduationReport', models.FileField(null=True, upload_to='')),
                ('DeclareBeginTime', models.DateField(null=True)),
                ('DeclareEndTime', models.DateField(null=True)),
                ('TaskBeginTime', models.DateField(null=True)),
                ('TaskEndTime', models.DateField(null=True)),
                ('MidtermBeginTime', models.DateField(null=True)),
                ('MidtermEndTime', models.DateField(null=True)),
                ('GraduatinoBeginTime', models.DateField(null=True)),
                ('GraduationEndTime', models.DateField(null=True)),
                ('SelectionReportFormTea', models.FileField(null=True, upload_to='')),
                ('TaskReportFormTea', models.FileField(null=True, upload_to='')),
                ('MidtermReportFormTea', models.FileField(null=True, upload_to='')),
                ('GraduationPaperFormTea', models.FileField(null=True, upload_to='')),
                ('GraduationPaperFormAss', models.FileField(null=True, upload_to='')),
                ('SelectionReportPass', models.CharField(default='', max_length=3)),
                ('TaskReportPass', models.CharField(default='', max_length=3)),
                ('MidtermReportPass', models.CharField(default='', max_length=3)),
                ('GraduationPaperPass', models.CharField(default='', max_length=3)),
                ('assesser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asserser', to='user.Teacher')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.Student')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='user.Teacher')),
            ],
        ),
    ]