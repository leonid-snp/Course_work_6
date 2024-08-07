# Приложение для рассылки уведомлений клиентам

### Для работы с проектом необходимо установить все зависимости в файле [pyproject.toml](pyproject.toml)
- poetry install


### Перед запуском приложения примените все миграции командой
- python3 manage.py migrate

### Выполни команду в консоли для тестового заполнения баз-данных
- python3 manage.py loaddata db.json

### Для работы заполните файл [.env.exampl](.env.exampl) затем переименуйте его в [.env](.env)

### django_setting
- SECRET_KEY= секретный ключ от приложения django
- DEBUG= режим отладки включен или выключен булево значение

### bd_setting
- NAME= имя вашей БД
- USER_BD= пользователь БД
- PASSWORD= пароль от БД
- HOST= хост
- PORT= порт

### # email_setting
- EMAIL_HOST=хост сервиса отправки писем
- EMAIL_PORT=порт
- EMAIL_USE_TLS=использовать безопасное соединение, булево значение
- EMAIL_USE_SSL=использовать защищенное соединение, булево значение
- EMAIL_HOST_USER=логин от сервиса отправки писем
- EMAIL_TO=почта с которой будут отправляться письма
- EMAIL_HOST_PASSWORD=пароль от приложения отправки писем

### # redis
- LOCATION=хост брокера редис

### Есть функционал отправки уведомлений
- создать аккаунт на сайте https://360.yandex.ru/mail/ если еще не создан
- в настройках https://mail.yandex.ru/?uid=1981646477#setup/client включить галочку на "С сервера imap.yandex.ru по протоколу IMAP"
- настроить аккаунт для писем зарегистрировать пароль для почты https://id.yandex.ru/security/app-passwords и сохранить его в файл .env


### Чтобы запустить приложение в консоли введите команду
- python manage.py runserver

### Перейдите по ссылке в терминале где написано 
- Starting development server at http://127.0.0.1:8000/

### Вы попали на главную страницу можете зарегистрироваться, есть всплывающее меню с кнопками выберите зарегистрироваться
- зарегистрироваться

### Следуйте инструкциям вам придет сообщение для подтверждения почты

### После подтверждения введите данные для входа в аккаунт если вас не перебросило на страницу входа перейдите самостоятельно в меню есть кнопка войти
- войти

### Далее решаете кем будет этот пользователь простым пользователем или модератором обязательно выберете соответствующие права для этого зайдите в админ и добавьте пользователю определенную группу
- вход в админ http://127.0.0.1:8000/admin/
- почта - admin@admin.com
- пароль - 12345

### Далее перезайдите пользователем который зарегистрировался и у него будет соответствующий функционал если пользователь то 
- пользователь может создавать, редактировать, удалять только свои созданные сообщения, клиенты, рассылки
- так же создавать статьи блога

### Если же вы модератор, то у вас функционал только такой
- включать, отключать рассылки
- просмотр, сообщений, клиентов рассылок, без возможности редактирования
- банить пользователя 

### Примечание по созданию рассылки
- дата начала рассылки, ровно в этот день в эту минуту придет сообщение
- периодичность, будет приходить сообщение ровно в указанный вами период
- по умолчанию рассылка создается со статусом создана, можно изменить на запущена при необходимости, но не обязательно, как придет время отправки сообщения статус сам поменяется на запущена
- для отключения рассылки укажите статус завершена

### Для запуска рассылки введите команду в терминале 
- celery -A config worker --beat --scheduler django --loglevel=info

### Для остановки рассылок введите команду в терминале
- ctrl+c

### Для выхода с сервера нажмите комбинацию клавиш в терминале
- ctrl+c