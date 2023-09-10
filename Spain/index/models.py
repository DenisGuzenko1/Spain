from django.core.validators import RegexValidator
from django.db import models


class Level_language(models.Model):
    level_lan = models.CharField(max_length=255)

    def __str__(self):
        return self.level_lan


class User(models.Model):
    name = models.CharField(max_length=40, verbose_name=u'Имя')
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")  # Валидатор для номера телефона
    phone_number = models.CharField(validators=[phoneNumberRegex], blank=True, max_length=16,
                                    verbose_name=u'Телефон')  # Поле для номера телефона пользователя
    mail = models.EmailField(verbose_name=u'Эл.почта')
    level = models.ForeignKey(Level_language, on_delete=models.CASCADE, verbose_name=u'Ваш уровень языка', null=True)
    target = models.TextField(blank=True, null=True, verbose_name=u'Цель изучения языка')
    time = models.CharField(max_length=20, verbose_name=u'Удобное для занятий время')
    communication_method = models.URLField(verbose_name=u'Укажите удобный для вас способ связи', null=True)
    special_requirements = models.TextField(max_length=255, blank=True, null=True,
                                            verbose_name=u'Напишите о ваших специальных требованиях к занятиям')
    experience = models.TextField(max_length=255, blank=True, null=True,
                                  verbose_name=u'Напишите о вашем уровне изучения языков')
    about_user = models.TextField(max_length=255, blank=True, null=True,
                                  verbose_name=u'Расскажите о себе')
    comments = models.TextField(max_length=255, blank=True, null=True, verbose_name=u'Ваши комментарии')
    new_user_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
