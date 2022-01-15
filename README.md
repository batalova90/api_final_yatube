## Приложение реализует API для социальной сети YATUBE ##

**Установка**

Клонировать репозиторий:

git clone https://github.com/batalova90/api_final_yatube/

## Установить зависимости из файла requirements.txt: ##
python3 -m pip install --upgrade pip

pip install -r requirements.txt

## Выполнить миграции: ##
python3 manage.py migrate

## Запустить проект: ##
python3 manage.py runserver

## Просмотреть доступные эндпоинты можно по адресу http://127.0.0.1:8000/redoc/
