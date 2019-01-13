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

### Project setup
```
yarn install
```

#### Compiles and hot-reloads for development
```
yarn run serve
```

#### Compiles and minifies for production
```
yarn run build
```

#### Run your tests
```
yarn run test
```

#### Lints and fixes files
```
yarn run lint
```

## TODO:
- test
  * selenium,
  * tornado testcase,
  * pytest,
  * coverage
- validation (валидация на сервере)
- CSRF
- журналирование
- документация (сгенерировать по doc классов)
- фронтенд:
    - date picker
