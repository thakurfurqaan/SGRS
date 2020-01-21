# Generated by Django 3.0.2 on 2020-01-21 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('redressal', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sys_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='sys_user', to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('designation', models.CharField(choices=[('ST', 'Student'), ('UNI', 'University'), ('INS', 'Institute'), ('DEP', 'Department'), ('UNI_H', 'University_H'), ('INS_H', 'Institute_H'), ('DEP_H', 'Department_H')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='University_Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redressal.University')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Temp_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254)),
                ('designation', models.CharField(choices=[('ST', 'Student'), ('UNI', 'University'), ('INS', 'Institute'), ('DEP', 'Department'), ('UNI_H', 'University_H'), ('INS_H', 'Institute_H'), ('DEP_H', 'Department_H')], max_length=15)),
                ('uidb64', models.CharField(max_length=255)),
                ('token', models.CharField(max_length=255)),
                ('redressal_body', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redressal.Redressal_Body')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Temp_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.IntegerField(unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='accounts.Temp_User')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.IntegerField(unique=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redressal.Department')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Institute_Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redressal.Institute')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Department_Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redressal.Department')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
