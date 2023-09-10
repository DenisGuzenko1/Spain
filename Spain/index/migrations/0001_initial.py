# Generated by Django 4.2.5 on 2023-09-10 16:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level_language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_lan', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Имя')),
                ('phone_number', models.CharField(blank=True, max_length=16, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')], verbose_name='Телефон')),
                ('mail', models.EmailField(max_length=254, verbose_name='Эл.почта')),
                ('target', models.TextField(blank=True, null=True, verbose_name='Цель изучения языка')),
                ('time', models.CharField(max_length=20, verbose_name='Удобное для занятий время')),
                ('communication_method', models.URLField(null=True, verbose_name='Укажите удобный для вас способ связи')),
                ('special_requirements', models.TextField(blank=True, max_length=255, null=True, verbose_name='Напишите о ваших специальных требованиях к занятиям')),
                ('experience', models.TextField(blank=True, max_length=255, null=True, verbose_name='Напишите о вашем уровне изучения языков')),
                ('about_user', models.TextField(blank=True, max_length=255, null=True, verbose_name='Расскажите о себе')),
                ('comments', models.TextField(blank=True, max_length=255, null=True, verbose_name='Ваши комментарии')),
                ('new_user_time', models.DateTimeField(auto_now=True)),
                ('level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.level_language', verbose_name='Ваш уровень языка')),
            ],
        ),
    ]