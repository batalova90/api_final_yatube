## Приложение реализует API для социальной сети YATUBE ##

**Установка**

Клонировать репозиторий:
```shell
git clone https://github.com/batalova90/api_final_yatube/
```
## Установить зависимости из файла requirements.txt: ##
```shell
python3 -m pip install --upgrade pip
```
```shell
pip install -r requirements.txt
```
## Выполнить миграции: ##
```shell
python3 manage.py migrate
```
## Запустить проект: ##
```shell
python3 manage.py runserver
```
## Просмотреть доступные эндпоинты
- http://127.0.0.1:8000/redoc/
