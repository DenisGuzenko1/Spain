# Импортируем необходимые модули и классы
import os

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

from .forms import UserForm


def index(request):
    # Проверяем метод запроса - GET или POST
    if request.method == 'POST':
        # Если метод POST, создаем форму на основе данных из запроса
        form = UserForm(request.POST)
        # Проверяем валидность данных формы
        if form.is_valid():
            # Если форма допустима, сохраняем данные в базу данных
            user = form.save()

            # Создаем сообщение для отправки админу с данными пользователя
            subject = 'Новый пользователь зарегистрирован'
            message = f'Пользователь: {user.name}\n' \
                      f'Почта: {user.mail}\n' \
                      f'Телефон: {user.phone_number}\n' \
                      f'Email: {user.mail}\n' \
                      f'Уровень языка: {user.level}\n' \
                      f'Цель изучения: {user.target}\n' \
                      f'Удобное время: {user.time}\n' \
                      f'Способ связи: {user.communication_method}\n' \
                      f'Спец. требования: {user.special_requirements}\n' \
                      f'Опыт изучения: {user.experience}\n' \
                      f'О пользователе: {user.about_user}\n' \
                      f'Комментарий: {user.comments}.'

            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = os.getenv('EMAIL_HOST_USER')  # Замените на адрес админа

            # Отправляем письмо админу
            send_mail(subject, message, from_email, [recipient_list])


            # Показываем сообщение об успешной регистрации пользователю
            messages.success(request, 'Пользователь успешно создан и уведомление отправлено админу.')

            # Перенаправляем пользователя на страницу 'success'
            return redirect('success')
        else:
            # Если форма не валидна, возвращаем ее с ошибками для исправления
            return form
    else:
        # Если метод запроса - GET, создаем пустую форму для отображения на странице
        form = UserForm()

    # Отображаем страницу 'index.html' с формой в контексте
    return render(request, 'index.html', {'form': form})
