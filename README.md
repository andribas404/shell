# shell
simple tornado service

# Задание:
Разработать систему учёта персонала. 
Клиент-серверная архитектура. 
СУБД SQLite. 

Обязательные поля у сотрудника : 
    ФИО, 
    дата рождения, 
    пол. 
    И ещё не менее 2 на ваш выбор.
    должность,
    отдел.

Обязательные функции: 
    добавить сотрудника, 
    удалить, 
    отредактировать 
    + одна на ваш выбор.
    переместить в архив

Нельзя использовать django, вместо него используем tornado.
В качестве frontend'а одна страница на jQuery или Vue (предпочтительней).

TODO:
test - selenium?, tornado testcase, pytest, coverage
+ rest api
+ vue
- templates (убрать лишнее)
- validation (валидация на клиенте, записываем любые данные)
проверка escape при записи - экранирование?
CSRF
logging
documentation
merge with vue
add app icon, link to github