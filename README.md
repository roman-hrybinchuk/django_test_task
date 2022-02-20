Для базы используеться SQLite. 
В ТЗ пишет PostgreSQL но не удобно тогда проект запускать.
Можно было бы в докере сделать но я думаю что это не столь важно.

Чтобы запустить надо установить зависимости.

`pip install -r requirements.txt`

Дальше сделать миграцию

`python manage.py migrate`

Создавать админа 

`python manage.py createsuperuser`

Поднять сам проект 

`python manage.py runserver`

В админке создать воркера  чтобы можно было проводить запросы.


Для авторизации в хедер Authorization добавить номер  телефона

1 REQ

`GET {host}/shop/trade-points`

`Headers 
    Authorization: {phone_number}`


2 REQ

`POST {host}/shop/visit/create`

`Headers 
    Authorization: {phone_number}`

BODY
```json
{
    "trade_point" : 1,
    "latitude" : 0.5,
    "longitude" : 0.5    
}
```





