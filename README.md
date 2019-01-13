# Панцирь
Микросервис веб-сервера Tornado с одностраничным клиентом, написанным с использованием фреймворка Vue.  

# Задание:
Разработать систему учёта персонала. 
Клиент-серверная архитектура. 
СУБД SQLite. 

## Обязательные поля у сотрудника: 
* ФИО, 
* дата рождения, 
* пол. 
* И ещё не менее 2 на ваш выбор:
    * должность,
    * отдел.

## Обязательные функции: 
* добавить сотрудника, 
* удалить, 
* отредактировать 
* одна на ваш выбор: переместить в архив

Нельзя использовать django, вместо него используем tornado.

В качестве frontend'а одна страница на jQuery или Vue (предпочтительней).

## TODO:
- test
  * selenium,
  * tornado testcase,
  * pytest,
  * coverage
+ rest api
+ vue
- validation (валидация на сервере, экранирование)
- CSRF
- журналирование
- документация (сгенерировать по doc классов)
- merge with vue
- deploy script
